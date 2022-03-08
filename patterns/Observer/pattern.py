class Observador:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
    def receber_notificacao(self, msg):
        print(f'{msg} para {self.nome}')

class Observavel:
    def __init__(self):
        self.observadores = []
    
    def adicionar_observador(self, observador):
        self.observadores.append(observador)
   	
    def notificar(self, msg):
        for observador in self.observadores:
            observador.receber_notificacao(msg)