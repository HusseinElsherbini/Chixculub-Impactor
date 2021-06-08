from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QRegExp
from PyQt5.QtGui import QRegExpValidator
import deleteDialog
import Dialog
from PyQt5.QtCore import pyqtSignal, QObject
from detectUsb import initDevice
import AboutMe

class customSignal(QObject):
    comChangedSignal = pyqtSignal()
    customSignal = pyqtSignal(str)

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
        self.deviceIcon.setPixmap(QtGui.QPixmap(":/icons/resources/{}".format(args[1])))
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
        self.icon5.addPixmap(QtGui.QPixmap(":/icons/resources/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.icon6.addPixmap(QtGui.QPixmap(":/icons/resources/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editBtn.setIcon(self.icon6)
        self.editBtn.installEventFilter(self)
        self.editBtn.setIconSize(QtCore.QSize(30, 30))
        self.editBtn.setToolTip("Modify Device")
        self.editBtn.setFlat(True)
        self.editBtn.setObjectName("editBtn")
        self.gridLayout.addWidget(self.editBtn, 0, 6, 1, 1)
        self.frameDeletedSignal = customSignal()
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
        if args[3] == "NOT FOUND":
            #self.connectBtn.setEnabled(False)
            self.setToolTip("CONNECTION ERROR! CHECK IP ADDRESS")

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

            self.icon6.addPixmap(QtGui.QPixmap(":/icons/resources/edit (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.editBtn.setIcon(self.icon6)
            return True

        if obj == self.editBtn and event.type() == QEvent.HoverLeave:

            self.icon6.addPixmap(QtGui.QPixmap(":/icons/resources/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.editBtn.setIcon(self.icon6)
            return True

        if obj == self.deleteBtn and event.type() == QEvent.HoverEnter:

            self.icon5.addPixmap(QtGui.QPixmap(":/icons/resources/delete (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.deleteBtn.setIcon(self.icon5)
            return True

        if obj == self.deleteBtn and event.type() == QEvent.HoverLeave:

            self.icon5.addPixmap(QtGui.QPixmap(":/icons/resources/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.deleteBtn.setIcon(self.icon5)
            return True

        return False

    def removeFrame(self):
        self.deleteLater()
        self.delDialog.close()
        if "LAN" in initDevice.devices[self.VID_PID]["Model Name"]:
            self.frameDeletedSignal.customSignal.emit("LAN")


    def closeDialog(self):
        self.delDialog.close()



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
        self.setShadow(self.uiDialog.statusLabel)
        self.setShadow(self.uiDialog.DeviceNameLE)
        self.PortnNumberFormat = "^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
        pnRegex = QRegExp(self.PortnNumberFormat)
        pnValidCheck = QRegExpValidator(pnRegex, self)
        self.uiDialog.PORTNUMBER_LE.setValidator(pnValidCheck)
        self.ipFormat = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegExp(
            "^" + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "\\." + self.ipFormat + "$")
        ipValidCheck = QRegExpValidator(ipRegex, self)
        self.uiDialog.IP_ADDRESS_LE.setValidator(ipValidCheck)
        #self.ComPorts = [port[0] for port in list(portsList.comports())]
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


    def close_Event(self):
        self.close()

    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)


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

    #############################################################################################################################
    #  Function: ConnectBtns                                                                                                    #
    #  Purpose: connects the confirm clicked event, device type and connection type comboboxes's current index changed events   #
    #           to addDeviceSteps function                                                                                      #
    #############################################################################################################################

    def ConnectBtns(self):
        self.uiDialog.ConfirmBtn.clicked.connect(self.verifyParam)



    def verifyParam(self):

        if self.uiDialog.IP_ADDRESS_LE.text() == "":

            self.uiDialog.statusLabel.setText("Please Enter an IP Address")


        else:
            for dev in initDevice.devices.keys():
                if initDevice.devices[dev]["Visa Handle"][7:] == self.uiDialog.IP_ADDRESS_LE.text():
                    self.close()
                    return
            self.device["IP Address"] = self.uiDialog.IP_ADDRESS_LE.text()

            if self.uiDialog.DeviceTypeCB.currentIndex() != 0:
                self.device["Device Type"] = self.uiDialog.DeviceTypeCB.currentText()
            else:
                self.device["Device Type"] = ""

            if self.uiDialog.DeviceNameLE.text() != "Enter Device Name (optional)":
                self.device["Device Name"] = self.uiDialog.DeviceNameLE.text()
            else:
                self.device["Device Name"] = ""

            if self.uiDialog.PORTNUMBER_LE.text() != "Enter Port Number (optional)":
                self.device["Port Number"] = self.uiDialog.PORTNUMBER_LE.text()
            else:
                self.device["Port Number"] = ""

            self.close()




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
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/resources/tyrannosaurus-rex.png")) #scaled(w,h, Qt.KeepAspectRatio)
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


class AboutMeDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.uiDialog = AboutMe.Ui_AboutDialog()  # create an instance of the dialog UI class
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
        self.uiDialog.closeBtn.clicked.connect(lambda: self.close())
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        self.uiDialog.Name.setGraphicsEffect(shadow)
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(25)
        self.uiDialog.Email.setGraphicsEffect(shadow1)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(25)
        self.uiDialog.Github.setGraphicsEffect(shadow2)
        shadow7 = QGraphicsDropShadowEffect()
        shadow7.setBlurRadius(25)
        self.uiDialog.Linkedin.setGraphicsEffect(shadow7)