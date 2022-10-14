import math
from tkinter import Y 
class punto():
    def _init_(self, x=0,y=0):
        self.x= x
        self.y= y
    def _str_(self):
        return "({},{})".format(self.x,self.y)
    def cuandrante(self):
        if self.x > 0 and self.y > 0:
            print("{} se encuentra en el pirmer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} se encuentra en el segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} se encuentra en el tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} se encuentra en el cuarto cuadrante".format(self))
        else:
            print("{} se encuentra en el origen".format(self))
    def vector(self):
        #NO SE
        pass
    
  

