from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint
import deleteDialog
import uiFunctions
import Dialog
import dialogAB


class removeDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.uiDialog = deleteDialog.Ui_Dialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(self)
        self.dialogTitleBar()

    def eventFilter(self, obj, event):

        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        return False

    def dialogTitleBar(self):
        self.uiDialog.closeBtn_3.clicked.connect(lambda: self.close())
        self.uiDialog.minBtn_3.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        self.uiDialog.frame_2.setGraphicsEffect(shadow)
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(25)
        self.uiDialog.DeleteBtn.setGraphicsEffect(shadow1)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(25)
        self.uiDialog.CancelBtn.setGraphicsEffect(shadow2)


class deviceFrame(QtWidgets.QFrame):

    def __init__(self, *args):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.setFont(font)
        self.setToolTipDuration(2000)
        self.setStyleSheet('''    
                           QFrame{
		color: black;
		border: 1px solid black;
		border-color:black;
		background:transparent;
}

QFrame:hover{

		background:transparent;
		border-color: red;
		border-radius:20px;
}
                                       ''')
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName(args[0])
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(12, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.deviceIcon = QtWidgets.QLabel(self)
        self.deviceIcon.setMinimumSize(QtCore.QSize(50, 50))
        self.deviceIcon.setMaximumSize(QtCore.QSize(50, 50))
        self.deviceIcon.setStyleSheet("background-color: rgba(0,0,0,0%);"
                                      "border: transparent;")
        self.deviceIcon.setText("")
        self.deviceIcon.setPixmap(QtGui.QPixmap("resources/{}".format(args[1])))
        self.deviceIcon.setScaledContents(True)
        self.deviceIcon.setObjectName("deviceIcon")
        self.gridLayout.addWidget(self.deviceIcon, 0, 0, 1, 1)
        self.connectBtn = QtWidgets.QPushButton(self)
        self.connectBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.connectBtn.setMaximumSize(QtCore.QSize(120, 30))
        self.connectBtn.setAutoFillBackground(False)
        self.connectBtn.setStyleSheet('''QPushButton {
  font: 75 10pt "Microsoft YaHei UI";
 color:black;
 background:transparent;
 border-radius:15px;
 border: 3px solid transparent;
 
	border-color:#78e4ff;
 padding:18px;
}

QPushButton:hover {
 border-color:rgb(0, 255, 128);
}
''')
        self.connectBtn.setDefault(False)
        self.connectBtn.setFlat(False)
        self.connectBtn.setObjectName("connectBtn")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        self.setGraphicsEffect(shadow)
        self.gridLayout.addWidget(self.connectBtn, 0, 5, 1, 1)
        self.deviceName = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.deviceName.setFont(font)
        self.deviceName.setStyleSheet(''' 

QLabel{
 color:black;
border: transparent;
background-color: rgba(0,0,0,0%);

 }''')
        self.deviceName.setObjectName("deviceName")
        self.deviceName.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{}</span></p></body></html>".format(
                                               args[0])))
        self.gridLayout.addWidget(self.deviceName, 0, 1, 1, 1)
        self.deleteBtn = QtWidgets.QPushButton(self)
        self.deleteBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.deleteBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.deleteBtn.setStyleSheet("QPushButton:hover{\n"
                                     "\n"
                                     "    background-color: rgb(91,91,91);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "    background:transparent;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "\n"
                                     "    	background-color: transparent;\n;"
                                     "border:transparent;"
                                     "}\n"
                                     "")
        self.deleteBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteBtn.setIcon(icon5)
        self.deleteBtn.setIconSize(QtCore.QSize(30, 30))
        self.deleteBtn.setFlat(True)
        self.deleteBtn.setObjectName("deleteBtn")
        self.gridLayout.addWidget(self.deleteBtn, 0, 6, 1, 1)
        self.connectBtn.setText(_translate("MainWindow", "Connect"))
        self.setToolTip(_translate("MainWindow",
                                   "<html><head/><body><p><span style=\" font-weight:600;\">Device:</span> {}</p><p><span style=\" font-weight:600;\">Connection Type:</span> {}</p></body></html>".format(
                                       args[2], args[3])))
        self.deleteBtn.setToolTip(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Delete</span></p></body></html>"))
        self.connectBtn.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Connect</span></p></body></html>"))

        self.deleteBtn.clicked.connect(self.deleteFrame)

    def deleteFrame(self):
        self.delDialog = removeDialog()
        self.delDialog.uiDialog.DeleteBtn.clicked.connect(self.removeFrame)
        self.delDialog.uiDialog.CancelBtn.clicked.connect(self.delDialog.close)
        self.delDialog.exec_()

    def removeFrame(self):
        self.deleteLater()
        self.delDialog.close()

    def closeDialog(self):
        self.delDialog.close()


class addDeviceDialog(QtWidgets.QDialog):
    # creates an instance of a dialog when the ADD device button is pressed

    def __init__(self, parent=None):

        super().__init__(parent)
        self.uiDialog = Dialog.Ui_Dialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(
            self)  # install an event filter to know when an event occurs on title bar
        self.dialogTitleBar()  # make window frameless
        self.setShadow(self.uiDialog.frame_7)
        self.setShadow(self.uiDialog.ConfirmBtn)
        self.setShadow(self.uiDialog.ComboBox2)
        self.setShadow(self.uiDialog.statusLabel)
        self.ConnectBtns()
        self.devices = {}
        self.device = {}

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(self.close_Event)
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def close_Event(self):
        self.step = 1
        self.close()

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
        return False

    def changeCBcontent(self, QComboBox, newList):

        QComboBox.clear()
        QComboBox.addItems(newList)

    def ConnectBtns(self):
        self.step = 1
        self.uiDialog.ConfirmBtn.clicked.connect(self.addDeviceSteps)
        self.uiDialog.ComboBox1.currentIndexChanged.connect(self.addDeviceSteps)
        self.uiDialog.ComboBox2.currentIndexChanged.connect(self.addDeviceSteps)

    def addDeviceSteps(self):

        if self.step == 1:
            self.step1()
        elif self.step == 2:
            self.step2()

    def step1(self):
        if self.sender() == self.uiDialog.ComboBox1:
            if self.uiDialog.ComboBox1.currentText() != "Select Device":
                self.uiDialog.statusLabel.clear()

        elif self.sender() == self.uiDialog.ComboBox2:
            if self.uiDialog.ComboBox2.currentText() != "Connection Type":
                self.uiDialog.statusLabel.clear()

        elif self.sender() == self.uiDialog.ConfirmBtn:
            if self.uiDialog.ComboBox1.currentText() != "Select Device" and self.uiDialog.ComboBox2.currentText() != "Connection Type":

                if self.uiDialog.centerStackedWidget.count() == 1:
                    self.step = 2
                    self.device = {
                        "Device Type": self.uiDialog.ComboBox1.currentText(),
                        "Connection Type": self.uiDialog.ComboBox2.currentText(),
                    }
                    self.page = dialogAB.dialogAbstractPage()
                    self.page.populateComboBox("Frame1", ["Enter Device Name (Optional)"])
                    self.page.populateComboBox("Frame2",
                                               ["Select Baud Rate", "9600", "14400", "19200", "38400", "57600",
                                                "115200", "128000", "256000"])
                    self.page.populateComboBox("Frame3", ["Select COM Port", "COM1"])
                    self.uiDialog.centerStackedWidget.addWidget(self.page)
                    self.page.CB2.currentIndexChanged.connect(self.addDeviceSteps)
                    self.page.CB3.currentIndexChanged.connect(self.addDeviceSteps)
                    self.page.CB.clicked.connect(self.addDeviceSteps)
                    self.page.PB.clicked.connect(self.addDeviceSteps)
                    self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                    self.addDeviceSteps()
                else:
                    self.step = 2
                    self.device = {
                        "Device Type": self.uiDialog.ComboBox1.currentText(),
                        "Connection Type": self.uiDialog.ComboBox2.currentText(),
                    }

                    self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                    self.addDeviceSteps()
            else:
                if self.uiDialog.ComboBox1.currentText() == "Select Device":
                    self.uiDialog.statusLabel.setText("Please select a Device")

                else:
                    self.uiDialog.statusLabel.setText("Please select a Connection Type")

    def step2(self):

        if self.sender() == self.page.CB2:
            if self.page.CB2.currentIndex() != 0 and self.page.CB3.currentIndex() != 0:
                self.page.statusLabel.clear()

        elif self.sender() == self.page.CB3:

            if self.page.CB3.currentText() != 0 and self.page.CB2.currentIndex() != 0:
                self.page.statusLabel.clear()

        elif self.sender() == self.page.CB:

            if self.page.CB2.currentIndex() != 0 and self.page.CB3.currentIndex() != 0:

                if self.page.CB1.currentText() != "Enter Device Name (Optional)":

                    self.device["DEVICE NAME"] = self.page.CB1.currentText()

                else:
                    self.device["DEVICE NAME"] = ""
                self.device["Baud Rate"] = self.page.CB2.currentText()
                self.device["COM PORT"] = self.page.CB3.currentText()

                print(self.device["DEVICE NAME"])
                print(self.device.keys())
                self.close()
            else:
                if self.page.CB2.currentText() == "Select Baud Rate":
                    self.page.statusLabel.clear()
                    self.page.statusLabel.setText("Please Select a Baud Rate")
                else:
                    self.page.statusLabel.clear()
                    self.page.statusLabel.setText("Please Select a COM PORT")

        elif self.sender() == self.page.PB:
            self.step = 1
            self.uiDialog.centerStackedWidget.setCurrentIndex(0)
