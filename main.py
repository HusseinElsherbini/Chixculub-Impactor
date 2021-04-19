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



class ChixculubImpactor(QMainWindow):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.buttons = {}
        self.dialogs = {}
        super().__init__()
        self.initUI()
        self.ComPorts = [port[0] for port in list(portsList.comports())]

        sys.exit(self.app.exec_())

    def initUI(self):

        # create main window dimensions and center it

        self.createWindow()
        uiFunctions.UIFunctions.activateTitleBarButtons(self)
        self.installEventFilters()
        self.addDeviceFrame(["Power Supply", "power-supply.png", "HET-2", "RS232", ""])
        self.addDeviceFrame(["Digital Multimeter", "multimeter.png", "Tektronix", "ETHERNET", "192.255.68.11"])
        self.addDeviceFrame(["Oscilloscope", "oscilloscope.png", "Yokogawa", "ETHERNET", "192.255.68.234"])
        self.activateButtons()
        self.watchedComPorts = []
        self.setShadow(self.ui.frame_14)
        self.setShadow(self.ui.label_4)
        self.setShadow(self.ui.homeBtn)
        self.setShadow(self.ui.frame_17)
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
    def createWindow(self):

        self.ui = MainWindow.Ui_MainWindow()
        #self.ui = test.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.resize(self.app.desktop().geometry().width()/4, self.app.desktop().geometry().height()/2)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove window top bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # make window frameless

    def setShadow(self, QFrame):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        QFrame.setGraphicsEffect(shadow)

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

    def center(self):

        qr = self.frameGeometry()
        cp = self.app.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addDeviceDialog(self):

        addDevice = subclasses.addDeviceDialog()
        addDevice.exec_()
        if addDevice.step !=1:
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
