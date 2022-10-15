class persona():
    
    edad = 18
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

persona1 = persona("Jose", "mexicano")

print(persona1.nombre)
