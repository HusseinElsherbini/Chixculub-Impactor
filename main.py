import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QPoint, QEvent, QObject, pyqtSignal, QThread, pyqtSlot, QMutex
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QFrame
import MainWindow
import uiFunctions
import subclasses
from detectUsb import initDevice
import random
import terminal
import modifyDialog
import devInterface
import time


mutex = QMutex()

##########################################################################################################################################################################################
#  Class: Signal                                                                                                                                                                         #
#  Purpose: Inherits from QObject class which enables the creation of custom signals in order to create arbitrary events.                                                                #
##########################################################################################################################################################################################
class Signal(QObject):

    customSignal = pyqtSignal(str)
    comSignal = pyqtSignal(str, str, str, object)
    cmdSignal = pyqtSignal(str, str, str,str, object)
    serialReconnectedSignal = pyqtSignal(str, str, str)

##########################################################################################################################################################################################
#  Class: communication                                                                                                                                                                  #
#  Purpose: Inherits from QObject class which enables the creation of custom signals in order to create arbitrary events. an object of this class is instantiated in the mainwindow and  #
#           moved to a thread which handles the processing of message from any device terminal. this is useful in order to avoid the blocking of the main GUI during readback timeout    #
##########################################################################################################################################################################################
class communication(QObject):

    queryRcvdSignal = pyqtSignal(str, str, object)
    messageSentSignal = pyqtSignal(str, str, object)

    def __init__(self, database):
        super().__init__()
        self.dataBase = database

    @pyqtSlot(str, str, str, object)
    def processMsg(self, msg, VID_PID, terminalName, obj):

        try:
            mutex.lock()
            if 'COM' in self.dataBase[VID_PID]['Model Name']:
                msgRcvd = self.dataBase[VID_PID]['Resource'].send(msg)
                self.queryRcvdSignal.emit(msgRcvd, terminalName, obj)
            else:
                msgRcvd = self.dataBase[VID_PID]['Resource'].query(msg)
                self.queryRcvdSignal.emit(msgRcvd, terminalName, obj)
            mutex.unlock()

        except Exception as e:
            mutex.unlock()
            self.queryRcvdSignal.emit(str(e), terminalName, obj)

    @pyqtSlot(str, str, str,str, object)
    def processCommand(self, cmd, query, VID_PID, terminalName, obj):
        try:
            mutex.lock()
            if 'COM' in self.dataBase[VID_PID]['Model Name']:
                self.dataBase[VID_PID]['Resource'].send_without_read(cmd)
                time.sleep(.1)
                msgRcvd = self.dataBase[VID_PID]['Resource'].send(query)
                self.queryRcvdSignal.emit(msgRcvd, terminalName, obj)
            else:
                self.dataBase[VID_PID]['Resource'].write(cmd)
                time.sleep(.1)
                msgRcvd = self.dataBase[VID_PID]['Resource'].query(query)
                self.queryRcvdSignal.emit(msgRcvd, terminalName, obj)
            mutex.unlock()

        except Exception as e:
            mutex.unlock()
            self.queryRcvdSignal.emit(str(e), terminalName, obj)


