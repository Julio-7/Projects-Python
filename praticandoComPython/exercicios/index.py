projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
  if projeto:
    print(f"Projeto: {projeto}\n")
  else:
    print("Projeto não disponível.\n")
    


encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")