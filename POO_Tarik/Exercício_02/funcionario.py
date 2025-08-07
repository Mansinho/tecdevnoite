class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f'''
Dados do funcionário:
Nome: {self.nome}
Salário: {self.salario}
Cargo: {self.cargo}
'''