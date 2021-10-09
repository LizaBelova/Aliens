from PyQt5 import QtGui
class alienShip():
    def __init__ (self, x, y):
        self.x=x
        self.y=y
        self.ship=QtGui.QImage("C:/Python/img/alien.bmp")
        self.width=self.ship.width()
        self.height=self.ship.height()
        
        
    def draw(self, Painter):
        Painter.drawImage(self.x,self.y,self.ship)

    def move(self, dx, dy):
        self.x=self.x+dx
        self.y=self.y+dy
    def __del__(self):
        self.y=1000
    


