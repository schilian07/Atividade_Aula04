#Questão 1
# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#Questão 2

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

# livro1 = Livro("A Metamorfose", " Jane Austen",  1813)
# livro2 = Livro("Orgulho e Preconceito", " Franz Kafka", 1915)

# print(livro1)
# print(livro2)

# #Questão 3

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

#     def emprestar(self):
#         self.disponivel = False

# livro = Livro("A Metamorfose", " Jane Austen",  1813)

# livro.emprestar()

# print(f"O livro está disponível? {'Sim' if livro.disponivel else 'Não'}")

#Questão 4

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]

livro1 = Livro("A Metamorfose", " Jane Austen",  1813)
livro2 = Livro("Orgulho e Preconceito", " Franz Kafka", 1915)
livro3 = Livro("O Grande Gatsby", " F. Scott Fitzgerald", 1925)
livro4 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)

livro1.emprestar()

livros_disponiveis_1915 = Livro.verificar_disponibilidade(1915)
for livro in livros_disponiveis_1915:
    print(livro)

livros_disponiveis_1967 = Livro.verificar_disponibilidade(1967)
for livro in livros_disponiveis_1967:
    print(livro)
