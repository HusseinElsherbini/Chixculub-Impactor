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


mutex = QMutex()

class Signal(QObject):

    customSignal = pyqtSignal(str)
    comSignal = pyqtSignal(str, str, str)

class communication(QObject):

    messageRcvdSignal = pyqtSignal(str, str)

    def __init__(self, database):
        super().__init__()
        self.dataBase = database

    @pyqtSlot(str, str, str)
    def processMsg(self, input, VID_PID, terminalName):

        try:
            mutex.lock()
            msgRcvd = self.dataBase[VID_PID]['Resource'].query(input)
            mutex.unlock()
            self.messageRcvdSignal.emit(msgRcvd, terminalName)

        except Exception as e:
            mutex.unlock()
            self.messageRcvdSignal.emit(str(e), terminalName)




class worker(QObject):

    newDeviceSignal = pyqtSignal(str, str)
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

                        self.newDeviceSignal.emit(device, d[device])
                        self.DeviceDisconnectedSignal.emit(device, False)
                        self.connectedDevices.append(device)
                        self.present = False

                except Exception as e:
                    print(e)

            for device in self.connectedDevices:

                try:
                    if device not in d.keys():


                        self.removeDeviceSignal.emit(device)
                            #self.lock.wait(timeout=None)
                        self.DeviceDisconnectedSignal.emit(device, True)
                            #self.lock.wait(timeout=None)
                        self.connectedDevices.remove(device)

                except Exception as e:
                        print(e)

            if len(self.connectedDevices) == 0 and self.present is not True:

                self.noDevicesSignal.emit()
                self.present = True


