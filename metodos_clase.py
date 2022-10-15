from traceback import print_tb


class persona():
    def __init__(self):
        pass
    
    def despedir(self):
        print("Adiós")

    @classmethod    
    def saludar(cls, nombre):
        print("Estoy saludando"+nombre)

persona.saludar(" Juan")