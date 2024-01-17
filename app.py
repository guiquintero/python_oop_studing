from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_pizza = Restaurante('Pizzaria do Python', 'Pizzaria')
bebida = Bebida('Coca-Cola', 5.00, 'Lata 350ml')
prato = Prato('Pizza de Calabresa', 40.00, 'Pizza de Calabresa com Catupiry')

restaurante_pizza.adicionar_item_cardapio(bebida)
restaurante_pizza.adicionar_item_cardapio(prato)

bebida.aplicar_desconto()
prato.aplicar_desconto()




def main():
    restaurante_pizza.exiber_cardapio
    

if __name__ == '__main__':
    main()