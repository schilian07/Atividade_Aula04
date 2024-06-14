#Questão 5 e 6 e 7
from Atividades_Aula04 import Livro

livro1 = Livro("A Metamorfose", " Jane Austen",  1813)
livro2 = Livro("O Grande Gatsby", " F. Scott Fitzgerald", 1925)

livro1.emprestar()

print(f"O livro 'Moby Dick' está disponível após o empréstimo? {'Sim' if livro1.disponivel else 'Não'}")

livros_disponiveis_1813 = Livro.verificar_disponibilidade(1813)
for livro in livros_disponiveis_1813:
    print(livro)

livros_disponiveis_1914 = Livro.verificar_disponibilidade(1914)
for livro in livros_disponiveis_1914:
    print(livro)