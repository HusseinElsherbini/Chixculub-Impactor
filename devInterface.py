import DeviceInterface
from detectUsb import initDevice
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QRegExp, QObject, pyqtSignal
from PyQt5.QtGui import QRegExpValidator

class Signal(QObject):


    comSignal = pyqtSignal(str, str, str)


class devInterface(QtWidgets.QWidget):

    def __init__(self,VID_PID, comSignal, cmdSignal):
        super().__init__()
        self.VID_PID = VID_PID
        self.comSignal = comSignal
        self.cmdSignal = cmdSignal
        self.readBack = ""
        self.center()
        self.window = DeviceInterface.Ui_Form()  # create an instance of the Form UI class
        self.window.setupUi(self)  # pass our window to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the window when it is first instantiated
        self.window.westTopFrame.installEventFilter(self)
        self.dialogTitleBar()
        self.setShadows()
        self.alignLineEdits()
        self.connectBtns()
        self.updatePages()

    #######################################################################################################################################################################################
    #  Function: eventFilter                                                                                                                                                              #
    #  Purpose: triggered when the event filter installed on the Top Frame detects an event, it checks if the event is a mouseBtn press or mouseMove in order to move the whole dialog    #
    #######################################################################################################################################################################################
    def eventFilter(self, obj, event):

        if obj == self.window.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.window.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        return False

    def connectBtns(self):

        self.window.CR_BTN.clicked.connect(self.changePage)
        self.window.CV_BTN.clicked.connect(self.changePage)
        self.window.CC_BTN.clicked.connect(self.changePage)
        self.window.CCD_BTN.clicked.connect(self.changePage)
        self.window.CR_L1.returnPressed.connect(lambda: self.cmdSignal.emit("RES:STAT:L1 {}".format(self.window.CR_L1.text()),"RESistance:STATic:L1?", self.VID_PID, None,self.window.CR_L1.setText))
        self.window.CR_L2.returnPressed.connect(lambda: self.cmdSignal.emit("RES:STAT:L2 {}".format(self.window.CR_L2.text()), "RESistance:STATic:L2?",self.VID_PID, None, self.window.CR_L2.setText))


    def alignLineEdits(self):

        for children in zip(self.window.CR.findChildren(QtWidgets.QLineEdit), self.window.CC.findChildren(QtWidgets.QLineEdit)):
            for child in children:
                child.setAlignment(QtCore.Qt.AlignCenter)
                child.setAlignment(QtCore.Qt.AlignCenter)

        for children in zip(self.window.CR.findChildren(QtWidgets.QComboBox), self.window.CC.findChildren(QtWidgets.QComboBox)):
            for child in children:
                child.setEditable(True)
                lineEdit = child.lineEdit()
                lineEdit.setAlignment(QtCore.Qt.AlignCenter)
                lineEdit.setReadOnly(True)


    def changePage(self):

        if self.sender() == self.window.CR_BTN:
            self.window.modePageStack.setCurrentIndex(0)
            self.cmdSignal.emit("MODE CRM","MODE?", self.VID_PID, None, self.window.CR_RANGE_LABEL.setText)

        elif self.sender() == self.window.CCD_BTN:
            self.window.modePageStack.setCurrentIndex(1)
            self.comSignal.emit("MODE?", self.VID_PID, None, self.window.CR_RANGE_LABEL.setText)

        elif self.sender() == self.window.CC_BTN:
            self.window.modePageStack.setCurrentIndex(2)
            self.cmdSignal.emit("MODE CCM","MODE?", self.VID_PID, None, self.window.CC_RANGE_LABEL.setText)

        elif self.sender() == self.window.CV_BTN:
            self.window.modePageStack.setCurrentIndex(3)

    def updatePages(self):
        self.updatCRPage()
        self.updateCCpage()

    def updatCRPage(self):
        self.comSignal.emit("RESistance:STATic:L1?", self.VID_PID, None, self.window.CR_L1.setText)
        self.comSignal.emit("RESistance:STATic:L2?", self.VID_PID, None, self.window.CR_L2.setText)
        self.comSignal.emit("RESistance:STATic:RISE?", self.VID_PID, None, self.window.CR_SR1.setText)
        self.comSignal.emit("RESistance:STATic:FALL?", self.VID_PID, None, self.window.CR_SR2.setText)
        self.comSignal.emit("RESistance:STATic:IRNG?", self.VID_PID, None,self.window.CR_IRANGE.setCurrentText)
        self.comSignal.emit("*IDN?", self.VID_PID, None,self.window.CR_DEVNAME_LABEL.setText)
        self.comSignal.emit("FETCh:VOLTage?", self.VID_PID, None,self.window.CR_VOLTAGE_LCD.display)
        self.comSignal.emit("FETCh:CURRent?", self.VID_PID, None, self.window.CR_CURRENT_LCD.display)

    def updateCCpage(self):
        self.comSignal.emit("CURR:STATic:L1?", self.VID_PID,  None,self.window.CC_L1.setText)
        self.comSignal.emit("CURR:STATic:L2?", self.VID_PID, None,self.window.CC_L2.setText)
        self.comSignal.emit("CURR:STATic:RISE?", self.VID_PID, None,self.window.CC_SR1.setText)
        self.comSignal.emit("CURR:STATic:FALL?", self.VID_PID, None,self.window.CC_SR2.setText)
        self.comSignal.emit("CURR:STATic:VRNG?", self.VID_PID, None,self.window.CC_VRANGE.setCurrentText)
        self.comSignal.emit("*IDN?", self.VID_PID, None,self.window.CC_DEVNAME_LABEL.setText)
        self.comSignal.emit("FETCh:VOLTage?", self.VID_PID, None,self.window.CC_VOLTAGE_LCD.display)
        self.comSignal.emit("FETCh:CURRent?", self.VID_PID, None, self.window.CC_CURRENT_LCD.display)

    def center(self):

        self.move(QtWidgets.QApplication.desktop().screen().rect().center()- self.rect().center())


    #######################################################################################################################################################################################
    #  Function: dialogTitleBar                                                                                                                                                           #
    #  Purpose: removes native title bar and connects close and minimize button click events to self.close() and showMinimized() functions which close and minimized dialog respectively  #
    #           adds shadow effect to the delete, cancel and line edit                                                                                                                    #
    #######################################################################################################################################################################################
    def dialogTitleBar(self):
        self.window.closeBtn.clicked.connect(lambda: self.close())
        self.window.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)

    def setShadows(self):
        children = list(self.window.CR.findChildren(QtWidgets.QLabel)) + list(self.window.CR.findChildren(QtWidgets.QLCDNumber))

        for child in children:
            if child.inherits("QLabel") and (child.objectName() == "CR_VLABEL" or child.objectName() == "CR_CLABEL"):
                self.setShadow(child)
            elif child.inherits("QLCDNumber"):
                self.setShadow(child)

        children = list(self.window.CC.findChildren(QtWidgets.QLabel)) + list(self.window.CC.findChildren(QtWidgets.QLCDNumber))

        for child in children:
            if child.inherits("QLabel") and (child.objectName() == "CC_VLABEL" or child.objectName() == "CC_CLABEL"):
                self.setShadow(child)
            elif child.inherits("QLCDNumber"):
                self.setShadow(child)

