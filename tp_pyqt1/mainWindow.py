import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__actions()
        self.__connectActions()
        self.__menubar()
        self.__toolBar()
        self.__shortcut()

        self.setWindowTitle("PROJECT IHM 2021-2022")
        self.resize(800, 400)

        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("Hello there !!")
        self.textEdit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.textEdit)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Bienvenue sur notre application")

        self.fileType = "txt"

    def __toolBar(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.copyActionN)
        fileToolBar.addAction(self.cutActionN)
        fileToolBar.addAction(self.newActionN)
        fileToolBar.addAction(self.openActionN)
        fileToolBar.addAction(self.pasteActionN)
        fileToolBar.addAction(self.saveActionN)
        fileToolBar.addAction(self.quitActionN)

    def __shortcut(self):
        self.newActionN.setShortcut("Ctrl+N")
        self.openActionN.setShortcut("Ctrl+O")
        self.saveActionN.setShortcut("Ctrl+S")
        self.quitActionN.setShortcut("Ctrl+Q")
        self.copyActionN.setShortcut("Ctrl+C")

    def __connectActions(self):
        self.openAction.triggered.connect(self.openFile)
        self.openActionN.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.saveActionN.triggered.connect(self.saveFile)
        self.quitAction.triggered.connect(self.quitApp)
        self.quitActionN.triggered.connect(self.quitApp)
        self.pasteAction.triggered.connect(self.pasteFile)
        self.pasteActionN.triggered.connect(self.pasteFile)
        self.newAction.triggered.connect(self.newFile)
        self.newActionN.triggered.connect(self.newFile)
        self.cutAction.triggered.connect(self.cutFile)
        self.cutActionN.triggered.connect(self.cutFile)
        self.copyAction.triggered.connect(self.copyFile)
        self.copyActionN.triggered.connect(self.copyFile)

    def __menubar(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        fileMenu = QMenu("&File", self)
        menu.addMenu(fileMenu)

        fileMenu.addAction(self.openActionN)
        fileMenu.addAction(self.saveActionN)
        fileMenu.addAction(self.copyActionN)
        fileMenu.addSeparator()
        fileMenu.addAction(self.quitActionN)

        menu.addAction(self.copyAction)
        menu.addAction(self.cutAction)
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.saveAction)
        menu.addAction(self.quitAction)

    def __actions(self):
        self.action = QAction(self)
        self.copyActionN  = QAction(QIcon("images/copy.png"),"&Copy", self)
        self.copyAction   = QAction("&Copy", self)
        self.cutActionN   = QAction(QIcon("images/cut.png"),"&Cut", self)
        self.cutAction    = QAction("&Cut", self)
        self.newActionN   = QAction(QIcon("images/new.png"),"&New", self)
        self.newAction    = QAction("&New", self)
        self.openActionN  = QAction(QIcon("images/open.png"),"&Open", self)
        self.openAction   = QAction("&Open", self)
        self.pasteActionN = QAction(QIcon("images/paste.png"),"&Paste", self)
        self.pasteAction  = QAction("&Paste", self)
        self.quitActionN  = QAction(QIcon("images/quit.png"),"&Quit", self)
        self.quitAction   = QAction("&Quit", self)
        self.saveActionN  = QAction(QIcon("images/save.png"),"&Save", self)
        self.saveAction   = QAction("&Save", self)


    def openFile(self):
        print("Open a été appuyé")
        self.statusbar.showMessage("Open a été appuyé")

        files = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.html *.txt)")
        if(files[0] != ""):
            filename = files[0].split('/')[-1]
            print("Nom du fichier : "+filename)

            filename = files[0]
            file = QFile(filename)

            file.open(QIODevice.ReadOnly | QFile.Text)
            txt = QTextStream(file).readAll()
            self.fileType = filename.split(".")[1]
            file.close()

            if(self.fileType == "html"):
                self.textEdit.setHtml(txt)
            else:
                self.textEdit.setPlainText(txt)

    def newFile(self):
        print("New a été appuyé")
        self.statusbar.showMessage("New a été appuyé")


    def saveFile(self):
        print("Save a été appuyé")
        self.statusbar.showMessage("Save a été appuyé")
        
        if(self.fileType == "html"):
            textBox = self.textEdit.toHtml()
        else:
            textBox = self.textEdit.toPlainText()
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName  = QFileDialog.getSaveFileName(self,"Veuillez entrer le nom du fichier (sans l'extension)",""," .txt;;.c;;.py;;.hs;;.css;;.js;;.html", options=options)
        if fileName[0] != "":
            with open(fileName[0]+fileName[1], 'w') as f:
                f.write(textBox)

    def pasteFile(self):
        print("Paste a été appuyé")
        self.statusbar.showMessage("Paste a été appuyé")
 
    def cutFile(self):
        print("Cut a été appuyé")
        self.statusbar.showMessage("Cut a été appuyé")


    def copyFile(self):
        print("Copy a été appuyé")
        self.statusbar.showMessage("Copy a été appuyé")

    def quitApp(self):
        print("Quit a été appuyé")
        self.statusbar.showMessage("Quit a été appuyé")
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Voulez-vous quitter ce programme ?")
        msgBox.setWindowTitle("Confirmation pour quitter")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        val = msgBox.exec()
        if val == QMessageBox.Yes: sys.exit()

    def closeEvent(self, event):
        print("Quit a été appuyé")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Voulez-vous quitter ce programme ?")
        msgBox.setWindowTitle("Confirmation pour quitter")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        val = msgBox.exec()

        if val == QMessageBox.Yes: 
            event.accept()
        else: 
            event.ignore()

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
