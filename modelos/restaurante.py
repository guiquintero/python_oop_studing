from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):   
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)} | {str(self.media_avaliacoes).ljust(20)} | {self.ativo}'
    
    @classmethod
    def lista_restaurantes(cls):
        print(f'{"NOME".ljust(20)} | {"CATEGORIA".ljust(20)} | {"AVALIACAO".ljust(20)} | {"ATIVO"}')
        for r in cls.restaurantes:
            print(r)

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def recber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma = sum(avaliacoes._nota for avaliacoes in self._avaliacoes)

        quantidade = len(self._avaliacoes)

        return round(soma / quantidade, 1)

    # def adicionar_bebida_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)

    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exiber_cardapio(self):
        print(f'{self._nome.ljust(25)} {"PRECO".ljust(13)} {"DESCRICAO"}')
        for item in self._cardapio:
            print(item)
            
