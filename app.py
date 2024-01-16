from restaurante import Restaurante

restaurante_pizza = Restaurante('Pizzaria do Python', 'Pizzaria')
restaurante_japa = Restaurante('Comida Japonesa', 'Japonesa')
restaurante_mexicano = Restaurante('Mexicano Food', 'Mexicana')
restaurante_pizza.recber_avaliacao('João', 4)
restaurante_pizza.recber_avaliacao('Maria', 5)
restaurante_pizza.recber_avaliacao('José', 8)


def main():
    Restaurante.lista_restaurantes()
    

if __name__ == '__main__':
    main()