import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QFrame
import Dialog
import MainWindow
import uiFunctions
import subclasses


class ChixculubImpactor(QMainWindow):

    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)
        self.buttons = {}
        self.dialogs = {}
        super().__init__()
        self.initUI()

        sys.exit(self.app.exec_())

    def initUI(self):

        # create main window dimensions and center it

        self.createWindow()
        uiFunctions.UIFunctions.activateTitleBarButtons(self)
        self.installEventFilters()

        self.addDeviceFrame(["Power Supply", "power-supply.png", "HET-2", "RS232"])
        self.addDeviceFrame(["Digital Multimeter", "multimeter.png", "Tektronix", "LAN"])
        self.addDeviceFrame(["Oscilloscope", "oscilloscope.png", "Yokogawa", "LAN"])
        self.activateButtons()
        self.setShadow(self.ui.frame_14)
        self.setShadow(self.ui.frame_17)
        self.center()
        # keeps record of old position of window
        self.oldPos = self.pos()
        # activates the app
        self.show()


    def createWindow(self):

        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
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

        arguments = [args[0], args[1], args[2], args[3]]
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
        # addDevice.show()

def main():
    Terminal = ChixculubImpactor()


if __name__ == '__main__':
    main()
