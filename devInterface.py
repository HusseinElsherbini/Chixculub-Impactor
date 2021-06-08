import DeviceInterface
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QObject, pyqtSignal, QThread, QMutex
from time import sleep
import detectUsb

mutex = QMutex()

class updateVC(QObject):

    RcvdSignal = pyqtSignal(dict, bool)


    def __init__(self, VID_PID):
        super().__init__()
        self.msgRcvd = {}
        self.VID_PID = VID_PID

    def processMsg(self):

        while(detectUsb.initDevice.devices[self.VID_PID]["Device interface"].isVisible()):
            try:
                mutex.lock()
                self.msgRcvd.update({"Voltage": detectUsb.initDevice.devices[self.VID_PID]['Resource'].send("FETCh:VOLT?")})
                self.msgRcvd.update({"Current": detectUsb.initDevice.devices[self.VID_PID]['Resource'].send("FETCh:CURR?")})
                self.RcvdSignal.emit(self.msgRcvd,False)
                mutex.unlock()

            except Exception as e:
                mutex.unlock()
                self.RcvdSignal.emit({},  True)

            sleep(0.5)

class devInterface(QtWidgets.QWidget):

    def __init__(self,VID_PID, comSignal, cmdSignal):
        super().__init__()
        self.VID_PID = VID_PID
        self.comSignal = comSignal
        self.cmdSignal = cmdSignal
        self.Short = False
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
        #self.updatePages()
        self.window.modePageStack.setCurrentIndex(0)
        self.communicationThread()

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
        self.window.ShortBtn.clicked.connect(self.ShortBtn)
        self.connectCRbtns()
        self.connectCCbtns()
        self.connectCVbtns()

    def ShortBtn(self):
        if self.Short:
            self.comSignal.emit("LOAD:SHOR OFF", self.VID_PID, None,None)
            self.window.ShortBtn.setStyleSheet("""
                QPushButton {
                    color:black;
                    background:transparent;
                    border-radius:15px;
                    border: 3px solid transparent;
                    border-color:#78e4ff;
                    padding:18px;
                }
                QPushButton:hover {
                    border-color:rgb(0, 255, 128);
                    color: rgb(0, 255, 128);
                }

                """)
            self.Short = False
        else:
            self.comSignal.emit("LOAD:SHOR ON", self.VID_PID, None,None)
            self.window.ShortBtn.setStyleSheet("""
                QPushButton {
                    color:black;
                    background:transparent;
                    border-radius:15px;
                    border: 3px solid transparent;
                    border-color:red;
                    padding:18px;
                }
                QPushButton:hover {
                    border-color:rgb(0, 255, 128);
                    color: rgb(0, 255, 128);
                }
                """)
            self.Short = True

    def connectCRbtns(self):
        cbDict = {"High":"High", "Medium" : "M" , "Low" : "0"}

        self.window.CR_L1.returnPressed.connect(
            lambda: self.cmdSignal.emit("RES:STAT:L1 {}".format(self.window.CR_L1.text()), "RESistance:STATic:L1?",
                                        self.VID_PID, None, self.window.CR_L1.setText))
        self.window.CR_L2.returnPressed.connect(
            lambda: self.cmdSignal.emit("RES:STAT:L2 {}".format(self.window.CR_L2.text()), "RESistance:STATic:L2?",
                                        self.VID_PID, None, self.window.CR_L2.setText))

        self.window.CR_SR1.returnPressed.connect(
            lambda: self.cmdSignal.emit("RES:STAT:RISE {}".format(self.window.CR_SR1.text()), "RES:STAT:RISE?",
                                        self.VID_PID, None, self.window.CR_SR1.setText))
        self.window.CR_SR2.returnPressed.connect(
            lambda: self.cmdSignal.emit("RES:STAT:FALL {}".format(self.window.CR_SR2.text()), "RESistance:STATic:FALL?",
                                        self.VID_PID, None, self.window.CR_SR2.setText))

        self.window.CR_IRANGE.currentIndexChanged.connect(
            lambda: self.cmdSignal.emit("RES:STAT:IRNG {}".format(cbDict[self.window.CR_IRANGE.currentText()]), "RES:STAT:IRNG?",
                                        self.VID_PID, None, self.window.CR_IRANGE.setCurrentText))

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


        for child in list(self.window.CV.findChildren(QtWidgets.QLineEdit)):

            child.setAlignment(QtCore.Qt.AlignCenter)
            child.setAlignment(QtCore.Qt.AlignCenter)

        for child in list(self.window.CV.findChildren(QtWidgets.QComboBox)):

            child.setEditable(True)
            lineEdit = child.lineEdit()
            lineEdit.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit.setReadOnly(True)

    def changePage(self):

        if self.sender() == self.window.CR_BTN:
            if not self.window.modePageStack.currentIndex() == 0:
                self.window.modePageStack.setCurrentIndex(0)
                self.cmdSignal.emit("MODE CRM","MODE?", self.VID_PID, None, self.window.CR_RANGE_LABEL.setText)

        elif self.sender() == self.window.CCD_BTN:
            if not self.window.modePageStack.currentIndex() == 1:
                self.window.modePageStack.setCurrentIndex(1)
                self.cmdSignal.emit("MODE CCDM", "MODE?", self.VID_PID, None, self.window.CCD_RANGE_LABEL.setText)

        elif self.sender() == self.window.CC_BTN:
            if not self.window.modePageStack.currentIndex() == 2:
                self.window.modePageStack.setCurrentIndex(2)
                self.cmdSignal.emit("MODE CCM","MODE?", self.VID_PID, None, self.window.CC_RANGE_LABEL.setText)

        elif self.sender() == self.window.CV_BTN:
            if not self.window.modePageStack.currentIndex() == 3:
                self.window.modePageStack.setCurrentIndex(3)
                self.cmdSignal.emit("MODE CVM", "MODE?", self.VID_PID, None, self.window.CV_RANGE_LABEL.setText)

    def updatePages(self):
        self.updatCRPage()
        self.updateCCpage()
        self.updateCCDpage()
        self.updateCVpage()

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

    def updateCCDpage(self):
        self.comSignal.emit("CURR:DYN:L1?", self.VID_PID,  None,self.window.CCD_L1.setText)
        self.comSignal.emit("CURR:DYN:L2?", self.VID_PID, None,self.window.CCD_L2.setText)
        self.comSignal.emit("CURR:DYN:T1?", self.VID_PID, None, self.window.CCD_T1.setText)
        self.comSignal.emit("CURR:DYN:T2?", self.VID_PID, None, self.window.CCD_T2.setText)
        self.comSignal.emit("CURR:DYN:RISE?", self.VID_PID, None,self.window.CCD_SR1.setText)
        self.comSignal.emit("CURR:DYN:FALL?", self.VID_PID, None,self.window.CCD_SR2.setText)
        self.comSignal.emit("CURR:DYN:VRNG?", self.VID_PID, None,self.window.CCD_VRANGE.setCurrentText)
        self.comSignal.emit("*IDN?", self.VID_PID, None,self.window.CCD_DEVNAME_LABEL.setText)
        self.comSignal.emit("FETCh:VOLTage?", self.VID_PID, None,self.window.CCD_VOLTAGE_LCD.display)
        self.comSignal.emit("FETCh:CURRent?", self.VID_PID, None, self.window.CCD_CURRENT_LCD.display)

    def updateCVpage(self):
        self.comSignal.emit("VOLT:STAT:L1?", self.VID_PID, None, self.window.CV_L1.setText)
        self.comSignal.emit("VOLT:STAT:L2?", self.VID_PID, None, self.window.CV_L2.setText)
        self.comSignal.emit("VOLT:STAT:IRNG?", self.VID_PID, None, self.window.CV_IRANGE.setCurrentText)
        self.comSignal.emit("VOLT:STAT:RES?", self.VID_PID, None, self.window.CV_RESPONSE.setCurrentText)
        self.comSignal.emit("VOLT:STAT:ILIM?", self.VID_PID, None, self.window.CV_ILIMIT.setText)
        self.comSignal.emit("*IDN?", self.VID_PID, None, self.window.CV_DEVNAME_LABEL.setText)
        self.comSignal.emit("FETCh:VOLTage?", self.VID_PID, None, self.window.CV_VOLTAGE_LCD.display)
        self.comSignal.emit("FETCh:CURRent?", self.VID_PID, None, self.window.CV_CURRENT_LCD.display)

    def communicationThread(self):
        self.thread = QThread()
        self.updateVC = updateVC(self.VID_PID)
        self.updateVC.moveToThread(self.thread)
        self.updateVC.RcvdSignal.connect(self.updateLCD)
        self.thread.started.connect(self.updateVC.processMsg)
        self.thread.start()

    def updateLCD(self,msg, error):
        if error == True:
            pass
        elif error == False:
            children = list(self.window.modePageStack.currentWidget().findChildren(QtWidgets.QLCDNumber))
            for child in children:
                if "VOLTAGE" in child.objectName():
                    child.display(msg["Voltage"])

                elif "CURRENT" in child.objectName():
                    child.display(msg["Current"])


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

        children = list(self.window.CV.findChildren(QtWidgets.QLabel)) + list(self.window.CV.findChildren(QtWidgets.QLCDNumber))

        for child in children:
            if child.inherits("QLabel") and (child.objectName() == "CV_VLABEL" or child.objectName() == "CV_CLABEL"):
                self.setShadow(child)
            elif child.inherits("QLCDNumber"):
                self.setShadow(child)

        children = list(self.window.CCD.findChildren(QtWidgets.QLabel)) + list(self.window.CCD.findChildren(QtWidgets.QLCDNumber))

        for child in children:
            if child.inherits("QLabel") and (child.objectName() == "CCD_VLABEL" or child.objectName() == "CCD_CLABEL"):
                self.setShadow(child)
            elif child.inherits("QLCDNumber"):
                self.setShadow(child)

    def connectCCbtns(self):
        cbDict = {"High":"High", "Medium" : "M" , "Low" : "0"}

        self.window.CC_L1.returnPressed.connect(
            lambda: self.cmdSignal.emit("CURR:STAT:L1 {}".format(self.window.CR_L1.text()), "CURR:STAT:L1?",
                                        self.VID_PID, None, self.window.CC_L1.setText))
        self.window.CC_L2.returnPressed.connect(
            lambda: self.cmdSignal.emit("CURR:STAT:L2 {}".format(self.window.CC_L2.text()), "CURR:STAT:L2?",
                                        self.VID_PID, None, self.window.CC_L2.setText))

        self.window.CC_SR1.returnPressed.connect(
            lambda: self.cmdSignal.emit("CURR:STAT:RISE {}".format(self.window.CC_SR1.text()), "CURR:STAT:RISE?",
                                        self.VID_PID, None, self.window.CR_SR1.setText))
        self.window.CC_SR2.returnPressed.connect(
            lambda: self.cmdSignal.emit("CURR:STAT:FALL {}".format(self.window.CC_SR2.text()), "CURRent:STATic:FALL?",
                                        self.VID_PID, None, self.window.CC_SR2.setText))

        self.window.CC_VRANGE.currentIndexChanged.connect(
            lambda: self.cmdSignal.emit("CURR:STAT:VRNG {}".format(cbDict[self.window.CC_VRANGE.currentText()]), "CURR:STAT:VRNG?",
                                        self.VID_PID, None, self.window.CC_VRANGE.setCurrentText))

    def connectCVbtns(self):
        cbDict = {"High": "High", "Medium": "M", "Low": "0"}

        self.window.CV_L1.returnPressed.connect(
            lambda: self.cmdSignal.emit("VOLT:STAT:L1 {}".format(self.window.CV_L1.text()), "VOLT:STAT:L1?",
                                        self.VID_PID, None, self.window.CV_L1.setText))
        self.window.CV_L2.returnPressed.connect(
            lambda: self.cmdSignal.emit("VOLT:STAT:L2 {}".format(self.window.CV_L2.text()), "VOLT:STAT:L2?",
                                        self.VID_PID, None, self.window.CV_L2.setText))

        self.window.CV_ILIMIT.returnPressed.connect(
            lambda: self.cmdSignal.emit("VOLT:STAT:ILIM {}".format(self.window.CV_ILIMIT.text()), "VOLT:STAT:ILIM?",
                                        self.VID_PID, None, self.window.CV_ILIMIT.setText))

        self.window.CV_RESPONSE.currentIndexChanged.connect(
            lambda: self.cmdSignal.emit("VOLT:STAT:RES {}".format(self.window.CV_RESPONSE.currentText()),
                                        "VOLT:STAT:RES?",
                                        self.VID_PID, None, self.window.CV_RESPONSE.setCurrentText))

        self.window.CV_IRANGE.currentIndexChanged.connect(
            lambda: self.cmdSignal.emit("VOLT:STAT:IRNG {}".format(cbDict[self.window.CV_IRANGE.currentText()]),
                                        "VOLT:STAT:IRNG?",
                                        self.VID_PID, None, self.window.CV_IRANGE.setCurrentText()))