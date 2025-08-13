#Crie um programa em Python que simule um sistema de chamada de senhas em um laboratório. O programa deve apresentar um menu com três opções: 
# criar nova senha, chamar a próxima senha e desistir (encerrar o programa). Ao escolher a opção de criar nova senha, o programa gera uma nova 
# senha, que será adicionada ao final de uma lista. Ao escolher a opção de chamar próxima senha, o programa deve remover e exibir a primeira senha 
# da lista, simulando o atendimento em ordem de chegada. A opção de desistir encerra o programa. Após cada ação realizada, o programa deve exibir a 
# lista atualizada de senhas. O funcionamento do programa deve manter a ordem das senhas conforme foram inseridas, garantindo que a primeira a ser chamada 
# sempre seja a que entrou primeiro.

senha = []
while True:
    print("1 - Criar nova senha")
    print("2 - Chamar a próxima senha")
    print("3 - Desistir")
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        nova_senha = input("Digite a senha: ")
        senha.append(nova_senha)
        print(f"Senha {nova_senha} adicionada à fila.")
    elif escolha == "2":
        if len(senha) > 0:
            chamada = senha.pop(0)  
            print("Senha chamada:", chamada)
        else:
            print("Nenhuma senha na fila.")
    elif escolha == "3":
        print("Sair do programa")
        break
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")