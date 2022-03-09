from functools import singledispatch


class Mala:
    def __init__(self, dono, peso):
        self.dono = dono
        self.peso = peso


class Bolsa:
    def __init__(self, dono, peso):
        self.dono = dono
        self.peso = peso


@singledispatch
def despachante(bagagem):
    ...

@despachante.register
def manda_pro_aviao(bagagem: Mala):
    print('Foi pro avião')

@despachante.register
def volta_pro_passageiro(bagagem: Bolsa):
    print('Volta pro passageiro')


despachante(Bolsa('Guilherme', 58.90))