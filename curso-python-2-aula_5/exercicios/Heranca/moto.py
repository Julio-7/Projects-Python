# 5 Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

from veiculo import Veiculo

class Moto(Veiculo):
  def __init__(self, marca, modelo, tipo):
    super().__init__(marca, modelo)
    self.tipo = tipo
  
  def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Tipo: {self.tipo} - Status: {status}"

    