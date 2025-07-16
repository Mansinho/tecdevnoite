#Questão 1:  Crie um dicionário que represente informações sobre uma pessoa, como nome, idade, cidade natal e 
# profissão.

# dadosPessoais = {"Nome": 'Ronaldo', "Idade": 20, "Cidade Natal": 'Natal', "Profissão": 'Analista de Segurança'}
# print(dadosPessoais)

#Questão 2 : Acesse e imprima valores específicos do dicionário que você criou no exercício anterior, como o 
# nome e a idade da pessoa.

# dadosPessoais = {"Nome": 'Ronaldo', "Idade": 20, "Cidade Natal": 'Natal', "Profissão": 'Analista de Segurança'}
# print(dadosPessoais ["Profissão"])
# print(dadosPessoais ["Cidade Natal"])

#Questão 3: Modifique o valor de um item no dicionário que você criou e, em seguida, imprima o dicionário 
# atualizado.

# dadosPessoais = {"Nome": 'Ronaldo', "Idade": 20, "Cidade Natal": 'Natal', "Profissão": 'Analista de Segurança'}
# print(dadosPessoais)
# dadosPessoais ["Nome"] = "Arthur"
# print(dadosPessoais)

#Questão 4: Adicione informações adicionais à pessoa no dicionário, como seu endereço de e-mail e número de 
# telefone.

# dadosPessoais = {"Nome": 'Ronaldo', "Idade": 20, "Cidade Natal": 'Natal', "Profissão": 'Analista de Segurança'}
# dadosPessoais ["E-mail"] = "ronaldo@gmail.com"
# dadosPessoais ["Telefone"] = " 84 99999-9999"
# print(dadosPessoais)

#Questão 5: Remova um item do dicionário, como o número de telefone, e imprima o dicionário atualizado.

# dadosPessoais = {"Nome": 'Ronaldo', "Idade": 20, "Cidade Natal": 'Natal', "Profissão": 'Analista de Segurança',
#                  "Telefone": '84 99999-9999'}
# print(dadosPessoais)
# dadosPessoais.pop ('Telefone')
# print(dadosPessoais)

#Questão 6:  Crie um dicionário com informações sobre vários amigos. Use um loop para iterar pelos itens do 
# dicionário e imprimir os nomes e idades dos amigos.

# amigos = {"Kaio":{"Idade": 20, "Profissao": 'Estudante', "Numero": '85 9 1000-0000'}, 
#           "Mikael":{"Idade": 22, "Profissao": 'Carteiro', "Numero": '85 9 1200-0000'},
#           "Alex": {"Idade": 27, "Profissao": 'Professor', "Numero": '84 9 1230-0000'}}

# for amigo in amigos:
#     print(amigo , ":" , amigos[amigo] ["Idade"])

#Questão 7 : Peça ao usuário para inserir o nome de um amigo e verifique se esse nome existe no dicionário de amigos. Imprima uma mensagem informando se o amigo está ou não na lista.

# nomeAmigo = input("Digite o nome do amigo: ")
# amigos = {"Kaio": 20, "Mikael": 22, "Alex": 27}

# if nomeAmigo in amigos:
#     print("O amigo está na lista")
# else:
#     print("Amigo não está na lista")

#Questão 8: Conte quantos amigos existem no dicionário e imprima o resultado.

# amigos = {"Kaio": 20, "Mikael": 22, "Alex": 27}
# print(f'Quantidade de amigos: {len(amigos)}')


#Desafio 1: Crie um dicionário de tradução que mapeie palavras de um idioma para outro (por exemplo, inglês para 
# espanhol). Peça ao usuário para inserir uma palavra em inglês e, em seguida, imprima a tradução correspondente.

# ingles = {"Hello": 'Ola', "Thanks": 'Obrigado', "Goodbye": 'Tchau', "Yes": 'Sim', "No": 'Não'}
# palavra = input("""
# ########## TRADUTOR EN -> PT ##########
#                 Digite uma palavra em inglês: """)
# print(f'A tradução de {palavra} é: {ingles[palavra]}')

#Desafio 2: Crie um dicionário que represente o estoque de uma loja, com produtos como chaves e quantidades em 
# estoque como valores. Permita que o usuário insira um produto e verifique se ele está em estoque. Se estiver, 
# informe a quantidade em estoque; caso contrário, informe que o produto não está disponível.

# estoque = {"Arroz": 20, "Carne": 15, "Feijão": 30, "Ovos": 25, "Pão": 10}
# produto = input("Digite o nome do produto: ")

# if produto in estoque:
#     print("O produto está em estoque")
# else:
#     print("O produto está faltando")
    


