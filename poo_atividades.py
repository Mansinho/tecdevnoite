# Atividade 1: Criação de uma Classe e Objeto

#   Descrição: Crie uma classe chamada Aluno com atributos nome e matricula. Adicione um método chamado
#   exibir_informacoes que imprime os detalhes do aluno. Crie um objeto dessa classe e chame o método. Crie o
#   método aprovado_reprovado que verifica se o aluno foi ou não aprovado.

# class Aluno:
#     def __init__(self, nome, matricula, nota):
#         self.nome = nome
#         self.matricula = matricula 
#         self.nota = nota 

#     def __str__(self):
#         return f"Nome: {self.nome} \nMatricula: {self.matricula} \nNota: {self.nota} \n"

#     def aprovado_reprovado(self):
#         if self.nota >= 7 and self.nota <= 10:
#             return "Aluno Aprovado"

#         elif self.nota >= 7 and self.nota <=0:
#             return "Aluno Reprovado"

#         else:
#             return "Nota invalida"

# aluno_1 =Aluno("Pedro", 12345, 10) 
# print(aluno_1)
# print(aluno_1.aprovado_reprovado()) 



# Atividade 2: Criando e Usando uma Classe

#   Descrição: Crie uma classe chamada Livro com atributos titulo e autor. Adicione um método chamado detalhes
#   que imprime o título e o autor do livro. Crie um objeto dessa classe e chame o método. Crie o método reputação,
#   no qual fala qual a reputação do livro

class Livro:
    def __init__(self, titulo, autor):
        self.titulo =  titulo
        self.autor = autor

    def __str__(self):
        return f"Titulo: {self.titulo} \n Autor: {self.autor}"
    
    def reputacao(self):
        if self.titulo >= 8 and self.titulo <= 10:
            return "Livro de alta reputação"
        
        elif self.titulo <= 8 and self.titulo >= 5:
            return "Livro de média reputação"
        
        elif self.titulo <= 5 and self.titulo >= 0:
            return "Livro de baixa reputação"
        
        else:
            return "Invalido"
        
    livro1 = Livro("Memórias do subsolo", "Fiódor Dostoiévski", 10)
    print(livro1)
    print(livro1.reputacao())