# 1 Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livros:
  livros = []
  
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.disponivel = True
    Livros.livros.append(self)  # Adiciona o livro na lista global

  # 2) Método especial __str__ para representar o objeto
  def __str__(self):
    return f"Nome do livro: {self.titulo} | Autor: {self.autor} | Ano da publicação: {self.ano_publicacao}"
  
  # 3) Método para emprestar livro
  def emprestar_livro(self):
    self.disponivel = False
    
  # 4) Método estático para verificar disponibilidade de livros em um ano específico
  @staticmethod
  def verificar_disponibilidade(ano):
    return [livro.titulo for livro in Livros.livros if livro.ano_publicacao == ano and livro.disponivel]

  

# Criando instâncias
livro_harry = Livros('Harry Potter', 'J.K. Rowling', 2001)
livro1 = Livros('Percy Jackson', 'Rick Riordan', 2001)

# Exibindo informações
print(livro_harry)
print(f"Antes de emprestar o livro: {livro_harry.disponivel}")
livro_harry.emprestar_livro()
print(f"Depois de emprestar o livro: {livro_harry.disponivel}")

# Chamando método corretamente
print("Livros disponíveis em 2001:", Livros.verificar_disponibilidade(2001))

