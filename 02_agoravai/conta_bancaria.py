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

class ContaPoupanca:
    def __init__(self):
        self.tipo = "cp"

class ContaCorrente(Conta):
    def __init__(self):
        self.tipo = "cc"
        self.limite_credito = 0

    def v_aumenta_limite(self, alteracao):
        self.limite_credito = alteracao
