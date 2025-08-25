#Creacion de una galleta

class Galleta:
    def __init__(self, nombre, forma):
        self.nombre=nombre
        self.forma=forma
    
    def hornear(self):
        print("Esta",self.nombre,"ha sido horneada en forma de",self.forma)
    