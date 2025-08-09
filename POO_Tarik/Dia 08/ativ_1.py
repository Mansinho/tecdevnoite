# Crie uma classe Veiculo e implemente pelo menos 3 subclasses de veículo. Os veiculos devem possuir pelo menos 4 atributos e 
# ser capazes de acelerar, parar e mostrar informações.

class Veiculo:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 15
        print(f'O {self.marca} {self.modelo} está acelerando...')
    
    def parar(self):
        self.velocidade = 0
        print(f'O {self.marca} {self.modelo} está parado...')
    
    def informacoes(self):
        print(f'''
Informações do veículo:
Marca: {self.marca}
Modelo: {self.modelo}
Cor: {self.cor}
Ano: {self.ano}
''')
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)

v1 = Veiculo('Fiat', 'Palio', 'Branco', 2008)
v2 = Carro('Porsche', '911 GT3 RS', 'Roxo', 2024)
v3 = Moto('BMW', 'R 1250 GS', 'Preto', 2020)
v4 = Caminhao('Mercedes-Benz', 'Actros', 'Azul', 2015)

v1.acelerar()
v2.acelerar()
v3.parar()
v4.informacoes()

