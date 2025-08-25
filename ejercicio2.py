class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo=titulo
        self.autor=autor
        self.precio=precio
        
    def mostrar_informacion(self):
        print(f"El libro titulado'{self.titulo}', escrito por '{self.autor}' se vende a {self.precio}")