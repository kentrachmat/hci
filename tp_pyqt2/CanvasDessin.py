import Trace as tr
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CanvasDessin(QWidget) :
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setMouseTracking(True)
        self.size = self.setMinimumSize(1200,600)
        self.trace = tr.Trace()
        self.save = 0
        self.atracer = []
        self.pencolor = QColor(0, 0, 0)
        self.penwidth = 4.0

    def paintEvent(self, event):
        path = QPainterPath()
        painter = QPainter(self) 
        
        for p in self.atracer :
            path.clear()
            for pp in p.points :
                if pp == p.points[0] :
                    path.moveTo(pp)
                path.lineTo(pp)
            painter.setPen(QPen(p.color, p.width))
            painter.drawPath(path)

    def mouseMoveEvent(self, event):
        if self.save == 1:
            self.trait.points.append(event.pos())
        self.update()

    def mousePressEvent(self, event):
        self.pStart = event.pos()
        self.save = 1
        self.trait = tr.Trace(self.penwidth, self.pencolor)
        self.atracer.append(self.trait)
        self.update()

    def mouseReleaseEvent(self, event):
        self.pStart = event.pos()
        self.save = 0
        self.update()

    def getPenColor(self) :
        return self.pencolor
    
    def getPenWidth(self) :
        return self.penwidth

    def setPenColor(self, qcolor) :
        qcolor = qcolor[1:]
        r, g, b = int(qcolor[:2], 16), int(qcolor[2:4], 16), int(qcolor[4:6], 16)
        self.pencolor = QColor(r, g, b)

    def setPenWidth(self, width) :
        self.penwidth = width