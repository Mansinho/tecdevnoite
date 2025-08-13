# class Carro:
#     rodas = 4
#     combustivel = "flex"
#     farois = 2
#     carroceria = "sedan"

#     def __init__(self, marca, modelo, ano, cor):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.cor = cor

#     def __str__(self):
#         return f"{self.marca} {self.modelo} {self.ano} {self.cor}"
    

# 1. Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material

# Métodos: trocaCor, mostraCor e CalcArea

import math

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

        def trocaCor(self, cor):
            self.cor = cor
            
        def mostraCor(self):
            return self.cor
            
        def CalcArea(self):
            raio = self.circunferencia / (2 * math.pi)
            area = 4 * math.pi * (raio ** 2)
            return area 
        
        def __str__(self):
            return f"Bola de {self.cor}, com circunferência de {self.circunferencia} cm, feita de {self.material}"
        
        bola = Bola("vermelha", 12.56, "borracha")

        print(bola.mostraCor())
        bola.trocaCor("azul")
        print(bola.mostraCor())
        area = bola.calcArea()
        print(f"Área da bola: {area:.2f} cm²")