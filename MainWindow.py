# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1449, 1038)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1062, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setStyleSheet("")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopFrame = QtWidgets.QFrame(self.MainFrame)
        self.TopFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.TopFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.TopFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TopFrame.setObjectName("TopFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TopFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ToodleFrame = QtWidgets.QFrame(self.TopFrame)
        self.ToodleFrame.setMinimumSize(QtCore.QSize(80, 55))
        self.ToodleFrame.setMaximumSize(QtCore.QSize(80, 55))
        self.ToodleFrame.setStyleSheet("background-color:#28282B;")
        self.ToodleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ToodleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToodleFrame.setObjectName("ToodleFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ToodleFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Toodle = QtWidgets.QPushButton(self.ToodleFrame)
        self.Toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.Toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.Toodle.setAutoFillBackground(False)
        self.Toodle.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(61, 61, 61)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.Toodle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/165-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Toodle.setIcon(icon)
        self.Toodle.setIconSize(QtCore.QSize(30, 30))
        self.Toodle.setFlat(True)
        self.Toodle.setObjectName("Toodle")
        self.horizontalLayout_5.addWidget(self.Toodle)
        self.horizontalLayout.addWidget(self.ToodleFrame)
        self.frame_2 = QtWidgets.QFrame(self.TopFrame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_2.setStyleSheet("background:rgb(51,51,51);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.appName = QtWidgets.QFrame(self.frame_2)
        self.appName.setMouseTracking(True)
        self.appName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.appName.setObjectName("appName")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.appName)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.appName)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.horizontalLayout_6.addWidget(self.appName)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(55, 55))
        self.frame.setMaximumSize(QtCore.QSize(55, 55))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.minBtn = QtWidgets.QPushButton(self.frame)
        self.minBtn.setMaximumSize(QtCore.QSize(55, 55))
        self.minBtn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(61, 61, 61)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.minBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/042-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minBtn.setIcon(icon1)
        self.minBtn.setIconSize(QtCore.QSize(30, 30))
        self.minBtn.setFlat(True)
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_10.addWidget(self.minBtn)
        self.horizontalLayout_6.addWidget(self.frame)
        self.MaxBtn = QtWidgets.QFrame(self.frame_2)
        self.MaxBtn.setMinimumSize(QtCore.QSize(55, 55))
        self.MaxBtn.setMaximumSize(QtCore.QSize(55, 55))
        self.MaxBtn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MaxBtn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MaxBtn.setObjectName("MaxBtn")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.MaxBtn)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.maxBtn = QtWidgets.QPushButton(self.MaxBtn)
        self.maxBtn.setMaximumSize(QtCore.QSize(55, 55))
        self.maxBtn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(61, 61, 61)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.maxBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maxBtn.setIcon(icon2)
        self.maxBtn.setIconSize(QtCore.QSize(30, 30))
        self.maxBtn.setFlat(True)
        self.maxBtn.setObjectName("maxBtn")
        self.horizontalLayout_8.addWidget(self.maxBtn)
        self.horizontalLayout_6.addWidget(self.MaxBtn)
        self.CloseBtn = QtWidgets.QFrame(self.frame_2)
        self.CloseBtn.setMinimumSize(QtCore.QSize(55, 55))
        self.CloseBtn.setMaximumSize(QtCore.QSize(55, 55))
        self.CloseBtn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CloseBtn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CloseBtn.setObjectName("CloseBtn")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.CloseBtn)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.closeBtn = QtWidgets.QPushButton(self.CloseBtn)
        self.closeBtn.setMaximumSize(QtCore.QSize(55, 55))
        self.closeBtn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(61, 61, 61)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.closeBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/cancel (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setIconSize(QtCore.QSize(30, 30))
        self.closeBtn.setFlat(True)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_7.addWidget(self.closeBtn)
        self.horizontalLayout_6.addWidget(self.CloseBtn)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.TopFrame)
        self.CenterFrame = QtWidgets.QFrame(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CenterFrame.sizePolicy().hasHeightForWidth())
        self.CenterFrame.setSizePolicy(sizePolicy)
        self.CenterFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CenterFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CenterFrame.setObjectName("CenterFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.CenterFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.westFrame = QtWidgets.QFrame(self.CenterFrame)
        self.westFrame.setMinimumSize(QtCore.QSize(80, 0))
        self.westFrame.setMaximumSize(QtCore.QSize(80, 16777215))
        self.westFrame.setStyleSheet("background:rgb(51,51,51);")
        self.westFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.westFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.westFrame.setObjectName("westFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.westFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.westFrame)
        self.frame_5.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_5.setMaximumSize(QtCore.QSize(80, 55))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(self.frame_5)
        self.homeBtn.setMaximumSize(QtCore.QSize(80, 55))
        self.homeBtn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(61, 61, 61)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.homeBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/beach-house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon4)
        self.homeBtn.setIconSize(QtCore.QSize(30, 30))
        self.homeBtn.setFlat(True)
        self.homeBtn.setObjectName("homeBtn")
        self.horizontalLayout_3.addWidget(self.homeBtn)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.westFrame)
        self.frame_6.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_6.setMaximumSize(QtCore.QSize(80, 55))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 55))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.westFrame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(80, 85))
        self.frame_8.setMaximumSize(QtCore.QSize(80, 85))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(14, 0, 0, 25)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setMinimumSize(QtCore.QSize(55, 55))
        self.label_4.setMaximumSize(QtCore.QSize(55, 55))
        self.label_4.setStyleSheet("QLabel {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(51,51,51);\n"
"    border: 5px solid rgb(51,51,51);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("resources/asteroid.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.westFrame)
        self.eastFrame = QtWidgets.QFrame(self.CenterFrame)
        self.eastFrame.setStyleSheet("background-color:white")
        self.eastFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.eastFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.eastFrame.setObjectName("eastFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.eastFrame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.eastFrame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab:hover{\n"
"\n"
"    background:transparent;\n"
"    background-color:rgb(238, 238, 238);\n"
"    border:10px\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    bottom:1px;\n"
"    border-bottom-color:red\n"
"}\n"
"QTabWidget{\n"
"    border-color:white\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"   border-bottom-color:red;\n"
"border-color:blue;\n"
"min-height:1ex;\n"
"min-width:20ex;\n"
"padding: 5px 5px 10px 10px;\n"
"\n"
"}\n"
"QTabBar::tab:top:selected {\n"
"border-bottom: 3px solid rgb(255, 125, 127);\n"
"color:rgb(255, 125, 127);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    bottom:1px;\n"
"    background-colorrgb(241, 241, 241)\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Devices = QtWidgets.QWidget()
        self.Devices.setObjectName("Devices")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Devices)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_11 = QtWidgets.QFrame(self.Devices)
        self.frame_11.setStyleSheet("background-color:white")
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_11)
        self.stackedWidget.setObjectName("stackedWidget")
        self.devicesPage = QtWidgets.QWidget()
        self.devicesPage.setObjectName("devicesPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.devicesPage)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.devicesPage)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1367, 926))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setStyleSheet("QFrame{\n"
"\n"
"    border-radius:20px;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setStyleSheet("background:transparent;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_14.setStyleSheet("QFrame{\n"
"        color: black;\n"
"        border: 1px solid black;\n"
"        border-color:black;\n"
"        background:transparent;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"\n"
"        background:transparent;\n"
"        border-color: red;\n"
"        border-radius:20px;\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_5 = QtWidgets.QLabel(self.frame_14)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"border: transparent;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("resources/oscilloscope (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_14.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_14)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"\n"
"QLabel{\n"
" color:black;\n"
"border: transparent;\n"
"background-color: rgba(0,0,0,0%);\n"
"\n"
" }")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_14.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame_14)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 30))
        self.pushButton.setStyleSheet("\n"
"QPushButton {\n"
"  font: 75 10pt \"Microsoft YaHei UI\";\n"
" color:black;\n"
" background:transparent;\n"
" border-radius:15px;\n"
" border: 3px solid transparent;\n"
" \n"
"    border-color:#78e4ff;\n"
" padding:18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border-color:rgb(0, 255, 128);\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_14.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(249, 249, 249);\n"
"    border:transparent;\n"
"}")
        self.pushButton_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_14.addWidget(self.pushButton_3)
        self.verticalLayout_9.addWidget(self.frame_14)
        self.gridLayout_2.addWidget(self.frame_13, 1, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_15.setStyleSheet("")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setStyleSheet("background:transparent;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setStyleSheet("border-color:black;\n"
"background:transparent;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setLineWidth(5)
        self.frame_17.setMidLineWidth(2)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_4.setMinimumSize(QtCore.QSize(56, 56))
        self.pushButton_4.setMaximumSize(QtCore.QSize(56, 56))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"\n"
"    border-radius: 27px;\n"
"    border-style: outset;\n"
"    background-color:transparent;\n"
"     border: 3px solid transparent;\n"
"\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    border-color: rgb(0, 255, 128);\n"
"        \n"
"    }\n"
"\n"
"")
        self.pushButton_4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QtCore.QSize(56, 56))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_10.addWidget(self.pushButton_4)
        self.horizontalLayout_16.addWidget(self.frame_17)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.horizontalLayout_15.addWidget(self.frame_16)
        self.gridLayout_2.addWidget(self.frame_15, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.devicesPage)
        self.scriptPage = QtWidgets.QWidget()
        self.scriptPage.setObjectName("scriptPage")
        self.stackedWidget.addWidget(self.scriptPage)
        self.verticalLayout_7.addWidget(self.stackedWidget)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.tabWidget.addTab(self.Devices, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.bottomFrame = QtWidgets.QFrame(self.eastFrame)
        self.bottomFrame.setMinimumSize(QtCore.QSize(0, 20))
        self.bottomFrame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.bottomFrame.setStyleSheet("background:rgb(51,51,51);")
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.bottomFrame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12.addWidget(self.frame_10)
        self.drag = QtWidgets.QFrame(self.bottomFrame)
        self.drag.setMinimumSize(QtCore.QSize(20, 20))
        self.drag.setMaximumSize(QtCore.QSize(20, 20))
        self.drag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drag.setObjectName("drag")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.drag)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label = QtWidgets.QLabel(self.drag)
        self.label.setMinimumSize(QtCore.QSize(20, 20))
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_13.addWidget(self.label)
        self.horizontalLayout_12.addWidget(self.drag)
        self.verticalLayout_6.addWidget(self.bottomFrame)
        self.horizontalLayout_2.addWidget(self.eastFrame)
        self.verticalLayout.addWidget(self.CenterFrame)
        self.verticalLayout_11.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Chixculub Impactor"))
        self.minBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Minimize</p></body></html>"))
        self.maxBtn.setToolTip(_translate("MainWindow", "Maximize"))
        self.closeBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Close</p></body></html>"))
        self.homeBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Home</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">Power Supply</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>New Device</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Devices), _translate("MainWindow", "Devices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Terminal 1"))
