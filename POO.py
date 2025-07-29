class cachorro:
    def __init__(self, raça, idade, cor):
        self.raça = raça
        self.idade = idade
        self.cor = cor

    def latir(self):
        print("AUAU")

cachorro = cachorro("Bulldog, 3 anos, marrom")
cachorro.latir()  
