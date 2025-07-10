#Peça ao usuário uma lista de 10 temperaturas, crie uma nova lista apenas com as temperaturas acima do valor da média.
temperatura = []
for i in range(10):
    temperatura.append(float(input('Digite uma temperatura: ')))
    media = sum(temperatura) / len(temperatura)
    nova_temperatura = [temp for temp in temperatura if temp > media]
print(nova_temperatura)