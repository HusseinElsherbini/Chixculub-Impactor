from main import ChixculubImpactor, addDeviceDialog
from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QEvent

WINDOW_STATE = 0


class UIFunctions(ChixculubImpactor):

    def activateTitleBarButtons(self):
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        self.ui.minBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.maxBtn.clicked.connect(lambda: UIFunctions.maximizeRestore(self))
        self.ui.Toodle.clicked.connect(lambda: UIFunctions.toodle(self, 160, True))

    def maximizeRestore(self):
        global WINDOW_STATE
        status = WINDOW_STATE
        if status == 0:
            self.showMaximized()
            WINDOW_STATE = 1
            self.ui.maxBtn.setToolTip("Restore")
            self.ui.maxBtn.setIcon(QIcon("resources/051-minimize.png"))
            self.ui.drag.hide()
        else:
            WINDOW_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.maxBtn.setToolTip("Maximize")
            self.ui.maxBtn.setIcon(QIcon("resources/expand.png"))
            self.ui.drag.show()

    def toodle(self, maxWidth, clicked):

        global elongate
        for x in self.ui.westFrame.findChildren(QFrame):
            x.setStyleSheet("background:rgb(51,51,51)")
        minWidth = 80
        if clicked:
            currentWidth = self.ui.westFrame.width()
            minWidth = 80

            if currentWidth == 80:
                elongate = maxWidth

            else:
                elongate = minWidth

        self.animation = QPropertyAnimation(self.ui.westFrame, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(minWidth)
        self.animation.setEndValue(elongate)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


class dialogUIFunctions(addDeviceDialog):

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(lambda: self.close())
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        self.uiDialog.frame_7.setGraphicsEffect(shadow)
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        self.uiDialog.pushButton.setGraphicsEffect(shadow1)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        self.uiDialog.ConTypeFrame.setGraphicsEffect(shadow2)
