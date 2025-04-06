from modelos.restaurante import Restaurante
from modelos.cardapio.bebidda import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Paozinho', 2.0, 'Melhor Pao da Cidade')
prato_pao.aplicar_desconto()

bolo_de_chocolate = Sobremesa('Bolo de Chocolate', 8.0, 'cobertura de granulado', 'Fatiado', 'Medio')
bolo_de_chocolate.aplicar_desconto()

restaurante_praca.adionar_no_cardapio(bebida_suco)
restaurante_praca.adionar_no_cardapio(prato_pao)
restaurante_praca.adionar_no_cardapio(bolo_de_chocolate)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()