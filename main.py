import sys
import time
import serial.tools.list_ports as portsList
from PyQt5 import QtWidgets, QtGui, QtCore, uic, Qt
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QFrame
import Dialog
import MainWindow
import uiFunctions
import subclasses
import threading
import detectUsb
import pyvisa
import random

class ChixculubImpactor(QMainWindow):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        self.connectedDevices = []
        self.initUI()
        self.ComPorts = [port[0] for port in list(portsList.comports())]
        sys.exit(self.app.exec_())

    def initUI(self):

        # create main window dimensions and center it

        self.createWindow()
        uiFunctions.UIFunctions.activateTitleBarButtons(self)
        self.installEventFilters()
        self.activateButtons()
        self.watchedComPorts = []
        self.enumerateDevices()
        self.devices.startThread(self.deviceStatus, ())
        self.setShadow(self.ui.label_4)
        self.setShadow(self.ui.homeBtn)
        self.setShadow(self.ui.frame_17)
        self.setShadow(self.ui.textEdit)
        self.center()
        # keeps record of old position of window
        self.oldPos = self.pos()
        # activates the app
        self.show()

    '''
    def checkComPorts(self, interval):

        self.ComPorts = [tuple(port) for port in list(portsList.comports())]
        print(self.ComPorts)
        while(True):
            self.ComPorts = [tuple(port) for port in list(portsList.comports())]
            for port in self.watchedComPorts:
    '''

    def enumerateDevices(self):

        self.devices = detectUsb.initDevice()
        i = 1
        for Device in self.devices.devices.keys():
            self.addDeviceFrame([self.devices.devices[Device]['Model Name'], "Device" + str(i) + '.png', "", self.devices.devices[Device]['Connection Type'], ""])
            self.connectedDevices.append(self.devices.devices[Device]['Model Name'])
            i += 1

    def createWindow(self):

        self.ui = MainWindow.Ui_MainWindow()
        # self.ui = test.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.resize(self.app.desktop().geometry().width()/4, self.app.desktop().geometry().height()/2)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove window top bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # make window frameless

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

    def activateButtons(self):

        self.ui.pushButton_4.clicked.connect(self.addDeviceDialog)

    def addDeviceFrame(self, args):

        arguments = [args[0], args[1], args[2], args[3], args[4]]
        newDevice = subclasses.deviceFrame(*arguments)
        self.ui.verticalLayout_9.addWidget(newDevice)
        return newDevice

    def removeDeviceFrame(self, deviceName):

        try:
            index = self.ui.verticalLayout_9.count()

            while index >=0:
                print(index)
                if self.ui.verticalLayout_9.itemAt(index).widget().objectName() == deviceName:

                    print("here")
                    self.ui.verticalLayout_9.itemAt(index).widget().deleteLater()
                index -= 1
                print(self.ui.verticalLayout_9.itemAt(index).widget().objectName())

        except AttributeError:
            pass

    def deviceStatus(self):


        while True:
            i = 0
            for device in self.devices.resourceManager.list_resources():
                d = self.devices.vidValidator()
                try:

                    if str(device)[8:12] + str(device)[16:20] in d:
                        if str(device)[8:12] + str(device)[16:20] not in self.devices.devices.keys():
                            self.devices.updateDevicesDB(device)


                        if self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'] not in self.connectedDevices:

                            self.connectedDevices.append(self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'])
                            self.addDeviceFrame([self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'], "Device" + str(random.randint(1,3)) + '.png', "",self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Connection Type'], ""])


                    else:
                        try:
                            if self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'] in self.connectedDevices:
                                self.removeDeviceFrame(self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'])
                                self.connectedDevices.remove(self.devices.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'])
                        except KeyError:
                            pass


                except pyvisa.errors.VisaIOError:
                    pass

            time.sleep(2)

    def center(self):

        qr = self.frameGeometry()
        cp = self.app.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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


if __name__ == '__main__':
    main()
