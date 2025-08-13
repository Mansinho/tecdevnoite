# Proponha uma classe a ser criada em Python. Crie pelo menos 4 atributos para essa classe e implemente pelo menos um método para 
# visualizar essas informações. Instanciar 3 objetos dessa classe e exibir as informações de cada um deles.

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano
        self.cor = cor

    def visualizar_carro(self):
        return f'''
Informações do veículo:

Marca: {self.marca}
Modelo: {self.modelo}
Ano: {self.ano}
Cor: {self.cor}
'''
    
if __name__ == "__main__":
    carro1 = Carro("Mercedes-Benz", "AMG C 63 S E Performance F1 Edition", 2024, "F1 Edition")
    carro2 = Carro("Ford", "Maverick", 1975, "Cinza")

    print(f'Veículo 1: {carro1.visualizar_carro()}')
    print(f'Veículo 2: {carro2.visualizar_carro()}')

