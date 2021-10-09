from PyQt5 import QtCore, QtWidgets, QtGui
from aship import alienShip
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        #super().__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.x=120
        self.y=220
        self.xbullet=self.x+25
        self.ybullet=self.y-20
        self.pull=[]
        self.alien=[]
    def paintEvent(self, e):
        Painter=QtGui.QPainter(self)
        Ship=QtGui.QImage("C:/Python/img/ship.bmp")
        Painter.drawImage(self.x,self.y,Ship)
        for i in self.pull:
            bullet=QtGui.QImage("C:/Python/img/bullet.bmp")
            Painter.drawImage(i[0],i[1],bullet)
        #print("jgjg")    
        for j in self.alien:
            j.draw(Painter)
        #print("jgj3543g")
        #alien1.draw(Painter)
        #alien2.draw(Painter)
        #alien3.draw(Painter)
        #alien4.draw(Painter)
        
        

    def keyPressEvent(self, event):
        if event.key()==QtCore.Qt.Key_B:
            self.timer.stop()
        if event.key()==QtCore.Qt.Key_Left:
            self.x=self.x-5
            self.repaint()
        if event.key()==QtCore.Qt.Key_Right:
            self.x=self.x+5
            self.repaint()
        if event.key()==QtCore.Qt.Key_Down:
            self.y=self.y+5
            self.repaint()
        if event.key()==QtCore.Qt.Key_Up:
            self.y=self.y-5
            self.repaint()
        if event.key()==QtCore.Qt.Key_Space:
            print("bullet")
            self.pull.append([self.x+25, self.y-20])
            self.repaint()
        if  event.key()==QtCore.Qt.Key_A:
            self.alien.append(alienShip(100,10))
            self.repaint()
            

    def update(self):
        print("tick")
        for j in self.alien:
            j.move(0, 10)
        #alien2.move(0, 10)
        #alien3.move(0, 10)
        #alien4.move(0, 10)
        #self.ybullet=self.ybullet-10
        for i in self.pull:
            i[1]=i[1]-10
            #if i[1]<=-1: self.pull.remove(i)
            for j in self.alien:
                if ((i[1]<=j.y+j.height) and ((i[0]<=j.x+j.width) and (i[0]>=j.x))):
                    self.pull.remove(i)
                    self.alien.remove(j)    
        self.repaint()
        

    def closeEvent(self, c):
        self.timer.stop()
        
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=MyWindow()
    window.setWindowTitle("пришельцы")
    window.resize(400,400)
    #alien=alienShip(50,30)
    #alien2=alienShip(120,30)
    #alien3=alienShip(190,30)
    #alien4=alienShip(260,30)
    window.show()
    sys.exit(app.exec_())
    
    
