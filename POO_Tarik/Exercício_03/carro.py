class Carro:
    def __init__(self, marca, modelo, ano, velocidade_maxima_kmh, aceleracao):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = 0  # em m/s
        self.velocidade_maxima_kmh = velocidade_maxima_kmh  #km/h
        self.velocidade_maxima = velocidade_maxima_kmh / 3.6  #convertendo para m/s
        self.aceleracao = aceleracao  # em m/s²
        self.tempo_arrancada = self.velocidade_maxima / self.aceleracao
        self.distancia_arrancada = 1/2 * self.aceleracao * (self.tempo_arrancada ** 2)

    def simular_arrancada(self):
        print(f"\nSimulando arrancada do {self.marca} {self.modelo} ({self.ano})...")
        print(f"Velocidade máxima: {self.velocidade_maxima_kmh} km/h")
        print(f"Aceleração: {self.aceleracao} m/s²")
        print(f"Tempo para atingir velocidade máxima: {self.tempo_arrancada:.2f} segundos")
        print(f"Distância percorrida na arrancada: {self.distancia_arrancada:.2f} metros")
        

