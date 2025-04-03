from modelos.avaliacao import Avaliacao

class Restaurante:
  restaurantes = []
  def __init__(self, nome, categoria):
    self._nome = nome.title() # deixa o atribudo protegido
    self._categoria = categoria.upper() # deixa tudo em letra maiuscula
    self._ativo = False # deixa o atribudo protegido
    self._avaliacao = [] # todo restaurante podera receber avaliacoes
    Restaurante.restaurantes.append(self)

  def __str__(self): # O método __str__ é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto, mostraremos determinada informação. 
    return f'{self._nome} | {self.categoria}'
  
  @classmethod
  def listar_restaurantes(cls):
    print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
    for restaurante in cls.restaurantes:
      print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}")

  @property # transformanmos o metodo em um atributo
  def ativo(self):
    return '⌧' if self._ativo else '☐'
  
  def alternar_ativo(self):
    self._ativo = not self._ativo
  
  def receber_avaliacao(self, cliente, nota):
    avaliacao = Avaliacao(cliente,nota)
    self._avaliacao.append(avaliacao)
    
  @property
  def media_avaliacoes(self):
    if not self._avaliacao:
      return 0
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #  informar que desejamos pegar todas as avaliações e, para cada avaliação, a única informação que queremos é a nota
    quantidade_de_notas = len(self._avaliacao)
    media = round(soma_das_notas/quantidade_de_notas,1) # esse ultimo numero definira quantas casas decimais mostrara
    return media
    
restaurante_praca = Restaurante('Ana Bella', 'Gourmet')
restaurante_bairro = Restaurante('Pizzaria', 'Massas')
restaurante_bairro.nome = 'Pizza 3.0' # nao consegue alterar nome pois o atributo nome esta protegido

restaurante_bairro.alternar_ativo()

# print(vars(restaurante_praca)) exibe tudo 

# Restaurante.listar_restaurantes()
