from tabnanny import verbose
from turtle import TurtleGraphicsError


class intro():
    Introvert = 9
    def __init__(self, valor):
        self.valor = valor
    def segundo(self):
        print("segundo")
    def tercero(self):
        print("tercero")
    
dato = intro("valor")
dir(dato)
print(dir(dato))

print(isinstance(dato,intro))
print(hasattr(dato,"Introvert"))
