# Crie um sistema de consumo de itens multimídia. Nesse sistema estão presentes Filmes, Livros e Músicas. Crie uma superclasse "Midia" 
# que contém pelo menos 5 atributos comuns à qualque mídia e que possua pelo menos 3 métodos (operações que podem ser feitos com ele). 
# Implemente as subclasses Filmes, Livros e Músicas e crie pelo menos 1 método e 1 atributo único para cada um.

class Midia:
    def __init__(self, titulo, autor, ano, preco, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.preco = preco
        self.genero = genero

    def __str__(self):
    