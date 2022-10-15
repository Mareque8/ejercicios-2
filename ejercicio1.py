import math

class punto:
    def _init_(self,x=0,y=0):
        self.x= x
        self.y= y
    def _str_(self):
        return "({},{})".format(self.x,self.y)
    def cuadrante(self):
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
    def vector(self,p):
          print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )    
class rectangulo:
    def _init_(self,pinicial=punto(),pfinal=punto()):
        self.pinicial = pinicial
        self.pfinal = pfinal
    def base(self):
        self.base = abs(self.pfinal.x-self.pinicial.x)
        print("{}  es la base  ".format(self.base))
    def altura(self):
        self.altura = abs(self.pfinal.y-self.pinicial.y)
        print("{} es la altura ".format(self.altura))
    def area(self):
        self.base = abs(self.pfinal.x-self.pinicial.x)
        self.altura = abs(self.pfinal.y-self.pinicial.y)
        self.area = abs(self.base*self.altura)
        print("{} es el area ".format(self.area))
        

a = punto(2, 3)
b = punto(5,5)
c = punto(-3, -1)
d = punto(0,0)

a.cuadrante
b.cuadrante
d.cuadrante
a.vector(b)
b.vector(a)
R = rectangulo(a,b)
R.base()
R.altura()
R.area()









