from math import *

class Circulo:
    def __init__(self,x,y,R):
        self.x=x
        self.y=y
        self.R=R
    
    def area(self):
        return pi*self.R**2
    
    def perimetro(self):
        return 2*pi*self.R
    
    def mostrar_propiedades(self):
        return (f"El circulo tiene un radio de {self.R} cm y su centro es")
