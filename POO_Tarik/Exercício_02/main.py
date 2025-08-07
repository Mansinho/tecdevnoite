# 1. Crie um sistema de gerenciamento de funcionários que faz uso de Programação Orientada a Objetos. Você deve criar um menu de opções que
#  contém as opções cadastrar funcionário e listar funcionários. Ao cadastrar funcionário, você deve utilizar a Classe Funcionario e
#  armazenar o funcionário criado em uma lista. Ao listar funcionários, você deve exibir os nomes e salários de todos os funcionários
#  cadastrados.
# Dados do Funcionário:
# - Nome
# - Salário
# - Cargo
# Bônus: Crie um método para exibir os dados de um funionário específico e permita que o usuário escolha qual funcionário deseja visualizar. 
# Crie um método para dar aumento para todos os funcionários.
from funcionario import Funcionario
class Sistema:
    def __init__(self):
        self.funcionarios = []
        self.opcao = 0

    def cadastrar_funcionario(self):
        nome = input("Digite o nome do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        cargo = input("Digite o cargo do funcionário: ")

        funcionario = Funcionario(nome, salario, cargo)
        self.funcionario.append(funcionario)
        print("Funcionário cadastrado com sucesso!")
        return funcionario
         
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'''
Nome: {funcionario.nome}
Salário: {funcionario.salario}
Cargo: {funcionario.cargo}
''')
    
    def menu(self):
        while True:
            print(f'''
########## Sistema de Gerenciamento de Funcionários ##########
                  1. Cadastrar funcionário
                  2. Listar funcionário
''')
            



    
    


