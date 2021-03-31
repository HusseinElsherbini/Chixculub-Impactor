import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow
import Styles
import Dialog
import MainWindow
import uiFunctions


class ChixclubImpactor(QMainWindow):

    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)
        self.buttons = {}
        self.dialogs = {}
        super().__init__()
        self.initUI()
        sys.exit(self.app.exec_())

    def initUI(self):

        # create main window dimensions and center it

        self.createWindow()
        self.oldPos = self.pos()
        uiFunctions.UIFunctions.activateTitleBarButtons(self)
        # create a menubar
        #self.addMenu()

        # create buttons and activate button press
        #self.addButton()
        #self.setButtonStyle('ADD DEVICE','style1',[20,50],[150,50],'resources/PowerSupply.png')

        #self.buttons['Button'].clicked.connect(self.buttonClicked)
       # self.activateButtonPress()

        # add toolbar
        #self.addToolbar()
        #self.statusBar()

        # modify style
        #self.set_Style()

        # add text editor
        #self.addTextEditor()
        self.center()
        # keeps record of old position of
        self.oldPosition = self.pos()
        # activates the app
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        newPos = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + newPos.x(), self.y() + newPos.y())
        self.oldPos = event.globalPos()

    def addButton(self):

        self.buttonGroup = QtWidgets.QButtonGroup()
        #self.window.MainWindow.B1.setStyleSheet(Styles.styles['style1'])
        id = 1
        for x in self.MainWindow.groupBox.findChildren(QtWidgets.QAbstractButton):
            self.buttonGroup.addButton(x,id)
            self.buttonGroup.button(id).setStyleSheet(Styles.styles['style1'])
            id += 1
            #self.window.MainWindow.B1.setStyleSheet(Styles.styles['style1'])
            #self.buttonGroup.button(1).setIcon(QtGui.QIcon('resources/PowerSupply.png'))
        #self.buttonGroup.setExclusive(True)


    def buttonClicked(self):

        sender = self.sender()

        if self.buttonGroup.checkedButton().objectName() == 'B1':
            self.statusBar().showMessage('B1')
            self.dialogs['addDeviceDialog'] = addDeviceDialog()
            #dialog.setStyleSheet(open("resources/frameless.qss",'r').read())
            #dialog.setAutoFillBackground(True)
            self.dialogs['addDeviceDialog'].adjustSize()
            self.dialogs['addDeviceDialog'].exec_()

    def createWindow(self):

        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove window top bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   # make window frameless


    def set_Style(self):

        palette = QtGui.QPalette()
        palette.setColor(palette.Window,QtGui.QColor(255,255,255))
        self.ModernWindow.setPalette(palette)


    def addMenu(self):

        menuBar = QtWidgets.QMenuBar(self)
        fileMenu = menuBar.addMenu('File')

        subMenu = fileMenu.addMenu('Port')
        subAct = QtWidgets.QAction('COM3', self)
        subMenu.addAction(subAct)

        newAct = QtWidgets.QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(subMenu)

    def center(self):

        qr = self.frameGeometry()
        cp = self.app.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addTextEditor(self):

        textEditor = self.QTextEdit()
        self.setCentralWidget(textEditor)



    def setButtonStyle(self, label, style, dimensions, position, IconPath):

        self.buttons[label].setGeometry(dimensions[0], dimensions[1], position[0], position[1])
        self.buttons[label].setStyleSheet(Styles.styles[style])
        if IconPath != 'NULL':
            self.buttons[label].setIcon(QtGui.QIcon(IconPath))

    def addToolbar(self):

        addEquipment = QtWidgets.QAction(QtGui.QIcon.fromTheme('list-add'), 'Add Equipment', self)

        self.addToolBar('Add Equipment').addAction(addEquipment)



    def showObjects(self):

        text = self.dialogs['addDeviceDialog'].TypeOfConnection.currentText()

        if text == 'RS232':
            self.dialogs['addDeviceDialog'].BaudRate.show()

    def hideObjects(self):

        self.dialogs['addDeviceDialog'].BaudRate.hide()

class addDeviceDialog(QtWidgets.QDialog):
    #creates an instance of a dialog when the ADD device button is pressed

    def __init__(self, parent=None):
        super().__init__(parent)
        self.addDevice = Dialog.Ui_DeviceInformation()
        self.addDevice.setupUi(self)

class Mainwin(QtWidgets.QMainWindow):

    def __init__(self, parent = None):

        super().__init__(parent)
        self.MainWindow = MainWindow.Ui_MainWindow()
        self.MainWindow.setupUi(self)

def main():

    Terminal = ChixclubImpactor()

if __name__ == '__main__':

    main()
