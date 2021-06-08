from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QRegExp, QObject, pyqtSignal
from PyQt5.QtGui import QRegExpValidator
import SerialDialog
import UsbDialog
import EthernetDialog


class mySignal(QObject):

    dialogClosedSignal = pyqtSignal(dict, str)

class modifySerialDialog(QtWidgets.QDialog):

    def __init__(self, *args):

        super().__init__()
        self.dev = args[0]
        self.uiDialog = SerialDialog.Ui_SerialModDialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(self)  # install an event filter to know when an event occurs on title bar
        self.uiDialog.DeviceNameLE.installEventFilter(self)
        self.uiDialog.TimeoutLE.installEventFilter(self)
        self.dialogTitleBar()  # make window frameless
        self.setShadow(self.uiDialog.DeviceTypeCB)
        self.setShadow(self.uiDialog.ConfirmBtn)
        self.setShadow(self.uiDialog.BaudRateCB)
        self.setShadow(self.uiDialog.statusLabel)
        self.setShadow(self.uiDialog.DeviceNameLE)
        self.setShadow(self.uiDialog.DataBitsCB)
        self.setShadow(self.uiDialog.ParityBitCB)
        self.setShadow(self.uiDialog.TimeoutLE)
        regex = QRegExp("[1-9]\\d{0,3}")
        validator = QRegExpValidator(regex, self)
        self.dialogFinishedSignal = mySignal()
        self.uiDialog.TimeoutLE.setValidator(validator)
        self.data = {}
        self.ConnectBtns()

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(self.close)
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def ConnectBtns(self):

        self.uiDialog.ConfirmBtn.clicked.connect(self.collectData)


    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)

    def eventFilter(self, obj, event):

        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.FocusOut:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(True)

        if obj == self.uiDialog.TimeoutLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.TimeoutLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.TimeoutLE and event.type() == QEvent.FocusOut:
            self.uiDialog.TimeoutLE.graphicsEffect().setEnabled(True)

        return False

    def collectData(self):

        if self.uiDialog.DeviceNameLE.text()  == "":
            self.data.update({"Device Name": " "})

        else:
            self.data.update({"Device Name": self.uiDialog.DeviceNameLE.text()})

        if self.uiDialog.TimeoutLE.text() == "":
            self.data.update({"Timeout": " "})

        else:
            self.data.update({"Timeout": self.uiDialog.TimeoutLE.text()})

        if self.uiDialog.DeviceTypeCB.currentIndex() == 0:

            self.data.update({"Device Type": " "})
        else:
            self.data.update({"Device Type": self.uiDialog.DeviceTypeCB.currentText()})

        if self.uiDialog.BaudRateCB.currentIndex() == 0:
            self.data.update({"Baud Rate": " "})

        else:
            self.data.update({"Baud Rate": self.uiDialog.BaudRateCB.currentText()})

        if self.uiDialog.DataBitsCB.currentIndex() == 0:
            self.data.update({"Data Bits": " "})

        else:
            self.data.update({"Data Bits": self.uiDialog.DataBitsCB.currentText()})

        if self.uiDialog.ParityBitCB.currentIndex()  == 0:
            self.data.update({"Parity Bit": " "})

        else:
            self.data.update({"Parity Bit": self.uiDialog.ParityBitCB.currentText()})

        self.close()
        self.dialogFinishedSignal.dialogClosedSignal.emit(self.data, self.dev)





