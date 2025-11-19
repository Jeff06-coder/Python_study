#Classe ContaBancaria com encapsulamento de atributos
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Atributo privado, só pode ser acessado dentro da classe mãe
        self.__titular = titular            
        # Atributo privado
        self.__saldo = saldo_inicial        

    #Fuction/método público para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso por {self.__titular}.")
        else:
            print("Valor de depósito inválido.")
    
    #Fuction/método público para sacar dinheiro
    def sacar(self, valor):
        if 0 < valor and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso por {self.__titular}.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    #Fuction/método público para consultar o saldo
    def consultar_saldo(self):
        print(f"Saldo atual de {self.__titular}: R${self.__saldo}")
    
#Instanciando um objeto da classe ContaBancaria
conta1 = ContaBancaria("João Silva", 1000)

#Realizando operações na conta
conta1.consultar_saldo()
conta1.depositar(500)
conta1.sacar(100)
conta1.consultar_saldo()