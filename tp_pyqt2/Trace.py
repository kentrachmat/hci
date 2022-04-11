from PyQt5.QtGui import *
class Trace :
    points = []
    width = 1
    color = QColor(50, 0, 50)
    
    def __init__(self, w=3,c=QColor(0, 50, 0)):
        self.width = w
        self.color = c
        self.points = []
        
    def add_points(self, val):
        self.points.append(val)