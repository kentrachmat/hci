import sys
import CanvasDessin as cd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Dessin(QMainWindow) :
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.canvasDessin = cd.CanvasDessin()
        self.setWindowTitle("PROJECT IHM 2021-2022")
        self.pixmap = QPixmap(20, 20)
        self.pixmap.fill(Qt.black)
        self.__menuBar()
        
    def __menuBar(self):
        self.fileToolBar = self.addToolBar("colorpicker")
        self.colorPicker   = QAction(QIcon("images/colorpicker.png"),"&colorpicker", self)
        self.widthPicker   = QAction(QIcon("images/width.png"),"&colorpicker", self)
        self.erasePicker   = QAction(QIcon("images/gomme.jpg"),"&colorpicker", self)

        self.icons = QIcon()  
        self.icons.addPixmap(self.pixmap, QIcon.Active)
        
        self.fileToolBar.addAction(self.colorPicker)
        self.fileToolBar.addAction(self.widthPicker)
        self.fileToolBar.addAction(self.erasePicker)
        self.fileToolBar.addAction(QAction(self.icons,"&colorpicker", self))

        self.colorPicker.triggered.connect(self.colorAction)
        self.widthPicker.triggered.connect(self.widthAction)
        self.erasePicker.triggered.connect(self.eraseAction)
    
    def widthAction (self):
        width, pressed = QInputDialog.getInt(self, "Input Width","Width:", 4, 0, 200, 1)
        if pressed:
            self.canvasDessin.setPenWidth(width)

    def colorAction(self):
        color = QColorDialog.getColor()
        if color.isValid(): 
            self.canvasDessin.setPenColor(color.name())
            self.pixmap.fill(color)
            self.removeToolBar(self.fileToolBar)
            self.__menuBar()

    def eraseAction(self):
        self.canvasDessin.atracer = []
        self.canvasDessin.repaint()

def main(args) :
    app = QApplication(args)
    dessin = Dessin()
    dessin.setCentralWidget(dessin.canvasDessin)
    dessin.show()
    app.exec()

if __name__ == "__main__":
    main(sys.argv)