from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QTextEdit, QListWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QEvent, QThread, QObject, pyqtSignal
from PyQt5.Qt import QTextCursor


class Signal(QObject):

    customSignal = pyqtSignal(str, str, str)

class editor(QTextEdit):

    def __init__(self, page, VID_PID, terminalName):
        super().__init__(page)
        self.VID_PID = VID_PID
        self.terminalName = terminalName
        self.viewport().installEventFilter(self)
        self.installEventFilter(self)
        self.setHtml("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#0033b3;\">Enter Command &gt;&gt; </span>")
        cursor = self.textCursor()
        self.msgSignal = Signal()
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)
        self.userInput = []
        self.lineNumber = 18

    def eventFilter(self, obj, event):

        if event.type() == QEvent.KeyPress:
            self.setTextColor(QtCore.Qt.black)
            if event.key() == QtCore.Qt.Key_Backspace and self.textCursor().position() < self.lineNumber:
                return True

            elif event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
                self.parseUserInput(self.toPlainText().rsplit(">>",1)[-1])
                self.lineNumber = self.textCursor().position() + 19
                self.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#0033b3;\">Enter Command >> </span>")
                #cursor = self.textCursor()
                #cursor.movePosition(QTextCursor.End)
                #cursor.movePosition(QTextCursor.Right)
                #self.setTextCursor(cursor)
                return True

            elif event.key() == QtCore.Qt.Key_Up or  event.key() == QtCore.Qt.Key_Down:
                return True
            elif event.key() == QtCore.Qt.Key_Left and self.textCursor().position() < self.lineNumber:
                return True

        if event.type() == QEvent.MouseButtonRelease:
            if event.button() == QtCore.Qt.LeftButton:
                if self.textCursor().position() < self.lineNumber:
                    cursor = self.textCursor()
                    cursor.movePosition(QTextCursor.End)
                    self.setTextCursor(cursor)
                    return True
                #print(self.textCursor().position())

        return False

    def parseUserInput(self,input):

        if input == " " or len(input) == 0:
            return

        elif input[0] == " ":
            input = input[1:]
            self.userInput.append(input)
        else:
            self.userInput.append(input)

        self.msgSignal.customSignal.emit(input, self.VID_PID, self.terminalName)


class readBack(QTextEdit):

    def __init__(self, frame, deviceName):

        super().__init__(frame)
        self.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#0033b3;\">Chixculub Impactor [Version 1.0.0] </span>")
        self.append("<span style=\"font-family:\'Courier new\'; font-size:11pt; color:#0033b3;\">{} Connected Successfully! </span>".format(deviceName[:len(deviceName)-8]))

class script(QTextEdit):

    def __init__(self, frame):

        super().__init__(frame)

class deviceList(QListWidget):

    def __init__(self, frame, connectedDevices):
        super().__init__(frame)
        self.availableDevices = connectedDevices

    def appendItems(self):

        for device in self.availableDevices:
            self.addItem()


