class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo=saldo
        self.numero_agencia=numero_agencia

    def sacar(self, valor):
        self._saldo-=valor

    def depositar(self, valor):
        self._saldo+=valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("051", 100)
conta.depositar(100)
print(conta.mostrar_saldo())
print(conta.numero_agencia)