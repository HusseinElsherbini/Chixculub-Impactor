from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QRegExp
from PyQt5.QtGui import QRegExpValidator
import deleteDialog
import Dialog
import dialogAB
import serial.tools.list_ports as portsList
import threading
import time
from PyQt5.QtCore import pyqtSignal, QObject



########################################################################################################################
#  class: removeDialog                                                                                                 #
#  purpose: a subclass that inherits from QDIALOG with additional functionality pertaining to the delete device dialog #
#  returns: an instance of the remove dialog class                                                                     #
########################################################################################################################
class removeDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.uiDialog = deleteDialog.Ui_Dialog()  # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(self)
        self.dialogTitleBar()

    #######################################################################################################################################################################################
    #  Function: eventFilter                                                                                                                                                              #
    #  Purpose: triggered when the event filter installed on the Top Frame detects an event, it checks if the event is a mouseBtn press or mouseMove in order to move the whole dialog    #
    #######################################################################################################################################################################################
    def eventFilter(self, obj, event):

        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()
        return False

    #######################################################################################################################################################################################
    #  Function: dialogTitleBar                                                                                                                                                           #
    #  Purpose: removes native title bar and connects close and minimize button click events to self.close() and showMinimized() functions which close and minimized dialog respectively  #
    #           adds shadow effect to the delete, cancel and line edit                                                                                                                    #
    #######################################################################################################################################################################################
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

    #######################################################################################################################################################################################
    #  Class: deviceFrame                                                                                                                                                                 #
    #  Purpose: a subclass that inherits from the QFrame class, with added functionality pertaining to the frame containing any added new device on the home page                         #
    #  Returns: an instance of the deviceFrame class                                                                                                                                      #
    #######################################################################################################################################################################################


