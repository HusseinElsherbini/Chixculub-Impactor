# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SerialModDialog(object):
    def setupUi(self, SerialModDialog):
        SerialModDialog.setObjectName("SerialModDialog")
        SerialModDialog.resize(409, 521)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SerialModDialog.sizePolicy().hasHeightForWidth())
        SerialModDialog.setSizePolicy(sizePolicy)
        SerialModDialog.setStyleSheet("\n"
"background-color:#ffecd9;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SerialModDialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainFrame = QtWidgets.QFrame(SerialModDialog)
        self.MainFrame.setMinimumSize(QtCore.QSize(408, 350))
        self.MainFrame.setStyleSheet("")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopFrame = QtWidgets.QFrame(self.MainFrame)
        self.TopFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.TopFrame.setStyleSheet("background:rgb(51,51,51);")
        self.TopFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TopFrame.setObjectName("TopFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TopFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.westTopFrame = QtWidgets.QFrame(self.TopFrame)
        self.westTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.westTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.westTopFrame.setObjectName("westTopFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.westTopFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2.addWidget(self.westTopFrame)
        self.minBtnFrame = QtWidgets.QFrame(self.TopFrame)
        self.minBtnFrame.setMinimumSize(QtCore.QSize(55, 55))
        self.minBtnFrame.setMaximumSize(QtCore.QSize(55, 55))
        self.minBtnFrame.setStyleSheet("background:transparent;")
        self.minBtnFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minBtnFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minBtnFrame.setObjectName("minBtnFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.minBtnFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minBtn = QtWidgets.QPushButton(self.minBtnFrame)
        self.minBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.minBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.minBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/042-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minBtn.setIcon(icon)
        self.minBtn.setIconSize(QtCore.QSize(30, 30))
        self.minBtn.setAutoDefault(False)
        self.minBtn.setFlat(True)
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_4.addWidget(self.minBtn)
        self.horizontalLayout_2.addWidget(self.minBtnFrame)
        self.closeBtnFrame = QtWidgets.QFrame(self.TopFrame)
        self.closeBtnFrame.setMinimumSize(QtCore.QSize(55, 55))
        self.closeBtnFrame.setMaximumSize(QtCore.QSize(55, 55))
        self.closeBtnFrame.setStyleSheet("background:transparent;")
        self.closeBtnFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.closeBtnFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.closeBtnFrame.setObjectName("closeBtnFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.closeBtnFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeBtn = QtWidgets.QPushButton(self.closeBtnFrame)
        self.closeBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.closeBtn.setMaximumSize(QtCore.QSize(30, 30))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/cancel (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QtCore.QSize(30, 30))
        self.closeBtn.setAutoDefault(False)
        self.closeBtn.setFlat(True)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        self.horizontalLayout_2.addWidget(self.closeBtnFrame)
        self.verticalLayout.addWidget(self.TopFrame)
        self.centerStackedWidget = QtWidgets.QStackedWidget(self.MainFrame)
        self.centerStackedWidget.setStyleSheet("")
        self.centerStackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.centerStackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.centerStackedWidget.setObjectName("centerStackedWidget")
        self.DeviceAndConTypePage = QtWidgets.QWidget()
        self.DeviceAndConTypePage.setStyleSheet("background:transparent;")
        self.DeviceAndConTypePage.setObjectName("DeviceAndConTypePage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DeviceAndConTypePage)
        self.verticalLayout_3.setContentsMargins(0, 25, 0, 0)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.statusLabel = QtWidgets.QLabel(self.DeviceAndConTypePage)
        self.statusLabel.setStyleSheet("color:red;")
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setIndent(0)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_3.addWidget(self.statusLabel)
        self.DeviceNameFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.DeviceNameFrame.setMinimumSize(QtCore.QSize(0, 30))
        self.DeviceNameFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.DeviceNameFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeviceNameFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeviceNameFrame.setObjectName("DeviceNameFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DeviceNameFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.DeviceName = QtWidgets.QFrame(self.DeviceNameFrame)
        self.DeviceName.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.DeviceName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeviceName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeviceName.setObjectName("DeviceName")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.DeviceName)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.DeviceNameLE = QtWidgets.QLineEdit(self.DeviceName)
        self.DeviceNameLE.setMinimumSize(QtCore.QSize(300, 30))
        self.DeviceNameLE.setMaximumSize(QtCore.QSize(300, 30))
        self.DeviceNameLE.setStyleSheet("QLineEdit{\n"
"    border:transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: 14px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:down-arrow {\n"
"    image: url(resources/arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QLineEdit QAbstractItemView {\n"
"\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(174, 255, 193);\n"
"    selection-color: black;\n"
"    background-color: white;\n"
"\n"
"}")
        self.DeviceNameLE.setText("")
        self.DeviceNameLE.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.DeviceNameLE.setClearButtonEnabled(True)
        self.DeviceNameLE.setObjectName("DeviceNameLE")
        self.horizontalLayout_3.addWidget(self.DeviceNameLE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.DeviceName)
        self.verticalLayout_3.addWidget(self.DeviceNameFrame)
        self.DeviceTypeFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.DeviceTypeFrame.setMinimumSize(QtCore.QSize(0, 30))
        self.DeviceTypeFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.DeviceTypeFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeviceTypeFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeviceTypeFrame.setObjectName("DeviceTypeFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.DeviceTypeFrame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.DeviceType = QtWidgets.QFrame(self.DeviceTypeFrame)
        self.DeviceType.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.DeviceType.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeviceType.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeviceType.setObjectName("DeviceType")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.DeviceType)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.DeviceTypeCB = QtWidgets.QComboBox(self.DeviceType)
        self.DeviceTypeCB.setMinimumSize(QtCore.QSize(300, 30))
        self.DeviceTypeCB.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DeviceTypeCB.setFont(font)
        self.DeviceTypeCB.setStyleSheet("QComboBox{\n"
"    border:transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: 14px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"\n"
"QComboBox:down-arrow {\n"
"    image: url(resources/arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(174, 255, 193);\n"
"    selection-color: black;\n"
"    background-color: white;\n"
"\n"
"}\n"
"")
        self.DeviceTypeCB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.DeviceTypeCB.setObjectName("DeviceTypeCB")
        self.DeviceTypeCB.addItem("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/battery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeviceTypeCB.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/multimeter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeviceTypeCB.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/power-supply (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeviceTypeCB.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/Device1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeviceTypeCB.addItem(icon5, "")
        self.horizontalLayout_9.addWidget(self.DeviceTypeCB)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_6.addWidget(self.DeviceType)
        self.verticalLayout_3.addWidget(self.DeviceTypeFrame)
        self.BaudRateFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.BaudRateFrame.setMinimumSize(QtCore.QSize(0, 30))
        self.BaudRateFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BaudRateFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BaudRateFrame.setObjectName("BaudRateFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.BaudRateFrame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.BaudRate = QtWidgets.QFrame(self.BaudRateFrame)
        self.BaudRate.setAutoFillBackground(False)
        self.BaudRate.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.BaudRate.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BaudRate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BaudRate.setObjectName("BaudRate")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.BaudRate)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.BaudRateCB = QtWidgets.QComboBox(self.BaudRate)
        self.BaudRateCB.setEnabled(True)
        self.BaudRateCB.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BaudRateCB.setFont(font)
        self.BaudRateCB.setStyleSheet("QComboBox{\n"
"    border:transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: 14px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"\n"
"QComboBox:down-arrow {\n"
"    image: url(resources/arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(174, 255, 193);\n"
"    selection-color: black;\n"
"    background-color: white;\n"
"\n"
"}\n"
"")
        self.BaudRateCB.setObjectName("BaudRateCB")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.BaudRateCB.addItem("")
        self.horizontalLayout_5.addWidget(self.BaudRateCB)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.BaudRate)
        self.verticalLayout_3.addWidget(self.BaudRateFrame)
        self.DataBitsFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.DataBitsFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.DataBitsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DataBitsFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DataBitsFrame.setObjectName("DataBitsFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.DataBitsFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.DataBits = QtWidgets.QFrame(self.DataBitsFrame)
        self.DataBits.setAutoFillBackground(False)
        self.DataBits.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.DataBits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DataBits.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DataBits.setObjectName("DataBits")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.DataBits)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.DataBitsCB = QtWidgets.QComboBox(self.DataBits)
        self.DataBitsCB.setEnabled(True)
        self.DataBitsCB.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DataBitsCB.setFont(font)
        self.DataBitsCB.setStyleSheet("QComboBox{\n"
"    border:transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: 14px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"\n"
"QComboBox:down-arrow {\n"
"    image: url(resources/arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(174, 255, 193);\n"
"    selection-color: black;\n"
"    background-color: white;\n"
"\n"
"}\n"
"")
        self.DataBitsCB.setObjectName("DataBitsCB")
        self.DataBitsCB.addItem("")
        self.DataBitsCB.addItem("")
        self.DataBitsCB.addItem("")
        self.DataBitsCB.addItem("")
        self.DataBitsCB.addItem("")
        self.horizontalLayout_10.addWidget(self.DataBitsCB)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_7.addWidget(self.DataBits)
        self.verticalLayout_3.addWidget(self.DataBitsFrame)
        self.ParityBitFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.ParityBitFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ParityBitFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ParityBitFrame.setObjectName("ParityBitFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ParityBitFrame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ParityBit = QtWidgets.QFrame(self.ParityBitFrame)
        self.ParityBit.setAutoFillBackground(False)
        self.ParityBit.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.ParityBit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ParityBit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ParityBit.setObjectName("ParityBit")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.ParityBit)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.ParityBitCB = QtWidgets.QComboBox(self.ParityBit)
        self.ParityBitCB.setEnabled(True)
        self.ParityBitCB.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ParityBitCB.setFont(font)
        self.ParityBitCB.setStyleSheet("QComboBox{\n"
"    border:transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: 14px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"\n"
"QComboBox:down-arrow {\n"
"    image: url(resources/arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(174, 255, 193);\n"
"    selection-color: black;\n"
"    background-color: white;\n"
"\n"
"}\n"
"")
        self.ParityBitCB.setObjectName("ParityBitCB")
        self.ParityBitCB.addItem("")
        self.ParityBitCB.addItem("")
        self.ParityBitCB.addItem("")
        self.ParityBitCB.addItem("")
        self.ParityBitCB.addItem("")
        self.ParityBitCB.addItem("")
        self.horizontalLayout_12.addWidget(self.ParityBitCB)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_9.addWidget(self.ParityBit)
        self.verticalLayout_3.addWidget(self.ParityBitFrame)
        self.TimeoutFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.TimeoutFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.TimeoutFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TimeoutFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TimeoutFrame.setObjectName("TimeoutFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.TimeoutFrame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Timeout = QtWidgets.QFrame(self.TimeoutFrame)
        self.Timeout.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.Timeout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Timeout.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Timeout.setObjectName("Timeout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.Timeout)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.TimeoutLE = QtWidgets.QLineEdit(self.Timeout)
        self.TimeoutLE.setMinimumSize(QtCore.QSize(300, 30))
        self.TimeoutLE.setMaximumSize(QtCore.QSize(300, 30))
        self.TimeoutLE.setStyleSheet("QLineEdit{\n"
"    border:transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: 14px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:down-arrow {\n"
"    image: url(resources/arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QLineEdit QAbstractItemView {\n"
"\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(174, 255, 193);\n"
"    selection-color: black;\n"
"    background-color: white;\n"
"\n"
"}")
        self.TimeoutLE.setText("")
        self.TimeoutLE.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.TimeoutLE.setClearButtonEnabled(True)
        self.TimeoutLE.setObjectName("TimeoutLE")
        self.horizontalLayout_11.addWidget(self.TimeoutLE)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_8.addWidget(self.Timeout)
        self.verticalLayout_3.addWidget(self.TimeoutFrame)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.ConfirmBtnFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.ConfirmBtnFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.ConfirmBtnFrame.setStyleSheet("")
        self.ConfirmBtnFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ConfirmBtnFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ConfirmBtnFrame.setObjectName("ConfirmBtnFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.ConfirmBtnFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.ConfirmBtnFrame)
        self.frame_3.setEnabled(True)
        self.frame_3.setStyleSheet("QFrame{\n"
"background:transparent;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(15, 0, 35, 15)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ConfirmBtn = QtWidgets.QPushButton(self.frame_3)
        self.ConfirmBtn.setEnabled(True)
        self.ConfirmBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.ConfirmBtn.setMaximumSize(QtCore.QSize(120, 30))
        self.ConfirmBtn.setStyleSheet("\n"
"QPushButton:enabled {\n"
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
"}\n"
"\n"
"\n"
"QPushButton:!enabled {\n"
"  font: 75 10pt \"Microsoft YaHei UI\";\n"
" color:black;\n"
" background:transparent;\n"
" border-radius:15px;\n"
" border: 3px solid transparent;\n"
" \n"
"    border-color:lightgrey;\n"
" padding:18px;\n"
"}")
        self.ConfirmBtn.setAutoDefault(False)
        self.ConfirmBtn.setFlat(True)
        self.ConfirmBtn.setObjectName("ConfirmBtn")
        self.horizontalLayout_7.addWidget(self.ConfirmBtn)
        self.horizontalLayout_8.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.ConfirmBtnFrame)
        self.centerStackedWidget.addWidget(self.DeviceAndConTypePage)
        self.verticalLayout.addWidget(self.centerStackedWidget)
        self.verticalLayout_2.addWidget(self.MainFrame)

        self.retranslateUi(SerialModDialog)
        self.centerStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SerialModDialog)

    def retranslateUi(self, SerialModDialog):
        _translate = QtCore.QCoreApplication.translate
        SerialModDialog.setWindowTitle(_translate("SerialModDialog", "Dialog"))
        self.DeviceNameLE.setPlaceholderText(_translate("SerialModDialog", "Enter Device Name (optional)"))
        self.DeviceTypeCB.setItemText(0, _translate("SerialModDialog", "Select Device (optional)"))
        self.DeviceTypeCB.setItemText(1, _translate("SerialModDialog", "Power Supply"))
        self.DeviceTypeCB.setItemText(2, _translate("SerialModDialog", "Digital Multimeter"))
        self.DeviceTypeCB.setItemText(3, _translate("SerialModDialog", "Electronic Load"))
        self.DeviceTypeCB.setItemText(4, _translate("SerialModDialog", "Oscilloscope"))
        self.BaudRateCB.setItemText(0, _translate("SerialModDialog", "Select Baud Rate"))
        self.BaudRateCB.setItemText(1, _translate("SerialModDialog", "9600"))
        self.BaudRateCB.setItemText(2, _translate("SerialModDialog", "14400"))
        self.BaudRateCB.setItemText(3, _translate("SerialModDialog", "19200"))
        self.BaudRateCB.setItemText(4, _translate("SerialModDialog", "38400"))
        self.BaudRateCB.setItemText(5, _translate("SerialModDialog", "57600"))
        self.BaudRateCB.setItemText(6, _translate("SerialModDialog", "115200"))
        self.BaudRateCB.setItemText(7, _translate("SerialModDialog", "128000"))
        self.BaudRateCB.setItemText(8, _translate("SerialModDialog", "256000"))
        self.DataBitsCB.setItemText(0, _translate("SerialModDialog", "Data Bits"))
        self.DataBitsCB.setItemText(1, _translate("SerialModDialog", "8"))
        self.DataBitsCB.setItemText(2, _translate("SerialModDialog", "7"))
        self.DataBitsCB.setItemText(3, _translate("SerialModDialog", "6"))
        self.DataBitsCB.setItemText(4, _translate("SerialModDialog", "5"))
        self.ParityBitCB.setItemText(0, _translate("SerialModDialog", "Parity Bit"))
        self.ParityBitCB.setItemText(1, _translate("SerialModDialog", "None"))
        self.ParityBitCB.setItemText(2, _translate("SerialModDialog", "Even"))
        self.ParityBitCB.setItemText(3, _translate("SerialModDialog", "ODD"))
        self.ParityBitCB.setItemText(4, _translate("SerialModDialog", "Mark"))
        self.ParityBitCB.setItemText(5, _translate("SerialModDialog", "Space"))
        self.TimeoutLE.setPlaceholderText(_translate("SerialModDialog", "Enter Timeout (milliseconds)"))
        self.ConfirmBtn.setText(_translate("SerialModDialog", "Confirm"))
