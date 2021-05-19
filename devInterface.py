import DeviceInterface
from detectUsb import initDevice
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QRegExp, QObject, pyqtSignal
from PyQt5.QtGui import QRegExpValidator

class Signal(QObject):


    comSignal = pyqtSignal(str, str, str)


class devInterface(QtWidgets.QWidget):

    def __init__(self,VID_PID):
        super().__init__()
        self.VID_PID = VID_PID
        self.readBack = ""
        self.center()
        self.window = DeviceInterface.Ui_Form()  # create an instance of the Form UI class
        self.window.setupUi(self)  # pass our window to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the window when it is first instantiated
        self.window.westTopFrame.installEventFilter(self)
        self.dialogTitleBar()
        self.setShadow(self.window.Voltage_4)
        self.setShadow(self.window.Current_4)
        self.setShadow(self.window.Vlabel)
        self.setShadow(self.window.Alabel)
        self.setShadow(self.window.CR_VOLTAGE_LCD)
        self.setShadow(self.window.CR_CURRENT_LCD)
        self.setShadow(self.window.CR_VLABEL)
        self.setShadow(self.window.CR_CLABEL)
        self.alignLineEdits()
        self.connectBtns()

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

    #def fillPage(self):

    def alignLineEdits(self):

        for child in self.window.CR.findChildren(QtWidgets.QLineEdit):
            child.setAlignment(QtCore.Qt.AlignCenter)

        for child in self.window.CR.findChildren(QtWidgets.QComboBox):
            child.setEditable(True)
            lineEdit = child.lineEdit()
            lineEdit.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit.setReadOnly(True)
    def changePage(self):

        if self.sender() == self.window.CR_BTN:
            self.window.modePageStack.setCurrentIndex(0)

        elif self.sender() == self.window.CCD_BTN:
            self.window.modePageStack.setCurrentIndex(1)

        elif self.sender() == self.window.CC_BTN:
            self.window.modePageStack.setCurrentIndex(2)

        elif self.sender() == self.window.CV_BTN:
            self.window.modePageStack.setCurrentIndex(3)

    #def updatePage(self):
        #initDevice.

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

