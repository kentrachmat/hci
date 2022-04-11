import sys
import ButtonModel as bm
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CanvasButton(QWidget) :
    defaultCol = QColor(191, 189, 191)
    hoverCol = QColor(159, 177, 248)
    pressCol = QColor(60, 78, 150)

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.bbox = QRect(200, 40, 400, 250)
        self.setMouseTracking(True)
        self.cursorOver = True
        self.model = bm.ButtonModel()

    def mouseMoveEvent(self, event):
        self.pStart = event.pos()
        self.cursorOnEllipse(event.pos())
        if self.cursorOver :
            self.model.enter()
        else :
            self.model.leave()
        self.update()

    def mousePressEvent(self, event):
        self.pStart = event.pos()
        #print("press: ", self.pStart)
        if self.cursorOver :
            self.model.press()
        self.update()

    def mouseReleaseEvent(self, event):
        self.pStart = event.pos()
        #print("release: ", event.pos())
        self.model.release()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.bbox
        painter.setBrush(self.defaultCol)
        if self.model.state == 2 :
            painter.setBrush(self.hoverCol)
        if self.model.state == 3 :
            painter.setBrush(self.pressCol)
        painter.drawEllipse(rect)
        self.update()

    def cursorOnEllipse(self, point) :
        self.ellipse = QRegion(self.bbox, QRegion.Ellipse)
        if self.ellipse.contains(point) :
            self.cursorOver = True
            #print("move ellipse: ", self.pStart)

        else :
            self.cursorOver = False
            #print("move: ", self.pStart)


def main(args) :
    app = QApplication(args)
    win = QMainWindow()
    win.setWindowTitle("PROJECT IHM 2021-2022")
    win.resize(800, 400)

    canvasButton = CanvasButton()
    win.setCentralWidget(canvasButton)
    win.show()
    app.exec()
    
if __name__ == "__main__":
    main(sys.argv)