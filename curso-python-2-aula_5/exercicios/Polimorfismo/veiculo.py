# 1  Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# 2 No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

from abc import ABC,abstractmethod

class Veiculo:
  def __init__(self,modelo,marca):
    self.modelo = modelo
    self.marca = marca
  
    
  @abstractmethod
  def ligar(self):
    pass