##########################################################################################################################################################################################
#  Class: worker                                                                                                                                                                         #
#  Purpose: Inherits from QObject class which enables the creation of custom signals in order to create arbitrary events. an object of this class is instantiated in the mainwindow and  #
#           moved to a thread which handles the detection of devices connected or disconnected from Computer. this is useful in order to avoid the blocking of the main GUI              #
##########################################################################################################################################################################################
class worker(QObject):

    newDeviceSignal = pyqtSignal(str, str)
    newComDeviceSignal = pyqtSignal(str)
    DeviceDisconnectedSignal = pyqtSignal(str, bool)
    removeDeviceSignal = pyqtSignal(str)
    noDevicesSignal = pyqtSignal()

    def __init__(self, connectedDevices, dataBase, present):
        super().__init__()
        self.dataBase = list(dataBase)
        self.detectusb = initDevice()
        self.connectedDevices = connectedDevices
        self.present = present

    def run(self):


        while True:
            d = self.detectusb.vidValidator()
            for device in d.keys():

                try:
                    if (device not in self.connectedDevices) and (device not in self.dataBase):

                        self.newDeviceSignal.emit(device, d[device])
                        self.dataBase.append(device)
                        self.connectedDevices.append(device)
                        self.present = False

                    elif (device not in self.connectedDevices) and (device in self.dataBase):

                        if 'COM' in initDevice.devices[device]['Model Name']:
                                mutex.lock()
                                for i in list(initDevice.resourceManager.list_resources()):
                                    if "ASRL" in i:
                                        initDevice.updateDevicesDB(device=device, present=True)
                                        self.newComDeviceSignal.emit(device)
                                        self.connectedDevices.append(device)
                                        self.DeviceDisconnectedSignal.emit(device,False)
                                mutex.unlock()

                        else:
                            self.newDeviceSignal.emit(device, d[device])
                            self.DeviceDisconnectedSignal.emit(device, False)
                            self.connectedDevices.append(device)
                            self.present = False

                except Exception as e:
                    mutex.unlock()
                    print(str(e) + ' {worker, run, line 103}')
                    continue

            for device in self.connectedDevices:

                try:
                    if device not in d.keys():

                        self.removeDeviceSignal.emit(device)
                        self.DeviceDisconnectedSignal.emit(device, True)
                        self.connectedDevices.remove(device)

                except Exception as e:
                        print(str(e) + ' {worker, run, line 118}')

            if len(self.connectedDevices) == 0 and self.present is not True:

                self.noDevicesSignal.emit()
                self.present = True