class modifyUsbDialog(QtWidgets.QDialog):

    def __init__(self, *args):
        super().__init__()
        self.dev = args[0]
        self.uiDialog = UsbDialog.Ui_UsbModDialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(self)  # install an event filter to know when an event occurs on title bar
        self.uiDialog.DeviceNameLE.installEventFilter(self)
        self.uiDialog.DeviceTimeoutLE.installEventFilter(self)
        self.dialogTitleBar()  # make window frameless
        self.setShadow(self.uiDialog.DeviceTypeCB)
        self.setShadow(self.uiDialog.ConfirmBtn)
        self.setShadow(self.uiDialog.statusLabel)
        self.setShadow(self.uiDialog.DeviceNameLE)
        self.setShadow(self.uiDialog.DeviceTimeoutLE)
        regex = QRegExp("[1-9]\\d{0,3}")
        validator = QRegExpValidator(regex, self)
        self.uiDialog.DeviceTimeoutLE.setValidator(validator)
        self.data = {}
        self.dialogFinishedSignal = mySignal()
        self.ConnectBtns()

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(self.close)
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def ConnectBtns(self):

        self.uiDialog.ConfirmBtn.clicked.connect(self.collectData)


    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)

    def eventFilter(self, obj, event):

        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.FocusOut:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(True)

        if obj == self.uiDialog.DeviceTimeoutLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.DeviceTimeoutLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.DeviceTimeoutLE and event.type() == QEvent.FocusOut:
            self.uiDialog.DeviceTimeoutLE.graphicsEffect().setEnabled(True)

        return False

    def collectData(self):

        if self.uiDialog.DeviceNameLE.text()  is None:
            self.data.update({"Device Name": " "})

        else:
            self.data.update({"Device Name": self.uiDialog.DeviceNameLE.text()})

        if self.uiDialog.DeviceTimeoutLE.text() is None:
            self.data.update({"Timeout": " "})

        else:
            self.data.update({"Timeout": self.uiDialog.DeviceTimeoutLE.text()})

        if self.uiDialog.DeviceTypeCB.currentIndex() == 0:

            self.data.update({"Device Type": " "})
        else:
            self.data.update({"Device Type": self.uiDialog.DeviceTypeCB.currentText()})


        self.close()
        self.dialogFinishedSignal.dialogClosedSignal.emit(self.data, self.dev)

class modifyLanDialog(QtWidgets.QDialog):

    def __init__(self, *args):
        super().__init__()
        self.dev = args[0]
        self.uiDialog = EthernetDialog.Ui_EthernetDialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(self)  # install an event filter to know when an event occurs on title bar
        self.uiDialog.DeviceNameLE.installEventFilter(self)
        self.uiDialog.IPADDRESSLE.installEventFilter(self)
        self.dialogTitleBar()  # make window frameless
        self.setShadow(self.uiDialog.IPADDRESSLE)
        self.setShadow(self.uiDialog.ConfirmBtn)
        self.setShadow(self.uiDialog.statusLabel)
        self.setShadow(self.uiDialog.DeviceNameLE)
        self.setShadow(self.uiDialog.PortNumberLE)
        self.PortnNumberFormat = "^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
        pnRegex = QRegExp(self.PortnNumberFormat)
        pnValidCheck = QRegExpValidator(pnRegex, self)
        self.uiDialog.PortNumberLE.setValidator(pnValidCheck)
        self.ipFormat = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegExp(
            "^" + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "$")
        ipValidCheck = QRegExpValidator(ipRegex, self)
        self.uiDialog.IPADDRESSLE.setValidator(ipValidCheck)
        self.data = {}
        self.dialogFinishedSignal = mySignal()
        self.ConnectBtns()

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(self.close)
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def ConnectBtns(self):

        self.uiDialog.ConfirmBtn.clicked.connect(self.collectData)


    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)

    def eventFilter(self, obj, event):

        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.FocusOut:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(True)

        if obj == self.uiDialog.PortNumberLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.PortNumberLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.PortNumberLE and event.type() == QEvent.FocusOut:
            self.uiDialog.PortNumberLE.graphicsEffect().setEnabled(True)

        if obj == self.uiDialog.IPADDRESSLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.IPADDRESSLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.IPADDRESSLE and event.type() == QEvent.FocusOut:
            self.uiDialog.IPADDRESSLE.graphicsEffect().setEnabled(True)


        return False

    def collectData(self):

        if self.uiDialog.IPADDRESSLE is None:
            self.uiDialog.statusLabel.setText("Please Enter an IP Address")

        else:


            self.data.update({"IP Address": self.uiDialog.IPADDRESSLE.text()})

            if self.uiDialog.DeviceNameLE.text() == "":
                self.data.update({"Device Name": " "})

            else:
                self.data.update({"Device Name": self.uiDialog.DeviceNameLE.text() + " (LAN)"})

            if self.uiDialog.PortNumberLE.text() is None:
                self.data.update({"Port Number": " "})

            else:
                self.data.update({"Port Number": self.uiDialog.PortNumberLE.text()})


            self.close()
            self.dialogFinishedSignal.dialogClosedSignal.emit(self.data, self.dev)