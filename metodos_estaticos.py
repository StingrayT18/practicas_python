class persona():

    def __init__(self):
        pass

    def brincar(self):
        print("Brinco")

    @classmethod
    def correr(cls):
        print("Corro")

    @staticmethod    
    def nadar():
        print("Nadar")

jose = persona()
jose.nadar()

    