class deviceFrame(QtWidgets.QFrame):

    def __init__(self, *args):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.VID_PID = args[5]
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
QToolTip{
background-color:#ffecd9;
color:black;
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
 color: rgb(0, 255, 128);
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
        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap("resources/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteBtn.setIcon(self.icon5)
        self.deleteBtn.installEventFilter(self)
        self.deleteBtn.setIconSize(QtCore.QSize(30, 30))
        self.deleteBtn.setFlat(True)
        self.deleteBtn.setObjectName("deleteBtn")
        self.gridLayout.addWidget(self.deleteBtn, 0, 7, 1, 1)
        self.editBtn = QtWidgets.QPushButton(self)
        self.editBtn.setStyleSheet("QPushButton:hover{\n"
                                     "\n"
                                     "    background-color: rgb(91,91,91);\n"
                                     "ur"
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
        self.editBtn.setText("")
        self.icon6 = QtGui.QIcon()
        self.icon6.addPixmap(QtGui.QPixmap("resources/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editBtn.setIcon(self.icon6)
        self.editBtn.installEventFilter(self)
        self.editBtn.setIconSize(QtCore.QSize(30, 30))
        self.editBtn.setToolTip("Modify Device")
        self.editBtn.setFlat(True)
        self.editBtn.setObjectName("editBtn")
        self.gridLayout.addWidget(self.editBtn, 0, 6, 1, 1)

        self.connectBtn.setText(_translate("MainWindow", "Connect"))
        if args[3] == "ETHERNET":
            self.setToolTip(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-weight:600;\">Device:</span> {}</p><p><span style=\" font-weight:600;\">Connection Type:</span> {}</p><p><span style=\" font-weight:600;\">IP ADDRESS:</span> {}</p></body></html>".format(
                                           args[2], args[3], args[4])))
        else:
            self.setToolTip(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-weight:600;\">Device:</span> {}</p><p><span style=\" font-weight:600;\">Connection Type:</span> {}</p></body></html>".format(args[0],
                                           args[3].upper())))
        self.deleteBtn.setToolTip(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Delete</span></p></body></html>"))
        self.connectBtn.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Connect</span></p></body></html>"))

        self.deleteBtn.clicked.connect(self.deleteFrame)

    ###########################################################################################################################################################################################
    #  Function: deleteFrame                                                                                                                                                                  #
    #  Purpose: creates an instance of the removeDialog class and executes it, connects the delete and cancel button clicked events to functions removeFrame and delDialog.close respectively #
    ###########################################################################################################################################################################################

    def deleteFrame(self):
        self.delDialog = removeDialog()
        self.delDialog.uiDialog.DeleteBtn.clicked.connect(self.removeFrame)
        self.delDialog.uiDialog.CancelBtn.clicked.connect(self.delDialog.close)
        self.delDialog.exec_()

    def eventFilter(self, obj, event):

        if obj == self.editBtn and event.type() == QEvent.HoverEnter:

            self.icon6.addPixmap(QtGui.QPixmap("resources/edit (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.editBtn.setIcon(self.icon6)
            return True

        if obj == self.editBtn and event.type() == QEvent.HoverLeave:

            self.icon6.addPixmap(QtGui.QPixmap("resources/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.editBtn.setIcon(self.icon6)
            return True

        if obj == self.deleteBtn and event.type() == QEvent.HoverEnter:

            self.icon5.addPixmap(QtGui.QPixmap("resources/delete (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.deleteBtn.setIcon(self.icon5)
            return True

        if obj == self.deleteBtn and event.type() == QEvent.HoverLeave:

            self.icon5.addPixmap(QtGui.QPixmap("resources/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.deleteBtn.setIcon(self.icon5)
            return True

        return False

    def removeFrame(self):
        self.deleteLater()
        self.delDialog.close()

    def closeDialog(self):
        self.delDialog.close()


class customSignal(QObject):
    comChangedSignal = pyqtSignal()


#######################################################################################################################################################################################
#  Class: addDeviceDialog                                                                                                                                                             #
#  Purpose: a subclass that inherits from the QDialog class, with added functionality pertaining to adding a new device, collects information from user pertaining to said device     #
#  Returns: an instance of the addDeviceDialog class                                                                                                                                  #
#######################################################################################################################################################################################


class addDeviceDialog(QtWidgets.QDialog):

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
        self.ComPorts = [port[0] for port in list(portsList.comports())]
        self.ConnectBtns()
        self.devices = {}
        self.device = {}


    ###############################################################################################################################################################################
    #  Function: dialogTitleBar                                                                                                                                                   #
    #  Purpose: removes native title bar and connects close and minimize button click events to self.close_Event() and showMinimized() functions which close and minimized dialog #
    #  respectively adds shadow effect to the delete, cancel and line edit                                                                                                        #
    ###############################################################################################################################################################################

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(self.close_Event)
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def updateComPorts(self, interval):
        self.customSignal = customSignal()
        self.customSignal.comChangedSignal.connect(self.addDeviceSteps)
        ComPorts = self.fetchComPorts()[1:]
        while True:
            x = self.fetchComPorts()[1:]

            if ComPorts != x:

                #print("com ports: {}".format(ComPorts))
                #print("x: {}".format(x))
                self.customSignal.comChangedSignal.emit()
                ComPorts = x
            elif self.uiDialog.centerStackedWidget.currentWidget() != self.pageRS232_1:
                break

            time.sleep(interval)


    def startThread(self, function, arguments):

        self.threadx = threading.Thread(target=function, args=arguments)
        self.threadx.daemon = True
        self.threadx.start()

    def close_Event(self):
        self.step = 1
        self.close()

    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)

    def fetchComPorts(self):

        comPortParam = ["Select COM Port"]
        self.ComPorts = [port[0] for port in list(portsList.comports())]
        for i in self.ComPorts:
            comPortParam.append(i)
        return comPortParam

    ####################################################################################################################################################################
    #  Function: eventFilter                                                                                                                                           #
    #  Purpose: filters for mouse press and mouse move events occurring on artificial title bar in order to move the dialog window,                                    #
    #           also checks for mouse press events and out of focus events occurring on the line edit on the first page of dialog  in order to apply and remove shadow #
    ####################################################################################################################################################################

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

    #######################################################################################
    #  Function: changeCBcontent                                                          #
    #  Purpose: clears a combobox and adds new items that are passed as a list of strings #
    #######################################################################################

    def changeCBcontent(self, QComboBox, newList):

        QComboBox.clear()
        QComboBox.addItems(newList)

    #############################################################################################################################
    #  Function: ConnectBtns                                                                                                    #
    #  Purpose: connects the confirm clicked event, device type and connection type comboboxes's current index changed events   #
    #           to addDeviceSteps function                                                                                      #
    #############################################################################################################################

    def ConnectBtns(self):
        self.step = 1
        self.uiDialog.ConfirmBtn.clicked.connect(self.addDeviceSteps)
        self.uiDialog.DeviceTypeCB.currentIndexChanged.connect(self.addDeviceSteps)
        self.uiDialog.ConTypeCB.currentIndexChanged.connect(self.addDeviceSteps)

    #############################################################################################################################
    #  Function: addDeviceSteps                                                                                                 #
    #  Purpose: there are 3 steps to adding any device, depending on the connection type the user chooses on the first step and #
    #           which step they are currently on, the function reroutes to respective function                                  #
    #############################################################################################################################
    def addDeviceSteps(self):

        if self.step == 1:
            self.step1()
        elif self.step == 2:
            if self.device["Connection Type"] == "RS232":
                self.step2RS232()
            elif self.device["Connection Type"] == "ETHERNET":
                self.step2ETHERNET()

        elif self.step == 3:
            if self.device["Connection Type"] == "RS232":
                self.step3RS232()
            elif self.device["Connection Type"] == "ETHERNET":
                self.step3ETHERNET()

    #############################################################################################################################
    #  Function: addPage                                                                                                        #
    #  Purpose: adds a page to the stacked widget and connects combobox (if non empty list was passed) current index changed    #
    #           events, confirm button event and previous button event to addDeviceSteps function                               #
    #############################################################################################################################

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

        ####################################################################################################################################
        #  Function: step1                                                                                                                 #
        #  Purpose: this function is called when any of the events connected on the  comboBoxes or confirm button on first page occur      #
        #           if the confirm button is clicked, checks are carried out to ensure mandatory fields are filled out properly.           #
        #           it also includes functionality to ensure proper handling of the flow of the application in case the function is called #
        #           when the user has reached the page through the previous button                                                         #
        ####################################################################################################################################

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
                                     ["Select Baud Rate", "9600", "14400", "19200", "38400", "57600", "115200",
                                      "128000", "256000"], self.fetchComPorts(),
                                     ["Select Data Size (bits)", "8", "7", "6", "5"])
                        self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                        self.startThread(self.updateComPorts, (1,))


                    elif self.uiDialog.ConTypeCB.currentText() == "ETHERNET":
                        self.step = 2
                        self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                        self.device["Connection Type"] = self.uiDialog.ConTypeCB.currentText()
                        self.pageETHERNET_1 = dialogAB.dialogAbstractPage("LE", "ENTER IP ADDRESS (e.g 255.255.255.255)",
                                                                     "CB", "", "CB", "")

                        self.addPage(self.pageETHERNET_1, [], ["Select Socket Family", "AF_INET", "AF_INET6", "AF_UNIX"],
                                     ["Select Socket Type", "Stream", "Datagram"])
                        self.ipFormat = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
                        ipRegex = QRegExp(
                            "^" + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "$")
                        ipValidCheck = QRegExpValidator(ipRegex, self)
                        self.pageETHERNET_1.LE1.setValidator(ipValidCheck)
                        self.uiDialog.centerStackedWidget.setCurrentIndex(1)


                else:

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
                                self.uiDialog.centerStackedWidget.widget(x).deleteLater()

                            self.pageRS232_1 = dialogAB.dialogAbstractPage("CB", "", "CB", "", "CB", "")
                            self.addPage(self.pageRS232_1,
                                         ["Select Baud Rate", "9600", "14400", "19200", "38400", "57600", "115200",
                                          "128000", "256000"], self.fetchComPorts(),
                                         ["Select Data Size (bits)", "8", "7", "6", "5"])
                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                            self.startThread(self.updateComPorts, (1,))
                        else:
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.pageRS232_1.CB2.clear()
                            self.pageRS232_1.CB2.addItems(self.fetchComPorts())
                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)
                            self.startThread(self.updateComPorts, (1,))


                    elif self.uiDialog.ConTypeCB.currentText() == "ETHERNET":
                        if self.device["Connection Type"] != "ETHERNET":
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.device["Connection Type"] = self.uiDialog.ConTypeCB.currentText()
                            for x in range(1, self.uiDialog.centerStackedWidget.count()):

                                self.uiDialog.centerStackedWidget.widget(x).deleteLater()

                            self.ipFormat = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
                            ipRegex = QRegExp(
                                "^" + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "$")
                            ipValidCheck = QRegExpValidator(ipRegex, self)
                            self.pageETHERNET_1 = dialogAB.dialogAbstractPage("LE", "ENTER IP ADDRESS", "CB", "", "CB", "")
                            self.pageETHERNET_1.LE1.setValidator(ipValidCheck)
                            self.addPage(self.pageETHERNET_1, [],
                                         ["Select Socket Family", "AF_INET", "AF_INET6", "AF_UNIX"],
                                         ["Select Socket Type", "Stream", "Datagram"])

                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)


                        else:
                            self.step = 2
                            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (Optional)":
                                self.device["DEVICE NAME"] = self.uiDialog.DeviceNameLE.text()
                            else:
                                self.device["DEVICE NAME"] = ""
                            self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
                            self.uiDialog.centerStackedWidget.setCurrentIndex(1)



            else:
                if self.uiDialog.DeviceTypeCB.currentText() == "Select Device (optional)":
                    self.uiDialog.statusLabel.setText("Please select a Device")

                else:
                    self.uiDialog.statusLabel.setText("Please select a Connection Type")

    def step2RS232(self):

        if self.sender() == self.pageRS232_1.CB1:
            if self.pageRS232_1.CB1.currentIndex() != 0 and self.pageRS232_1.CB2.currentIndex() != 0 and self.pageRS232_1.CB3.currentIndex() != 0:
                self.pageRS232_1.statusLabel.clear()

        elif self.sender() == self.customSignal:
            x = self.pageRS232_1.CB2.currentText()
            self.changeCBcontent(self.pageRS232_1.CB2, self.fetchComPorts())
            self.pageRS232_1.CB2.setEnabled(False)
            self.pageRS232_1.CB2.setEnabled(True)
            if self.pageRS232_1.CB2.findText(x) != -1:

                self.pageRS232_1.CB2.setCurrentIndex(self.pageRS232_1.CB2.findText(x))

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
                    self.step = 3
                    self.pageRS232_2 = dialogAB.dialogAbstractPage("LE", "Enter Timeout (optional, Default:None)", "CB",
                                                                   "", "CB", "")
                    self.addPage(self.pageRS232_2, [],
                                 ["Parity (Optional, Default:None)", "ODD", "EVEN", "MARK", "SPACE"],
                                 ["Stop Bits (Optional, Default:None)", "1", "1.5", "2"])
                    self.pageRS232_2.LE1.installEventFilter(self)
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)

                else:
                    self.step = 3
                    self.device["Baud Rate"] = self.pageRS232_1.CB1.currentText()
                    self.device["COM PORT"] = self.pageRS232_1.CB2.currentText()
                    self.device["Data size"] = self.pageRS232_1.CB3.currentText()
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)

            else:
                self.pageRS232_1.statusLabel.setText("Please fill out all mandatory fields")

        elif self.sender() == self.pageRS232_1.PB:
            self.step = 1
            self.uiDialog.centerStackedWidget.setCurrentIndex(0)

    def step2ETHERNET(self):

        if self.sender() == self.pageETHERNET_1.LE1:
            if self.pageETHERNET_1.LE1.text() != "" and self.pageETHERNET_1.CB2.currentIndex() != 0 and self.pageETHERNET_1.CB3.currentIndex() != 0:
                self.page.statusLabel.clear()

        elif self.sender() == self.pageETHERNET_1.CB2:

            if self.pageETHERNET_1.LE1.text() != "" and self.pageETHERNET_1.CB2.currentIndex() != 0 and self.pageETHERNET_1.CB3.currentIndex() != 0:
                self.page.statusLabel.clear()

        elif self.sender() == self.pageETHERNET_1.CB3:

            if self.pageETHERNET_1.LE1.text() != "" and self.pageETHERNET_1.CB2.currentIndex() != 0 and self.pageETHERNET_1.CB3.currentIndex() != 0:
                self.pageETHERNET_1.statusLabel.clear()

        elif self.sender() == self.pageETHERNET_1.CB:

            if self.pageETHERNET_1.LE1.text() != "" and self.pageETHERNET_1.CB2.currentIndex() != 0 and self.pageETHERNET_1.CB3.currentIndex() != 0:
                if self.uiDialog.centerStackedWidget.count() == 2:
                    self.step = 3
                    self.device["IP ADDRESS"] = self.pageETHERNET_1.LE1.text()
                    self.device["Address Family"] = self.pageETHERNET_1.CB2.currentText()
                    self.device["Socket Type"] = self.pageETHERNET_1.CB3.currentText()
                    self.pageETHERNET_2 = dialogAB.dialogAbstractPage("LE", "Enter Timeout (optional, Default:None)", "LE",
                                                                 "Enter Port Number", "", "")
                    self.PortnNumberFormat = "^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
                    pnRegex = QRegExp(self.PortnNumberFormat)
                    pnValidCheck = QRegExpValidator(pnRegex, self)
                    self.pageETHERNET_2.LE2.setValidator(pnValidCheck)
                    self.addPage(self.pageETHERNET_2, [], [], [])
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)

                else:
                    self.step = 3
                    self.device["IP ADDRESS"] = self.pageETHERNET_1.LE1.text()
                    self.device["Address Family"] = self.page.CB2.currentText()
                    self.device["Socket Type"] = self.page.CB3.currentText()
                    self.uiDialog.centerStackedWidget.setCurrentIndex(2)

            else:
                self.pageETHERNET_1.statusLabel.setText("Please fill out all mandatory fields")

        elif self.sender() == self.pageETHERNET_1.PB:
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

            self.close()

        elif self.sender() == self.pageRS232_2.PB:
            self.step = 2
            self.uiDialog.centerStackedWidget.setCurrentIndex(1)

    def step3ETHERNET(self):

        if self.sender() == self.pageETHERNET_2.CB:
            if self.pageETHERNET_2.LE2.text() != "":
                if self.pageETHERNET_2.LE1.text() != "Enter Timeout (optional, Default:None)":
                    self.device["Timeout"] = self.pageETHERNET_2.LE1.text()
                else:
                    self.device["Timeout"] = ""

                self.device["Port Number"] = self.pageETHERNET_2.LE2.text()

                self.close()
            else:
                self.pageETHERNET_2.statusLabel.setText("Please Enter a Port Number")

        elif self.sender() == self.pageETHERNET_2.PB:
            self.step = 2
            self.uiDialog.centerStackedWidget.setCurrentIndex(1)


class noDeviceFrame(QtWidgets.QFrame):

    def __init__(self):

        super().__init__()
        self.setStyleSheet("QFrame{background:transparent;}")
        self.setMinimumSize(QtCore.QSize(0, 500))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("noDeviceFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("")
        w = self.label_2.height()
        h = self.label_2.width()
        self.label_2.setPixmap(QtGui.QPixmap("resources/tyrannosaurus-rex.png")) #scaled(w,h, Qt.KeepAspectRatio)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff5500;\">No Devices Detected!</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Make sure devices are connected, turned on, and a suitable Visa library is installed!</span></p></body></html>")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.setShadow(self.label_5)
        self.setShadow(self.label_2)

    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)