##########################################################################################################################################################################################
#  Class: ChixculubImpactor                                                                                                                                                              #
#  Purpose: Creates the main window for the GUI handles the addition of device frames when a device is connected. handles the main event loop. instantiates and executes dialogs related #
#           adding new devices, modifying devices and other features.                                                                                                                    #
##########################################################################################################################################################################################
class ChixculubImpactor(QMainWindow):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        ErrorLog = open('Error Log.txt', 'w')
        self.devices = initDevice()
        self.comSignal = Signal()
        self.initUI()
        sys.exit(self.app.exec_())

    def initUI(self):

        # create main window dimensions and center it

        self.createWindow()
        uiFunctions.UIFunctions.activateTitleBarButtons(self)
        self.installEventFilters()
        self.activateButtons()
        self.present = False
        self.enumerateDevices()
        self.deviceChangeThread()
        self.communicationThread()
        self.setShadow(self.ui.label_4)
        self.setShadow(self.ui.homeBtn)
        self.setShadow(self.ui.frame_17)
        self.setShadow(self.ui.terminalEdit)
        self.setShadow(self.ui.tabWidget)
        self.center()
        # keeps record of old position of window
        self.oldPos = self.pos()
        # activates the app
        self.show()

    def createWindow(self):

        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.resize(self.app.desktop().geometry().width(), self.app.desktop().geometry().height())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove window top bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # make window frameless
        self.ui.tabWidget.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide, None)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTerminal)

    def center(self):

        qr = self.frameGeometry()
        cp = self.app.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setShadow(self, qframe):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        qframe.setGraphicsEffect(shadow)

    def enumerateDevices(self):

        self.devices.detectDevices()
        i = 1
        for Device in initDevice.devices.keys():

            self.addDeviceFrame([initDevice.devices[Device]['Model Name'], "Device" + str(i) + '.png', "",
                                 initDevice.devices[Device]['Connection Type'], "", Device])
            initDevice.connectedDevices.append(Device)
            i += 1

        if len(initDevice.connectedDevices) == 0:
            if self.ui.frame_13.findChild(QFrame, "noDeviceFrame") == None:
                noDeviceFrame = subclasses.noDeviceFrame()
                self.ui.verticalLayout_9.addWidget(noDeviceFrame)
                self.present = True

    def installEventFilters(self):

        self.ui.appName.installEventFilter(self)

    def eventFilter(self, obj, event):

        if obj == self.ui.appName and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.ui.appName and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        return False

    def closeWindow(self):

        for device in initDevice.connectedDevices:

            try:
                initDevice.devices[device]['Resource'].close()

            except Exception as e:
                print(str(e) + ' {MainWindow, closeWindow, line 284}')

        self.app.closeAllWindows()

    def addTerminal(self):

        sender = self.sender().parentWidget()

        if self.ui.tabWidget.findChild(QtWidgets.QWidget,str(sender.objectName()).rsplit(None, 1)[0] + " Terminal") == None:
            if sender.VID_PID == '0A690879':
                self.addDevInterface(sender.VID_PID)
            newTerminal = terminal.terminal(str(sender.objectName()).rsplit(None, 1)[0] + " Terminal", sender.VID_PID)
            newTerminal.terminalEdit.msgSignal.customSignal.connect(self.passToCommThread)
            newTerminal.scriptArea.finishedAnalysis.runScriptSignal.connect(self.createScript)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.tabWidget.addTab(newTerminal, icon, str(sender.objectName()).rsplit(None, 1)[0] + " Terminal")
            #self.addDevInterface()


        else:
            pass

    def closeTerminal(self, currentIndex):

        self.currentIndex = currentIndex
        self.closeTerminalDialog = subclasses.removeDialog()
        self.closeTerminalDialog.uiDialog.label_2.setText("Are you sure you want to close this Terminal?")
        self.closeTerminalDialog.uiDialog.DeleteBtn.clicked.connect(self.deleteTerminal)
        self.closeTerminalDialog.uiDialog.CancelBtn.clicked.connect(self.closeTerminalDialog.close)
        self.closeTerminalDialog.exec_()

    def disableTerminal(self, tab, disconnected):

        try:
            term = self.ui.tabWidget.findChild(QtWidgets.QWidget,initDevice.devices[tab]['Model Name'].rsplit(None, 1)[0] + " Terminal")

            if term is not None:

                if disconnected:
                    self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(term)).setDisabled(True)
                    term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#C75450;\">Device Disconnected! </span>")

                elif not disconnected:
                    if not self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(term)).isEnabled():
                        self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(term)).setDisabled(False)
                        term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#C75450;\">Device Reconnected! </span>")
        except Exception as e:
            print(str(e)  + ' {{MainWindow, disableTerminal, line 335}}')

    def deleteTerminal(self):

        self.ui.tabWidget.widget(self.currentIndex).deleteLater()
        self.ui.tabWidget.removeTab(self.currentIndex)
        self.closeTerminalDialog.close()

    def createScript(self, list, devID, devList, terminalName):

        self.list = list
        codeBlock = ""
        scriptName = "Script" + devID + ".txt"
        script = open(scriptName, 'w')
        print(devList)
        loop = 0
        self.number = 0
        for cmd in list:
            for key, value in cmd.items():
                if key.lower() == "loop":
                    loop += 1
                    codeBlock += "for x in range({}):\n".format(value[0])
                    for x in range(loop):
                        codeBlock += '\t'
                    pass
                elif key.lower() == "delay":
                    script.write("time.sleep({})".format(value[0]))
                elif key.lower() == "endloop" and list.index(cmd) == len(list) - 1:
                    loop -= 1
                    pass
                elif terminal.script.intChecker(key):
                    msg = value[0]
                    dev = str(devList[key][1])
                    obj = ''
                    codeBlock += "self.comSignal.comSignal.emit(msg, dev, terminalName, obj)\n"
                    for x in range(loop):
                        codeBlock += '\t'


        singleCodeObject = compile(codeBlock.strip(), '<string>', 'single')
        exec(singleCodeObject)


    def activateButtons(self):

        self.ui.closeBtn.clicked.connect(self.closeWindow)
        self.ui.pushButton_4.clicked.connect(self.addDeviceDialog)
        self.ui.homeBtn.clicked.connect(lambda: self.ui.tabWidget.setCurrentIndex(0))

    def compileScript(self):

        singleCodeObject = compile('print(self.list)', '<string>', 'single')
        exec(singleCodeObject)

    def addDeviceFrame(self, args):

        arguments = [args[0], args[1], args[2], args[3], args[4], args[5]]
        newDevice = subclasses.deviceFrame(*arguments)
        self.ui.verticalLayout_9.addWidget(newDevice)
        newDevice.connectBtn.clicked.connect(self.addTerminal)
        newDevice.editBtn.clicked.connect(self.modifyDialog)
        return newDevice

    def removeDeviceFrame(self, deviceName):

        try:
            device = initDevice.devices[deviceName]['Model Name']
            self.ui.frame_13.findChild(QFrame, device).deleteLater()
            if 'COM' in initDevice.devices[deviceName]['Model Name']:
                initDevice.devices[deviceName]['Resource'].ser.close()
            else:
                initDevice.devices[deviceName]['Resource'].close()

        except Exception as e:
            print(str(e)  + ' {MainWindow, removeDeviceFrame, line 249}')

    def sendUserInput(self,msg, VID_PID, terminalName):

        if msg is not None:
            term = self.ui.tabWidget.findChild(QtWidgets.QWidget, terminalName)
            try:
                if msg[-1] == "?":
                    term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:black;\">{} </span>".format(initDevice.devices[VID_PID]['Resource'].query(msg)))
                else:
                    initDevice.devices[VID_PID]['Resource'].write(msg)
            except Exception as e:
                term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:black;\">{} </span>".format(e))

    def addUsbDevice(self, device, devName):

        if self.ui.frame_13.findChild(QFrame, "noDeviceFrame") is not None:
            self.ui.frame_13.findChild(QFrame, "noDeviceFrame").deleteLater()

        if device not in initDevice.devices.keys():

            for i in self.devices.resourceManager.list_resources():
                if "ASRL" in i:
                    self.devices.updateDevicesDB(device, devName,i)

                elif device == str(i)[8:12] + str(i)[16:20]:

                    self.devices.updateDevicesDB(i)
        else:
            self.devices.updateDevicesDB(device, present=True)

        try:
            arguments = [initDevice.devices[device]['Model Name'], "Device" + str(random.randint(1,3)) + '.png', "",initDevice.devices[device]['Connection Type'], "",device]
            newDevice = subclasses.deviceFrame(*arguments)
            newDevice.connectBtn.clicked.connect(self.addTerminal)
            newDevice.editBtn.clicked.connect(self.modifyDialog)
            self.ui.verticalLayout_9.addWidget(newDevice)

        except Exception as e:
            print(str(e) + ' {{MainWindow, add, line 315}}')

    def addNoDevicesPage(self):

        noDeviceFrame = subclasses.noDeviceFrame()
        self.ui.verticalLayout_9.addWidget(noDeviceFrame)


    def passToCommThread(self, msg, VID_PID, terminalName):
        obj = None
        self.comSignal.comSignal.emit(msg, VID_PID, terminalName, obj)

    def serialReconnected(self, device):
        try:
            arguments = [initDevice.devices[device]['Model Name'], "Device" + str(random.randint(1,3)) + '.png', "",initDevice.devices[device]['Connection Type'], "",device]
            newDevice = subclasses.deviceFrame(*arguments)
            newDevice.connectBtn.clicked.connect(self.addTerminal)
            newDevice.editBtn.clicked.connect(self.modifyDialog)
            self.ui.verticalLayout_9.addWidget(newDevice)

        except Exception as e:
            print(str(e) + ' {{MainWindow, serialReconnected, line 424}}')

    def appendMsg(self, msg, terminalName, obj):

        if terminalName == '':
            msg = msg.rstrip()
            obj(msg)
            return
        term = self.ui.tabWidget.findChild(QtWidgets.QWidget, terminalName)
        self.number += 1
        term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:black;\">{}. {} </span>".format(self.number, msg))

    def processDeviceModData(self,data, devName):

        if "COM" in devName:
            dev = self.ui.frame_13.findChild(QFrame, devName)
            if data['Device Name'] != " ":
                dev.deviceName.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{}</span></p></body></html>".format(data['Device Name']))
            if data["Timeout"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].ser.timeout = int(data['Timeout'])/1000.00
            if data["Baud Rate"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].ser.baud_rate = int(data['Baud Rate'])
            if data["Data Bits"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].ser.data_bits = int(data['Data Bits'])
            if data["Parity Bit"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].ser.parity_bit = data['Parity Bit']
        else:
            dev = self.ui.frame_13.findChild(QFrame, devName)
            if data['Device Name'] != "":
                self.ui.frame_13.findChild(QFrame, devName).deviceName.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{}</span></p></body></html>".format(data['Device Name']))

            if data["Timeout"] != "":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].timeout = int(data['Timeout'])

    def deviceChangeThread(self):

        self.thread = QtCore.QThread()
        self.worker = worker(initDevice.connectedDevices, initDevice.devices.keys(), self.present)
        self.worker.moveToThread(self.thread)
        self.worker.newDeviceSignal.connect(self.addUsbDevice)
        self.worker.newComDeviceSignal.connect(self.serialReconnected)
        self.worker.noDevicesSignal.connect(self.addNoDevicesPage)
        self.worker.DeviceDisconnectedSignal.connect(self.disableTerminal)
        self.worker.removeDeviceSignal.connect(self.removeDeviceFrame)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def communicationThread(self):
        self.comThread = QThread()
        self.comWorker = communication(initDevice.devices)
        self.comWorker.moveToThread(self.comThread)
        self.comWorker.queryRcvdSignal.connect(self.appendMsg)
        self.comSignal.comSignal.connect(self.comWorker.processMsg)
        self.comSignal.cmdSignal.connect(self.comWorker.processCommand)
        self.comThread.start()

    def modifyDialog(self):

        if "COM" in self.sender().parent().objectName():
            self.modify_dialog = modifyDialog.modifySerialDialog(*[self.sender().parent().objectName()])
            self.modify_dialog.dialogFinishedSignal.dialogClosedSignal.connect(self.processDeviceModData)
            self.modify_dialog.show()
        else:
            self.modify_dialog = modifyDialog.modifyUsbDialog(*[self.sender().parent().objectName()])
            self.modify_dialog.dialogFinishedSignal.dialogClosedSignal.connect(self.processDeviceModData)
            self.modify_dialog.show()

    def addDevInterface(self, VID_PID):

        initDevice.devices[VID_PID]["Device interface"] = devInterface.devInterface(VID_PID, self.comSignal.comSignal, self.comSignal.cmdSignal)
        initDevice.devices[VID_PID]['Device interface'].show()

    def addDeviceDialog(self):

        addDevice = subclasses.addDeviceDialog()
        addDevice.exec_()
        if addDevice.step != 1:
            icon = ""
            if addDevice.device["Device Type"] == "Oscilloscope":
                icon = "oscilloscope.png"
            elif addDevice.device["Device Type"] == "Power Supply":
                icon = "power-supply.png"
            elif addDevice.device["Device Type"] == "Digital Multimeter":
                icon = "multimeter.png"

            if addDevice.device["Connection Type"] == "LAN":
                self.addDeviceFrame([addDevice.device["DEVICE NAME"], icon, addDevice.device["Device Type"],
                                     addDevice.device["Connection Type"], addDevice.device["IP ADDRESS"]])
            elif addDevice.device["Connection Type"] == "RS232":
                self.addDeviceFrame([addDevice.device["DEVICE NAME"], icon, addDevice.device["Device Type"],
                                     addDevice.device["Connection Type"], ""])

def main():
    Terminal = ChixculubImpactor()
    Terminal.ErrorLog.close()

if __name__ == '__main__':
    main()
