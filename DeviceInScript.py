import addDeviceToScript
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QEvent, QPoint, QObject, pyqtSignal
import detectUsb


class mySignal(QObject):

    dialogClosedSignal = pyqtSignal(dict, str)

class deviceInScriptDialog(QtWidgets.QDialog):

    def __init__(self, connectedDevices, VID_PID):

        super().__init__()
        #self.dev = args[0]
        self.uiDialog = addDeviceToScript.Ui_DeviceInScript() # create an instance of the dialog UI class
        self.uiDialog.setupUi(self)  # pass our dialog to the setup function of the UI wrapper
        self.oldPos = self.pos()  # keep track of the position of the dialog when it is first instantiated
        self.uiDialog.westTopFrame.installEventFilter(self)  # install an event filter to know when an event occurs on title bar
        self.dialogTitleBar()  # make window frameless
        self.connectedDevices = connectedDevices
        self.data = ""
        self.callingDev = VID_PID
        self.ConnectBtns()

    def dialogTitleBar(self):
        self.uiDialog.closeBtn.clicked.connect(self.close)
        self.uiDialog.minBtn.clicked.connect(lambda: self.showMinimized())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def ConnectBtns(self):

        self.uiDialog.ConfirmBtn.clicked.connect(self.collectData)


    def setShadow(self, obj):

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        obj.setGraphicsEffect(shadow)

    def addItems(self, connectedDevices):

        for dev in connectedDevices:
            if dev != self.callingDev:
                self.uiDialog.DeviceCB.addItem(detectUsb.initDevice.devices[dev]['Model Name'])

    def eventFilter(self, obj, event):

        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                self.oldPos = event.globalPos()
        if obj == self.uiDialog.westTopFrame and event.type() == QEvent.MouseMove:
            newPos = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + newPos.x(), self.y() + newPos.y())
            self.oldPos = event.globalPos()

        return False

    def collectData(self):

        if self.uiDialog.DeviceCB.currentIndex() != 0:
            self.data = self.uiDialog.DeviceCB.currentText()






