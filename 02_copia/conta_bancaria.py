class Conta:

    def __init__(self, numero, saldo=0):
        self.saldo =  saldo
        self.numero = numero


    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para essa operação.")
            return False

    def deposito(self, valor):
        self.saldo += valor

    def imprime_saldo
        print ("O saldo é: R$ %.2f" self.saldo)
