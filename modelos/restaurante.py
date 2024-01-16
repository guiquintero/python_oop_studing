from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):   
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
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