class ChixculubImpactor(QMainWindow):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        ErrorLog = open('Error Log.txt', 'w')
        self.devices = initDevice()
        self.devices.detectDevices()
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


    def enumerateDevices(self):

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

    def createWindow(self):

        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.resize(self.app.desktop().geometry().width(), self.app.desktop().geometry().height())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove window top bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # make window frameless
        self.ui.tabWidget.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide, None)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTerminal)

    def setShadow(self, qframe):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        qframe.setGraphicsEffect(shadow)

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

    def closeTerminal(self, currentIndex):

        self.currentIndex = currentIndex
        self.closeTerminalDialog = subclasses.removeDialog()
        self.closeTerminalDialog.uiDialog.label_2.setText("Are you sure you want to close this Terminal?")
        self.closeTerminalDialog.uiDialog.DeleteBtn.clicked.connect(self.deleteTerminal)
        self.closeTerminalDialog.uiDialog.CancelBtn.clicked.connect(self.closeTerminalDialog.close)
        self.closeTerminalDialog.exec_()

    def deleteTerminal(self):

        self.ui.tabWidget.widget(self.currentIndex).deleteLater()
        self.ui.tabWidget.removeTab(self.currentIndex)
        self.closeTerminalDialog.close()

    def activateButtons(self):

        self.ui.closeBtn.clicked.connect(self.closeWindow)
        self.ui.pushButton_4.clicked.connect(self.addDeviceDialog)
        self.ui.homeBtn.clicked.connect(lambda: self.ui.tabWidget.setCurrentIndex(0))

    def addDeviceFrame(self, args):

        arguments = [args[0], args[1], args[2], args[3], args[4], args[5]]
        newDevice = subclasses.deviceFrame(*arguments)
        self.ui.verticalLayout_9.addWidget(newDevice)
        newDevice.connectBtn.clicked.connect(self.addTerminal)
        newDevice.editBtn.clicked.connect(self.modifyDialog)
        return newDevice

    def removeDeviceFrame(self, deviceName):
        device = initDevice.devices[deviceName]['Model Name']
        try:
            self.ui.frame_13.findChild(QFrame, device).deleteLater()
            initDevice.devices[deviceName]['Resource'].close()

        except Exception as e:
            print(e)



    def addTerminal(self):

        sender = self.sender().parentWidget()

        if self.ui.tabWidget.findChild(QtWidgets.QWidget, str(sender.objectName()).rsplit(None,1)[0] + " Terminal") == None:
            newTerminal = terminal.terminal(str(sender.objectName()).rsplit(None,1)[0] + " Terminal", sender.VID_PID)
            #newTerminal.terminalEdit.msgSignal.customSignal.connect(self.sendUserInput)
            newTerminal.terminalEdit.msgSignal.customSignal.connect(self.passToCommThread)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.tabWidget.addTab(newTerminal,icon,str(sender.objectName()).rsplit(None,1)[0] + " Terminal")

        else:
            pass

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

    def closeWindow(self):

        for device in self.devices.resourceManager.list_opened_resources():
            try:
                device.close()
            except Exception as e:
                print(e)


        self.app.closeAllWindows()

    def add(self, device, devName):

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

        arguments = [initDevice.devices[device]['Model Name'], "Device" + str(random.randint(1,3)) + '.png', "",initDevice.devices[device]['Connection Type'], "",device]
        newDevice = subclasses.deviceFrame(*arguments)
        newDevice.connectBtn.clicked.connect(self.addTerminal)
        newDevice.editBtn.clicked.connect(self.modifyDialog)
        self.ui.verticalLayout_9.addWidget(newDevice)

        #self.lock.set()

    def disableTerminal(self, tab, disconnected):

        term = self.ui.tabWidget.findChild(QtWidgets.QWidget,initDevice.devices[tab]['Model Name'].rsplit(None, 1)[0] + " Terminal")

        if term is not None:
            try:
                if disconnected:
                    self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(term)).setDisabled(True)
                    term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#C75450;\">Device Disconnected! </span>")

                elif not disconnected:
                    if not self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(term)).isEnabled():
                        self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(term)).setDisabled(False)
                        term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#C75450;\">Device Reconnected! </span>")
            except Exception as e:
                print(e)


    def addNoDevicesPage(self):

        noDeviceFrame = subclasses.noDeviceFrame()
        self.ui.verticalLayout_9.addWidget(noDeviceFrame)

    def center(self):

        qr = self.frameGeometry()
        cp = self.app.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def passToCommThread(self, input, VID_PID, terminalName):

        self.comSignal.comSignal.emit(input, VID_PID, terminalName)

    def communicationThread(self):
        self.comThread = QThread()
        self.comWorker = communication(initDevice.devices)
        self.comWorker.moveToThread(self.comThread)
        self.comWorker.messageRcvdSignal.connect(self.appendMsg)
        self.comSignal.comSignal.connect(self.comWorker.processMsg)
        self.comThread.start()

    def appendMsg(self, msg, terminalName):
        term = self.ui.tabWidget.findChild(QtWidgets.QWidget, terminalName)
        term.readBack.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:black;\">{} </span>".format(msg))

    def processDeviceModData(self,data, devName):

        if "COM" in devName:
            dev = self.ui.frame_13.findChild(QFrame, devName)
            if data['Device Name'] != " ":
                dev.deviceName.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{}</span></p></body></html>".format(data['Device Name']))
            if data["Timeout"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].timeout = int(data['Timeout'])

            if data["Baud Rate"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].baud_rate = int(data['Baud Rate'])
            if data["Data Bits"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].data_bits = int(data['Data Bits'])
            if data["Parity Bit"] != " ":
                VID = dev.VID_PID
                initDevice.devices[VID]['Resource'].parity_bit = data['Parity Bit']
            initDevice.devices[VID]['Resource'].close()
            initDevice.devices[VID]['Resource'].open()
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
        self.worker.newDeviceSignal.connect(self.add)
        self.worker.noDevicesSignal.connect(self.addNoDevicesPage)
        self.worker.DeviceDisconnectedSignal.connect(self.disableTerminal)
        self.worker.removeDeviceSignal.connect(self.removeDeviceFrame)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def modifyDialog(self):

        if "COM" in self.sender().parent().objectName():
            self.modify_dialog = modifyDialog.modifySerialDialog(*[self.sender().parent().objectName()])
            self.modify_dialog.dialogFinishedSignal.dialogClosedSignal.connect(self.processDeviceModData)
            self.modify_dialog.show()
        else:
            self.modify_dialog = modifyDialog.modifyUsbDialog(*[self.sender().parent().objectName()])
            self.modify_dialog.dialogFinishedSignal.dialogClosedSignal.connect(self.processDeviceModData)
            self.modify_dialog.show()


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
