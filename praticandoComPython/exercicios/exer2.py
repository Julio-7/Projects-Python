# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['julio', 'joao', 'gabriel','kauan']
ano_nascimento_atual = [2002,2025]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for numero in numeros:
  print(f'numero: {numero}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for numero in numeros:
  if(numero%2==1):
    soma += numero
print('A soma',soma)

# soma_impares = 0
# for i in range(1, 11, 2):
#     print(i)
# # print(soma_impares)


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
  print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input('Digite o numero para a tabuada: '))
for i in range(1,11):
  resultado = numero_tabuada * i
  print(f'Tabuada {numero_tabuada} X {i} = {resultado}')
  
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

soma_exer = 0

try:
  for numero in numeros:
      soma_exer += numero
  print(f'A soma dos elementos: {soma_exer}')
  # print(f'tamanho da lista é: ',len(numeros))
except:
  print('algo deu errado')


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

notas = [7.1, 6, 8, 4]
soma_valores = 0

try:
  for nota in notas:
    soma_valores += nota
    media = soma_valores / len(notas)
  print(f'A media das notas: {media:.2f}')
  
except ZeroDivisionError: # é uma exceção específica que ocorre quando há uma tentativa de divisão por zero
  print("A lista está vazia, não é possível calcular a média.") 

except Exception as e:
  print(e)