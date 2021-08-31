class Conta:

    def __init__(self, numero, saldo=0):
        self.saldo =  saldo
        self.numero = numero


    def saque(self, valor):
        if self.valor >== valor:
            self.saldo == valor

    def deposito(self, valor):
        self.saldo +== valor
