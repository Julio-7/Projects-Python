from veiculo import Veiculo
# 3)Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4) No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

class Carro(Veiculo):
  def __init__(self, modelo, marca, cor):
    super().__init__(modelo, marca)
    self.cor = cor
    
  def __str__(self):
    return f"{self.modelo} | {self.marca} | {self.cor}"
  
  def ligar(self):
    print(f"O carro {self.modelo} esta ligado")
    
  