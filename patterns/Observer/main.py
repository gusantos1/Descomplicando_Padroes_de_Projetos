from pattern import Observador, Observavel


caio = Observador('Caio', 'caio22@gmail.com')
fernanda = Observador('Fernanda', 'fernanda33@gmail.com')
marcela = Observador('Marcela', 'marcela21@gmail.com')
observadores = [caio, fernanda, marcela]

obs = Observavel()
for observador in observadores:
    obs.adicionar_observador(observador)

obs.notificar('Desconto exclusivo de 20%')