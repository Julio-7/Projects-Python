# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from exer3 import Livros

# Criando os livros novamente no novo contexto
livro1 = Livros("Python in Practice", "Emily Coder", 2021)
livro2 = Livros("Machine Learning", "John AI", 2020)

print(f"Antes de emprestar (biblioteca): Livro disponível? {livro1.disponivel}")
livro1.emprestar_livro()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro1.disponivel}")

print("Livros disponiveis em 2021: ", Livros.verificar_disponibilidade(2022))
