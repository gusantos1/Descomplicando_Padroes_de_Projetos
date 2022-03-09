class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.filiais = []
    
    def adicionar_filial(self, local):
        self.filiais.append(local)
    
    def mostrar_filiais(self):
        print(self.filiais)