# Biblíoteca necessária para criar classes abstratas e métodos abstratos
from abc import ABC, abstractmethod

class Cliente():
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta.historico)
            transacao.registrar(conta)  # Registra a transação no histórico da conta
        else:
            print("Conta não pertence a este cliente.")
            
    @classmethod
    def filtrando_clientes(cls, clientes, cpf):
        """Busca um cliente na lista pelo CPF e o retorna"""
        for cliente in clientes:
            # Aqui assume-se que PessoaFisica tem o atributo 'cpf'
            if cliente.cpf == cpf:
                return cliente
        return None
        

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco, contas):
        super().__init__(endereco, contas)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def realizar_transacao(self, conta, transacao):
        # Passamos o objeto 'conta' inteiro para o registrar!
        transacao.registrar(conta)

class Conta:
    def __init__(self, numero_conta, cliente, historico):
        self.numero_conta = numero_conta
        self._saldo = 0
        self.historico = historico
        self.agencia = "0001"
        self.cliente = cliente

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
    
    @classmethod
    def buscar_conta(cls, numero, contas):
        """Varre a lista de contas e retorna a conta com o número digitado"""
        for conta in contas:
            if conta.numero_conta == numero:
                return conta
        return None


class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, historico, limite, limite_saques):
        super().__init__(numero_conta, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Fabrica uma nova conta corrente com os padrões certos"""
        historico = Historico()
        return cls(numero, cliente, historico, limite=500, limite_saques=3) 

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        

    @abstractmethod
    def registrar(self, historico):
        historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__(valor, "Saque")

    def registrar(self, historico):
        # historico aqui é o objeto da conta. Chamamos o sacar dela para validar e diminuir o saldo!
        sucesso_saque = historico.sacar(self.valor)
        
        # Se a conta aprovar o saque, salvamos no histórico dela
        if sucesso_saque:
            historico.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor, "Deposito")

    def registrar(self, historico):
        # historico aqui é o objeto da conta. Chamamos o depositar dela para mudar o saldo!
        historico.depositar(self.valor)
        
        # Agora acessamos o atributo 'historico' de dentro da conta para salvar a transação
        historico.historico.adicionar_transacao(self)


def menu():
    print('''
\n=========================
Bem-vindo ao Banco POO!
    1 - Criar cliente
    2 - Criar conta
    3 - Depositar
    4 - Sacar
    5 - Extrato
    0 - Sair
========================
'''
)

if __name__ == "__main__":
    contas = []
    clientes = []


    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Obrigado por usar o Banco POO! Até logo!")
            break

        # Lógica para criar cliente
        elif opcao == '1':
           cliente_nome = input("Digite o nome do cliente: ")
           cliente_cpf = input("Digite o CPF do cliente: ")
           cliente_data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
           cliente_endereco = input("Digite o endereço do cliente: ")
           cliente = PessoaFisica(cliente_nome, cliente_cpf, cliente_data_nascimento, cliente_endereco, [])
           clientes.append(cliente)
           print(f"Cliente {cliente_nome} criado com sucesso.")

        # Lógica para criar conta
        elif opcao == '2':
            cpf_procura = input("Digite o CPF do titular da conta: ")

            # !!! AGORA QUEM PROCURA É A CLASSE CLIENTE !!!
            cliente_encontrado = Cliente.filtrando_clientes(clientes, cpf_procura)

            if not cliente_encontrado:
                print("Cliente não encontrado. Por favor, crie o cliente primeiro.")
            else:
                # !!! QUEM FABRICA A CONTA É A PRÓPRIA CLASSE CONTA !!!
                numero_conta = len(contas) + 1  # Simples lógica para gerar número de conta
                nova_conta = ContaCorrente.nova_conta(cliente_encontrado, numero_conta)

                # Salva nas listas
            contas.append(nova_conta)
            cliente_encontrado.contas.append(nova_conta) # Vincula a conta ao cliente

            print("Opção para criar conta realizada com sucesso!")
            
        # Lógica para depositar
        elif opcao == '3':
            numero_procurado = int(input("Digite o número da conta para depósito: "))
        
            # 1. Busca o objeto da conta correspondente na lista global de contas
            conta_destino = Conta.buscar_conta(numero_procurado, contas)
        
            if conta_destino:
                valor = float(input("Digite o valor para depósito: "))
            
                # 2. Cria o objeto da transação de Depósito (Sua classe Deposito do Print 3)
                transacao = Deposito(valor)
            
                # 3. Executa a transação passando o cliente/conta (A regra do desafio DIO)
                # O cliente da conta é quem realiza a transação
                conta_destino.cliente.realizar_transacao(conta_destino, transacao)
            
                print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso na conta {numero_procurado}!")
            else:
                print("\n Erro: Conta não encontrada!")

        # Lógica para sacar  
        elif opcao == '4':
            numero_procurado = int(input("Digite o número da conta para saque: "))
        
            # 1. Busca o objeto da conta correspondente na lista global de contas
            conta_destino = Conta.buscar_conta(numero_procurado, contas)
        
            if conta_destino:
                valor = float(input("Digite o valor para saque: "))
            
                # 2. Cria o objeto da transação de Saque (Sua classe Saque do Print 3)
                transacao = Saque(valor)
            
                # 3. Executa a transação passando o cliente/conta (A regra do desafio DIO)
                # O cliente da conta é quem realiza a transação
                conta_destino.cliente.realizar_transacao(conta_destino, transacao)
            
                print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso na conta {numero_procurado}!")
            else:
                print("\n❌ Erro: Conta não encontrada!")
            

        # Lógica para extrato  
        elif opcao == '5':
            numero_procurado = int(input("Digite o número da conta para ver o extrato: "))
        
            # 1. Busca a conta na lista global de contas
            conta_alvo = Conta.buscar_conta(numero_procurado, contas)
        
            if conta_alvo:
                print(f"\n================ EXTRATO CONTA {numero_procurado} ================")
            
                # 2. Pega a lista de transações direto do histórico da conta encontrada
                # Lembra do Captura de tela 2026-06-17 083155.png? conta.historico.transacoes
                lista_transacoes = conta_alvo.historico.transacoes
            
                # 3. Verifica se a lista de transações está vazia
                if not lista_transacoes:
                    print("Não foram realizadas movimentações nesta conta.")
                else:
                    # 4. Se houver transações, passa por cada uma exibindo os detalhes
                    for transacao in lista_transacoes:
                        # Cada transação tem .tipo e .valor (definidos na classe Transacao)
                        print(f"{transacao.tipo}: R$ {transacao.valor:.2f}")
            
                    # 5. Exibe o saldo atual consolidado (que você definiu na classe Conta)
                    print(f"\nSaldo atual: R$ {conta_alvo._saldo:.2f}")
                    print("==================================================")
            
            else:
                print("\n❌ Erro: Conta não encontrada!")
            
        else:
            print("Opção inválida. Por favor, tente novamente.")