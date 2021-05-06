# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UsbDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UsbModDialog(object):
    def setupUi(self, UsbModDialog):
        UsbModDialog.setObjectName("UsbModDialog")
        UsbModDialog.resize(408, 350)
        UsbModDialog.setStyleSheet("\n"
"background-color:#ffecd9;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(UsbModDialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainFrame = QtWidgets.QFrame(UsbModDialog)
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
        self.frame_7 = QtWidgets.QFrame(self.DeviceNameFrame)
        self.frame_7.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.DeviceNameLE = QtWidgets.QLineEdit(self.frame_7)
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
        self.DeviceNameLE.setObjectName("DeviceNameLE")
        self.horizontalLayout_3.addWidget(self.DeviceNameLE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.DeviceNameFrame)
        self.DeviceTimeoutFrame = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.DeviceTimeoutFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeviceTimeoutFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeviceTimeoutFrame.setObjectName("DeviceTimeoutFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DeviceTimeoutFrame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.DeviceTimeoutFrame)
        self.frame_8.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.DeviceTimeoutLE = QtWidgets.QLineEdit(self.frame_8)
        self.DeviceTimeoutLE.setMinimumSize(QtCore.QSize(300, 30))
        self.DeviceTimeoutLE.setMaximumSize(QtCore.QSize(300, 30))
        self.DeviceTimeoutLE.setStyleSheet("QLineEdit{\n"
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
        self.DeviceTimeoutLE.setText("")
        self.DeviceTimeoutLE.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.DeviceTimeoutLE.setObjectName("DeviceTimeoutLE")
        self.horizontalLayout_5.addWidget(self.DeviceTimeoutLE)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.DeviceTimeoutFrame)
        self.DeviceTypeFrame_2 = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.DeviceTypeFrame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.DeviceTypeFrame_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.DeviceTypeFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeviceTypeFrame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeviceTypeFrame_2.setObjectName("DeviceTypeFrame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.DeviceTypeFrame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.DeviceTypeFrame_2)
        self.frame_4.setStyleSheet("QFrame{\n"
"\n"
"    background:transparent;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.DeviceTypeCB = QtWidgets.QComboBox(self.frame_4)
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
        icon5.addPixmap(QtGui.QPixmap("resources/oscilloscope (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeviceTypeCB.addItem(icon5, "")
        self.horizontalLayout_9.addWidget(self.DeviceTypeCB)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.DeviceTypeFrame_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.frame_2 = QtWidgets.QFrame(self.DeviceAndConTypePage)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
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
        self.verticalLayout_3.addWidget(self.frame_2)
        self.centerStackedWidget.addWidget(self.DeviceAndConTypePage)
        self.verticalLayout.addWidget(self.centerStackedWidget)
        self.verticalLayout_2.addWidget(self.MainFrame)

        self.retranslateUi(UsbModDialog)
        self.centerStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UsbModDialog)

    def retranslateUi(self, UsbModDialog):
        _translate = QtCore.QCoreApplication.translate
        UsbModDialog.setWindowTitle(_translate("UsbModDialog", "Dialog"))
        self.DeviceNameLE.setPlaceholderText(_translate("UsbModDialog", "Enter Device Name (optional)"))
        self.DeviceTimeoutLE.setPlaceholderText(_translate("UsbModDialog", "Enter read timeout (seconds)"))
        self.DeviceTypeCB.setItemText(0, _translate("UsbModDialog", "Select Device (optional)"))
        self.DeviceTypeCB.setItemText(1, _translate("UsbModDialog", "Power Supply"))
        self.DeviceTypeCB.setItemText(2, _translate("UsbModDialog", "Digital Multimeter"))
        self.DeviceTypeCB.setItemText(3, _translate("UsbModDialog", "Electronic Load"))
        self.DeviceTypeCB.setItemText(4, _translate("UsbModDialog", "Oscilloscope"))
        self.ConfirmBtn.setText(_translate("UsbModDialog", "Confirm"))