class terminal(QtWidgets.QWidget):

    def __init__(self, objectName, VID_PID):

        super().__init__()
        self.setObjectName(objectName)
        self.VID_PID = VID_PID
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setStyleSheet("background-color: #F2F2F2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea_2.setStyleSheet("""
            QScrollBar::handle:vertical { 
                background-color: rgb(242,242,242,90);
                }
            QScrollBar::add-line:vertical {
                height: 0px;
                }
            QScrollBar::sub-line:vertical {
                height: 0px;
                }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                height: 0px;
                }
            QScrollBar::handle:vertical:hover{  
                background-color: rgb(214,214,214,90);
                }
                """)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1363, 673))
        self.scrollAreaWidgetContents_2.setStyleSheet("background: transparent;")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(9)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(9)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_20 = QtWidgets.QFrame(self.frame_4)
        self.frame_20.setMaximumSize(QtCore.QSize(120, 34))
        self.frame_20.setStyleSheet("\n"
                                    "\n"
                                    "QFrame:hover{\n"
                                    "background-color:rgb(226, 226, 226)\n"
                                    "}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.comboBox = QtWidgets.QComboBox(self.frame_20)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "    border:transparent;\n"
                                    "    color: black;\n"
                                    "    font: 14px;\n"
                                    "\n"
                                    "}\n"
                                    "QComboBox:focus:out {\n"
                                    "\n"
                                    "    selection-background-color: lightgray;\n"
                                    "    \n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:down-arrow {\n"
                                    "    image: url(resources/arrow.png);\n"
                                    "    width: 14px;\n"
                                    "    height: 14px;\n"
                                    "}\n"
                                    "QAbstractItemView{\n"
                                    "background:#F2F2F2;\n"
                                    "border:transparent;\n"
                                    "\n"
                                    "}")
        self.comboBox.setIconSize(QtCore.QSize(24, 24))
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/01-Terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/coding1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, "")
        self.verticalLayout_16.addWidget(self.comboBox)
        self.horizontalLayout_14.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_4)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_21.setMaximumSize(QtCore.QSize(120, 34))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_14.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_4)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_14.addWidget(self.frame_22)
        self.verticalLayout_15.addWidget(self.frame_4)
        self.frame_23 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_23)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.terminalEdit = editor(self.page, str(self.VID_PID), self.objectName())
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.terminalEdit.setFont(font)
        self.terminalEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.terminalEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.terminalEdit.setOverwriteMode(True)
        self.terminalEdit.setTabStopWidth(80)
        self.terminalEdit.setCursorWidth(10)
        self.terminalEdit.setPlaceholderText("")
        self.terminalEdit.setObjectName("terminalEdit")
        self.terminalEdit.setStyleSheet("\n"
                                        "QTextEdit{\n"
                                        "border:1px solid #AFACAC;\n"
                                        "color: black;"
                                        "background-color: #FFFFFF\n"
                                        "}")
        self.verticalLayout_19.addWidget(self.terminalEdit)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_24 = QtWidgets.QFrame(self.page_2)
        self.frame_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.textEdit = QtWidgets.QTextEdit(self.frame_24)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setCursorWidth(10)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("\n"
                                    "QTextEdit{\n"
                                    "border:1px solid #AFACAC;\n"
                                    "background-color: #FFFFFF\n"
                                    "}")
        self.verticalLayout_20.addWidget(self.textEdit)
        self.gridLayout_5.addWidget(self.frame_24, 0, 0, 1, 1)
        self.frame_25 = QtWidgets.QFrame(self.page_2)
        self.frame_25.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 32))
        self.frame_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_14 = QtWidgets.QFrame(self.frame_26)
        self.frame_14.setMaximumSize(QtCore.QSize(34, 34))
        self.frame_14.setStyleSheet("QFrame{\n"
                                    "background:transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame:hover{\n"
                                    "background-color:rgb(226, 226, 226)\n"
                                    "}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.runScriptBtn = QtWidgets.QPushButton(self.frame_14)
        self.runScriptBtn.setStyleSheet("QPushButton{\n"
                                        "border:transparent;\n"
                                        "}")
        self.runScriptBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runScriptBtn.setIcon(icon8)
        self.runScriptBtn.setIconSize(QtCore.QSize(24, 24))
        self.runScriptBtn.setFlat(True)
        self.runScriptBtn.setObjectName("pushButton_5")
        self.verticalLayout_14.addWidget(self.runScriptBtn)
        self.verticalLayout_22.addWidget(self.frame_14)
        self.frame_18 = QtWidgets.QFrame(self.frame_26)
        self.frame_18.setMaximumSize(QtCore.QSize(34, 34))
        self.frame_18.setStyleSheet("QFrame{\n"
                                    "background:transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame:hover{\n"
                                    "background-color:rgb(226, 226, 226)\n"
                                    "}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pauseBtn = QtWidgets.QPushButton(self.frame_18)
        self.pauseBtn.setStyleSheet("QPushButton{\n"
                                        "border:transparent;\n"
                                        "}")
        self.pauseBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseBtn.setIcon(icon9)
        self.pauseBtn.setIconSize(QtCore.QSize(24, 24))
        self.pauseBtn.setFlat(True)
        self.pauseBtn.setObjectName("pushButton_3")
        self.verticalLayout_13.addWidget(self.pauseBtn)
        self.verticalLayout_22.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_26)
        self.frame_19.setMaximumSize(QtCore.QSize(34, 34))
        self.frame_19.setStyleSheet("QFrame{\n"
                                    "background:transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame:hover{\n"
                                    "background-color:rgb(226, 226, 226)\n"
                                    "}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.stopBtn = QtWidgets.QPushButton(self.frame_19)
        self.stopBtn.setStyleSheet("QPushButton{\n"
                                      "border:transparent;\n"
                                      "}")
        self.stopBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/stop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopBtn.setIcon(icon10)
        self.stopBtn.setIconSize(QtCore.QSize(24, 24))
        self.stopBtn.setFlat(True)
        self.stopBtn.setObjectName("pushButton")
        self.verticalLayout_11.addWidget(self.stopBtn)
        self.verticalLayout_22.addWidget(self.frame_19)
        self.verticalLayout_21.addWidget(self.frame_26)
        self.gridLayout_5.addWidget(self.frame_25, 0, 2, 1, 1)
        self.frame_27 = QtWidgets.QFrame(self.page_2)
        self.frame_27.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 34))
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_30 = QtWidgets.QFrame(self.frame_28)
        self.frame_30.setMinimumSize(QtCore.QSize(24, 24))
        self.frame_30.setStyleSheet("QFrame{\n"
                                    "background:transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame:hover{\n"
                                    "background-color:rgb(226, 226, 226)\n"
                                    "}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.addDeviceBtn = QtWidgets.QPushButton(self.frame_30)
        self.addDeviceBtn.setMaximumWidth(24)
        self.frame_30.setMaximumWidth(24)
        self.addDeviceBtn.setStyleSheet("QPushButton{\n"
                                        "border:transparent;\n"
                                        "}")
        self.addDeviceBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/plus (5).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDeviceBtn.setIcon(icon11)
        self.addDeviceBtn.setIconSize(QtCore.QSize(24, 24))
        self.addDeviceBtn.setFlat(True)
        self.addDeviceBtn.setObjectName("pushButton_6")
        self.verticalLayout_25.addWidget(self.addDeviceBtn)
        self.horizontalLayout_17.addWidget(self.frame_30)
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setMinimumSize(QtCore.QSize(24, 24))
        self.frame_29.setStyleSheet("QFrame{\n"
                                    "background:transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame:hover{\n"
                                    "background-color:rgb(226, 226, 226)\n"
                                    "}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_29.setObjectName("frame_29")
        self.frame_24.setStyleSheet("QFrame{background:transparent;}")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.removeDeviceBtn = QtWidgets.QPushButton(self.frame_29)
        self.removeDeviceBtn.setMaximumWidth(24)
        self.frame_29.setMaximumWidth(24)
        self.removeDeviceBtn.setStyleSheet("QPushButton{\n"
                                        "border:transparent;\n"
                                        "}")
        self.removeDeviceBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources/delete (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeDeviceBtn.setIcon(icon12)
        self.removeDeviceBtn.setIconSize(QtCore.QSize(24, 24))
        self.removeDeviceBtn.setFlat(True)
        self.removeDeviceBtn.setObjectName("pushButton_7")
        self.verticalLayout_24.addWidget(self.removeDeviceBtn)
        self.horizontalLayout_17.addWidget(self.frame_29)
        self.verticalLayout_23.addWidget(self.frame_28)
        self.listWidget = QtWidgets.QListWidget(self.frame_27)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("\n"
                                      "QListWidget{\n"
                                      "border:1px solid #AFACAC;\n"
                                      "background-color: #FFFFFF;\n"
                                      "}")
        self.verticalLayout_23.addWidget(self.listWidget)
        self.gridLayout_5.addWidget(self.frame_27, 0, 1, 1, 1)
        self.stackedWidget_2.addWidget(self.page_2)
        self.verticalLayout_18.addWidget(self.stackedWidget_2)
        self.verticalLayout_15.addWidget(self.frame_23)
        self.readBack = readBack(self.scrollAreaWidgetContents_2, objectName)#QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.readBack.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.readBack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.readBack.setObjectName("textEdit_2")
        self.verticalLayout_15.addWidget(self.readBack)
        self.readBack.setStyleSheet("\n"
                                    "QTextEdit{\n"
                                    "border:1px solid #AFACAC;\n"
                                    "background-color: #FFFFFF\n"
                                    "}")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        self.page_2.setStyleSheet("background:transparent;")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("resources/terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.setItemText(0, "Terminal")
        self.comboBox.setItemText(1,  "Script")
        self.terminalEdit.setMouseTracking(True)
        self.comboBox.setEditable(True)
        self.comboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox.lineEdit().setReadOnly(True)
        self.pauseBtn.setToolTip("Pause Script")
        self.addDeviceBtn.setToolTip("Add device to script")
        self.stopBtn.setToolTip("Stop script")
        self.runScriptBtn.setToolTip("Run script")
        self.removeDeviceBtn.setToolTip("Remove device from script")
        self.readBack.setReadOnly(True)
        '''
        self.setShadow(self.terminalEdit)
        self.setShadow(self.textEdit)
        self.setShadow(self.addDeviceBtn)
        self.setShadow(self.pauseBtn)
        self.setShadow(self.stopBtn)
        self.setShadow(self.removeDeviceBtn)
        self.setShadow(self.runScriptBtn)
        self.setShadow(self.comboBox)
        '''
        self.connectBtns()

    def connectBtns(self):

        self.comboBox.currentTextChanged.connect(self.changePage)

    def changePage(self):

        if self.comboBox.currentText() == "Script":
            self.stackedWidget_2.setCurrentIndex(1)
        else:
            self.stackedWidget_2.setCurrentIndex(0)

    def setShadow(self, object):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        object.setGraphicsEffect(shadow)