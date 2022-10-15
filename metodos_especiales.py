class Clase():
    #1
    def __new__(cls): #metodos especiales. personalizacion de instancias de las clases
        print("new")
        return super().__new__(cls) #devolver una instancia
    #2
    def __init__(self): #metodos especiales. inicializacion de las instancias de las clases
        print("init")

c = Clase()
 
