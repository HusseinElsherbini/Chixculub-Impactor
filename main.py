import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
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
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        self.ui.frame_14.setGraphicsEffect(shadow)
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
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        self.ui.pushButton_4.setGraphicsEffect(shadow)
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

        addDevice = addDeviceDialog()
        addDevice.exec_()
        # addDevice.show()



class addDeviceDialog(QtWidgets.QDialog):
    # creates an instance of a dialog when the ADD device button is pressed

    def __init__(self, parent=None):
        super().__init__(parent)
        self.uiDialog = Dialog.Ui_Dialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.TopFrame.installEventFilter(self)  # install an event filter to know when an event occurs on title bar
        uiFunctions.dialogUIFunctions.dialogTitleBar(self)  # make window frameless

    def eventFilter(self, obj, event):

        if obj == self.uiDialog.TopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.TopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        return False





def main():
    Terminal = ChixculubImpactor()


if __name__ == '__main__':
    main()
