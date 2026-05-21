class Conta:
    def __init__(self, titular, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor

    def obter_saldo(self):
        # ... verificações
        return self._saldo

conta = Conta("João", 1000)
print(conta._saldo)  # Acessando o saldo diretamente (não recomendado)
conta._saldo = 500  # Modificando o saldo diretamente (não recomendado)
conta.depositar(200)  # Depositando dinheiro usando o método

print(conta.obter_saldo())  # Obtendo o saldo usando o método