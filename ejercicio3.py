class Nota:
    def __init__(self, nota, nombre_estudiante):
        self.nota=nota
        self.nombre_estudiante=nombre_estudiante
        
    def aprobado(self):
        if self.nota > 75:
            print(f"El/La estudiante {self.nombre_estudiante} ha aprobado")
            print(f"El/La estudiante {self.nombre_estudiante} ha reprobado")