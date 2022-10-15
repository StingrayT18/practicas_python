class Perro:

    def avanzar(self):
        print("Tenemos 4 patas")

class Perico:

    def avanzar(self):
        print("Volar")

def mover(animal):
    animal.avanzar


perro = Perro()
perico = Perico()
perro.avanzar()
perico.avanzar()

mover(perro)
mover(perico)