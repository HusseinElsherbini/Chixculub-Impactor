from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QRegExp
from PyQt5.QtGui import QRegExpValidator
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
        self.uiDialog.westTopFrame.installEventFilter(self)  # install an event filter to know when an event occurs on title bar
        self.uiDialog.DeviceNameLE.installEventFilter(self)
        self.dialogTitleBar()  # make window frameless
        self.setShadow(self.uiDialog.DeviceTypeCB)
        self.setShadow(self.uiDialog.ConfirmBtn)
        self.setShadow(self.uiDialog.ConTypeCB)
        self.setShadow(self.uiDialog.statusLabel)
        self.setShadow(self.uiDialog.DeviceNameLE)
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
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.MouseButtonPress:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(False)
        if obj == self.uiDialog.DeviceNameLE and event.type() == QEvent.FocusOut:
            self.uiDialog.DeviceNameLE.graphicsEffect().setEnabled(True)
        return False

    def changeCBcontent(self, QComboBox, newList):

        QComboBox.clear()
        QComboBox.addItems(newList)

    def ConnectBtns(self):
        self.step = 1
        self.uiDialog.ConfirmBtn.clicked.connect(self.addDeviceSteps)
        self.uiDialog.DeviceTypeCB.currentIndexChanged.connect(self.addDeviceSteps)
        self.uiDialog.ConTypeCB.currentIndexChanged.connect(self.addDeviceSteps)

    def addDeviceSteps(self):

        if self.step == 1:
            self.step1()
        elif self.step == 2:
            if self.device["Connection Type"] == "RS232":
                self.step2RS232()
            elif self.device["Connection Type"] == "LAN":
                self.step2LAN()

        elif self.step == 3:
            if self.device["Connection Type"] == "RS232":
                self.step3RS232()
            elif self.device["Connection Type"] == "LAN":
                self.step3LAN()

    def addPage(self, page, CB1, CB2, CB3):

        if CB1:

            page.populateComboBox("Frame1", CB1)
            page.CB1.currentIndexChanged.connect(self.addDeviceSteps)

        if CB2:

            page.populateComboBox("Frame2", CB2)
            page.CB2.currentIndexChanged.connect(self.addDeviceSteps)

        if CB3:

            page.populateComboBox("Frame3", CB3)
            page.CB3.currentIndexChanged.connect(self.addDeviceSteps)

        self.uiDialog.centerStackedWidget.addWidget(page)
        page.CB.clicked.connect(self.addDeviceSteps)
        page.PB.clicked.connect(self.addDeviceSteps)

    def step1(self):
        if self.sender() == self.uiDialog.DeviceTypeCB:
            if self.uiDialog.DeviceTypeCB.currentText() != "Select Device":
                self.uiDialog.statusLabel.clear()

        elif self.sender() == self.uiDialog.ConTypeCB:
            if self.uiDialog.ConTypeCB.currentText() != "Connection Type":
                self.uiDialog.statusLabel.clear()

        elif self.sender() == self.uiDialog.ConfirmBtn:
            if self.uiDialog.DeviceTypeCB.currentIndex() != 0 and self.uiDialog.ConTypeCB.currentIndex() != 0:

                if self.uiDialog.centerStackedWidget.count() == 1:
                    if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":

                        self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()

                    else:
                        self.device["DEVICE NAME"] = ""

                    if self.uiDialog.ConTypeCB.currentText() == "RS232":
                        self.step = 2
                        self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                        self.device["Connection Type"] = self.uiDialog.ConTypeCB.currentText()
                        self.pageRS232_1 = dialogAB.dialogAbstractPage("CB", "", "CB", "", "CB", "")
                        self.addPage(self.pageRS232_1,
                                 ["Select Baud Rate", "9600", "14400", "19200", "38400", "57600", "115200", "128000",
                                  "256000"], ["Select COM Port", "COM1"],
                                 ["Select Data Size (bits)", "8", "7", "6", "5"])
                        self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                        self.addDeviceSteps()

                    elif self.uiDialog.ConTypeCB.currentText() == "LAN":
                        self.step = 2
                        self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                        self.device["Connection Type"] = self.uiDialog.ConTypeCB.currentText()
                        self.pageLAN_1 = dialogAB.dialogAbstractPage("LE", "ENTER IP ADDRESS (e.g 255.255.255.255)", "CB", "", "CB", "")
                        self.addPage(self.pageLAN_1,[],["Select Socket Family", "AF_INET", "AF_INET6", "AF_UNIX"], ["Select Socket Type", "Stream", "Datagram"])
                        self.ipFormat = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
                        ipRegex = QRegExp("^" + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "$")
                        ipValidCheck = QRegExpValidator(ipRegex, self)
                        self.pageLAN_1.LE1.setValidator(ipValidCheck)
                        self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                        self.addDeviceSteps()

                else:
                    print(self.uiDialog.ConTypeCB.currentText())
                    if self.uiDialog.ConTypeCB.currentText() == "RS232":

                        if self.device["Connection Type"] != "RS232":
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.device["Connection Type"] = self.uiDialog.ConTypeCB.currentText()
                            for x in range(1, self.uiDialog.centerStackedWidget.count()):
                                self.uiDialog.centerStackedWidget.removeWidget(self.uiDialog.centerStackedWidget.widget(x))
                            if hasattr(self,'pageRS232_1'):
                                self.uiDialog.centerStackedWidget.addWidget(self.pageRS232_1)
                            else:
                                self.pageRS232_1 = dialogAB.dialogAbstractPage("CB", "", "CB", "", "CB", "")
                                self.addPage(self.pageRS232_1,["Select Baud Rate", "9600", "14400", "19200", "38400", "57600", "115200","128000","256000"], ["Select COM Port", "COM1"],
                                             ["Select Data Size (bits)", "8", "7", "6", "5"])
                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                            self.addDeviceSteps()
                        else:
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                            self.addDeviceSteps()


                    elif self.uiDialog.ConTypeCB.currentText() == "LAN":
                        if self.device["Connection Type"] != "LAN":
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.device["Connection Type"] = self.uiDialog.ConTypeCB.currentText()
                            for x in range(1, self.uiDialog.centerStackedWidget.count()):
                                self.uiDialog.centerStackedWidget.removeWidget(self.uiDialog.centerStackedWidget.widget(x))
                            if hasattr(self, 'pageLAN_1'):
                                print("exists")
                                self.uiDialog.centerStackedWidget.addWidget(self.pageLAN_1)
                            else:
                                self.ipFormat = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
                                ipRegex = QRegExp("^" + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "$")
                                ipValidCheck = QRegExpValidator(ipRegex, self)
                                self.pageLAN_1 = dialogAB.dialogAbstractPage("LE", "ENTER IP ADDRESS", "CB", "", "CB","")
                                self.pageLAN_1.LE1.setValidator(ipValidCheck)
                                self.addPage(self.pageLAN_1, [],
                                             ["Select Socket Family", "AF_INET", "AF_INET6", "AF_UNIX"],
                                             ["Select Socket Type", "Stream", "Datagram"])

                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                            self.addDeviceSteps()

                        else:
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                            self.addDeviceSteps()


            else:
                if self.uiDialog.DeviceTypeCB.currentText() == "Select Device (optional)":
                    self.uiDialog.statusLabel.setText("Please select a Device")

                else:
                    self.uiDialog.statusLabel.setText("Please select a Connection Type")

    def step2RS232(self):

        if self.sender() == self.pageRS232_1.CB1:
            if self.pageRS232_1.CB1.currentIndex() != 0 and self.pageRS232_1.CB2.currentIndex() != 0 and self.pageRS232_1.CB3.currentIndex() != 0:
                self.pageRS232_1.statusLabel.clear()

        elif self.sender() == self.pageRS232_1.CB2:

            if self.pageRS232_1.CB1.currentIndex() != 0 and self.pageRS232_1.CB2.currentIndex() != 0 and self.pageRS232_1.CB3.currentIndex() != 0:
                self.pageRS232_1.statusLabel.clear()

        elif self.sender() == self.pageRS232_1.CB3:

            if self.pageRS232_1.CB1.currentIndex() != 0 and self.pageRS232_1.CB2.currentIndex() != 0 and self.pageRS232_1.CB3.currentIndex() != 0:
                self.pageRS232_1.statusLabel.clear()

        elif self.sender() == self.pageRS232_1.CB:

            if self.pageRS232_1.CB1.currentIndex() != 0 and self.pageRS232_1.CB2.currentIndex() != 0 and self.pageRS232_1.CB3.currentIndex() != 0:
                if self.uiDialog.centerStackedWidget.count() == 2:
                    self.device["Baud Rate"] = self.pageRS232_1.CB1.currentText()
                    self.device["COM PORT"] = self.pageRS232_1.CB2.currentText()
                    self.device["Data size"] = self.pageRS232_1.CB3.currentText()
                    print(self.device.keys())
                    self.step = 3
                    self.pageRS232_2 = dialogAB.dialogAbstractPage("LE", "Enter Timeout (optional, Default:None)", "CB", "","CB", "")
                    self.addPage(self.pageRS232_2, [],
                                 ["Parity (Optional, Default:None)", "ODD", "EVEN", "MARK", "SPACE"],
                                 ["Stop Bits (Optional, Default:None)", "1", "1.5", "2"])
                    self.pageRS232_2.LE1.installEventFilter(self)
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)
                    self.addDeviceSteps()
                else:
                    self.step = 3
                    self.device["Baud Rate"] = self.pageRS232_1.CB1.currentText()
                    self.device["COM PORT"] = self.pageRS232_1.CB2.currentText()
                    self.device["Data size"] = self.pageRS232_1.CB3.currentText()
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)
                    self.addDeviceSteps()
            else:
                self.pageRS232_1.statusLabel.setText("Please fill out all mandatory fields")

        elif self.sender() == self.pageRS232_1.PB:
            self.step = 1
            self.uiDialog.centerStackedWidget.setCurrentIndex(0)

    def step2LAN(self):

        if self.sender() == self.pageLAN_1.LE1:
            if self.pageLAN_1.LE1.text() != "" and self.pageLAN_1.CB2.currentIndex() != 0 and self.pageLAN_1.CB3.currentIndex() != 0:
                self.page.statusLabel.clear()

        elif self.sender() == self.pageLAN_1.CB2:

            if self.pageLAN_1.LE1.text() != "" and self.pageLAN_1.CB2.currentIndex() != 0 and self.pageLAN_1.CB3.currentIndex() != 0:
                self.page.statusLabel.clear()

        elif self.sender() == self.pageLAN_1.CB3:

            if self.pageLAN_1.LE1.text() != "" and self.pageLAN_1.CB2.currentIndex() != 0 and self.pageLAN_1.CB3.currentIndex() != 0:
                self.pageLAN_1.statusLabel.clear()

        elif self.sender() == self.pageLAN_1.CB:

            if self.pageLAN_1.LE1.text() != "" and self.pageLAN_1.CB2.currentIndex() != 0 and self.pageLAN_1.CB3.currentIndex() != 0:
                if self.uiDialog.centerStackedWidget.count() == 2:
                    self.step = 3
                    self.device["IP ADDRESS"] = self.pageLAN_1.LE1.text()
                    self.device["Address Family"] = self.pageLAN_1.CB2.currentText()
                    self.device["Socket Type"] = self.pageLAN_1.CB3.currentText()
                    print(self.device.keys())
                    self.pageLAN_2 = dialogAB.dialogAbstractPage("LE", "Enter Timeout (optional, Default:None)", "LE", "Enter Port Number","", "")
                    self.addPage(self.pageLAN_2, [],[],[])
                    self.pageLAN_2.LE1.installEventFilter(self)
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)
                    self.addDeviceSteps()
                else:
                    self.step = 3
                    self.device["IP ADDRESS"] = self.pageLAN_1.LE1.text()
                    self.device["Address Family"] = self.page.CB2.currentText()
                    self.device["Socket Type"] = self.page.CB3.currentText()
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)
                    self.addDeviceSteps()
            else:
                self.pageLAN_1.statusLabel.setText("Please fill out all mandatory fields")

        elif self.sender() == self.pageLAN_1.PB:
            self.step = 1
            self.uiDialog.centerStackedWidget.setCurrentIndex(0)

    def step3RS232(self):

        if self.sender() == self.pageRS232_2.CB:
            if self.pageRS232_2.LE1.text() != "Enter Timeout (optional, Default:None)":
                self.device["Timeout"] = self.pageRS232_2.LE1.text()
            else:
                self.device["Timeout"] = ""

            if self.pageRS232_2.CB2.currentIndex() != 0:
                self.device["Parity"] = self.pageRS232_2.CB2.currentText()
            else:
                self.device["Parity"] = ""

            if self.pageRS232_2.CB3.currentIndex() != 0:
                self.device["Stop Bits"] = self.pageRS232_2.CB3.currentText()
            else:
                self.device["Stop Bits"] = ""

            for x in self.device.keys():
                print("%s : %s " % (x, self.device[x]))
            self.close()

        elif self.sender() == self.pageRS232_2.PB:
            self.step = 2
            self.uiDialog.centerStackedWidget.setCurrentIndex(1)

    #def step3LAN(self):