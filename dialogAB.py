from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint


class dialogAbstractPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("AbstractPage")
        #self.setStyleSheet("background:transparent;")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_8.setContentsMargins(0, 25, 0, 0)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.AbstractFrame1 = QtWidgets.QFrame(self)
        self.AbstractFrame1.setMinimumSize(QtCore.QSize(0, 30))
        self.AbstractFrame1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AbstractFrame1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AbstractFrame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AbstractFrame1.setObjectName("AbstractFrame1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.AbstractFrame1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.AF1 = QtWidgets.QFrame(self.AbstractFrame1)
        self.AF1.setStyleSheet("QFrame{\n"
                               "\n"
                               "    background:transparent;\n"
                               "}")
        self.AF1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AF1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AF1.setObjectName("AF1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.AF1)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.CB1 = QtWidgets.QComboBox(self.AF1)
        self.CB1.setMinimumSize(QtCore.QSize(300, 30))
        self.CB1.setAutoFillBackground(True)
        self.CB1.setStyleSheet("QComboBox{\n"
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
                               "\n"
                               "")
        self.CB1.setEditable(True)
        self.CB1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.CB1.setIconSize(QtCore.QSize(24, 24))
        self.CB1.setFrame(False)
        self.CB1.setObjectName("CB1")
        self.horizontalLayout_9.addWidget(self.CB1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_7.addWidget(self.AF1)
        self.verticalLayout_8.addWidget(self.AbstractFrame1)
        self.AbstractFrame2 = QtWidgets.QFrame(self)
        self.AbstractFrame2.setMinimumSize(QtCore.QSize(0, 30))
        self.AbstractFrame2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AbstractFrame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AbstractFrame2.setObjectName("AbstractFrame2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AbstractFrame2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AF2 = QtWidgets.QFrame(self.AbstractFrame2)
        self.AF2.setAutoFillBackground(False)
        self.AF2.setStyleSheet("QFrame{\n"
                               "\n"
                               "    background:transparent;\n"
                               "}")
        self.AF2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AF2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AF2.setObjectName("AF2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.AF2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.CB2 = QtWidgets.QComboBox(self.AF2)
        self.CB2.setEnabled(True)
        self.CB2.setMinimumSize(QtCore.QSize(300, 30))
        self.CB2.setStyleSheet("QComboBox{\n"
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
        self.CB2.setObjectName("CB2")
        self.horizontalLayout_6.addWidget(self.CB2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_6.addWidget(self.AF2)
        self.verticalLayout_8.addWidget(self.AbstractFrame2)
        self.AbstractFrame3 = QtWidgets.QFrame(self)
        self.AbstractFrame3.setMinimumSize(QtCore.QSize(0, 30))
        self.AbstractFrame3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AbstractFrame3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AbstractFrame3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AbstractFrame3.setObjectName("AbstractFrame3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.AbstractFrame3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.AF3 = QtWidgets.QFrame(self.AbstractFrame3)
        self.AF3.setStyleSheet("QFrame{\n"
                               "\n"
                               "    background:transparent;\n"
                               "}")
        self.AF3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AF3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AF3.setObjectName("AF3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.AF3)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.CB3 = QtWidgets.QComboBox(self.AF3)
        self.CB3.setMinimumSize(QtCore.QSize(300, 30))
        self.CB3.setStyleSheet("QComboBox{\n"
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
        self.CB3.setObjectName("CB3")
        self.horizontalLayout_12.addWidget(self.CB3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.verticalLayout_9.addWidget(self.AF3)
        self.verticalLayout_8.addWidget(self.AbstractFrame3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 54, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem12)
        self.conPrevFrame = QtWidgets.QFrame(self)
        self.conPrevFrame.setEnabled(True)
        self.statusLabel = QtWidgets.QLabel(self)
        self.statusLabel.setStyleSheet("color:red; background:transparent; font-size:16px;")
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setIndent(0)
        self.statusLabel.setObjectName("statusLabel")
        self.setShadow(self.statusLabel)
        self.verticalLayout_8.insertWidget(0, self.statusLabel)
        self.conPrevFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.conPrevFrame.setStyleSheet("")
        self.conPrevFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conPrevFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.conPrevFrame.setObjectName("conPrevFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.conPrevFrame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.CPFrame = QtWidgets.QFrame(self.conPrevFrame)
        self.CPFrame.setEnabled(True)
        self.CPFrame.setStyleSheet("QFrame{\n"
                                   "background:transparent;\n"
                                   "}")
        self.CPFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CPFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CPFrame.setObjectName("CPFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.CPFrame)
        self.horizontalLayout_11.setContentsMargins(15, 0, 35, 15)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.PB = QtWidgets.QPushButton(self.CPFrame)
        self.PB.setEnabled(True)
        self.PB.setMinimumSize(QtCore.QSize(120, 30))
        self.PB.setMaximumSize(QtCore.QSize(120, 30))
        self.PB.setText("Previous")
        self.PB.setStyleSheet("\n"
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
        self.PB.setAutoDefault(False)
        self.PB.setFlat(True)
        self.PB.setObjectName("PB")
        self.horizontalLayout_11.addWidget(self.PB)
        self.CB = QtWidgets.QPushButton(self.CPFrame)
        self.CB.setEnabled(True)
        self.CB.setMinimumSize(QtCore.QSize(120, 30))
        self.CB.setMaximumSize(QtCore.QSize(120, 30))
        self.CB.setText("Confirm")
        self.CB.setStyleSheet("\n"
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
        self.CB.setAutoDefault(False)
        self.CB.setFlat(True)
        self.CB.setObjectName("CB")
        self.horizontalLayout_11.addWidget(self.CB)
        self.horizontalLayout_10.addWidget(self.CPFrame)
        self.verticalLayout_8.addWidget(self.conPrevFrame)

    def populateComboBox(self, obj, List):
        if obj == "Frame1":
            self.CB1.clear()
            self.CB1.addItems(List)

        elif obj == "Frame2":
            self.CB2.clear()
            self.CB2.addItems(List)

        elif obj == "Frame3":
            self.CB3.clear()
            self.CB3.addItems(List)

    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)
