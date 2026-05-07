import textwrap
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0


    def __iter__(self):
        # O Python exige que o iterador retorne ele mesmo
        return self

    def __next__(self):
        # Se o nosso "contador" ainda não chegou ao fim da lista...
        if self._index < len(self.contas):
            # A gente pega a conta atual
            conta = self.contas[self._index]
            # Move o contador para a próxima posição
            self._index += 1
            # Entrega a conta e diz: "Aqui está, pode usar!"
            return f"{conta.agencia} | {conta.numero_conta} | {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}"
        
        # Se o contador passou do fim da lista, a gente avisa: "Acabou o baralho!"
        raise StopIteration

class Cliente:
    def __init__(self, edereco, nome):
        self.endereco = edereco
        self.contas = []
        self.nome = nome
        
    def realizar_transacao(self, conta, transacao):
        # Aqui o cliente dá a ordem para o "motoboy" agir no caso a função registrar da class Transacao
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, edereco, nome, cpf, data_nascimento):
        super().__init__(edereco, nome)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# Fazendo a class Conta, colocando seus construtores para a base das proximas
class Conta:
    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()
        self.agencia = "0001"

        @property
        def agencia(self):
            return self._agencia
        

    # Validando operações de saque e depósito para evitar saldo negativo e depósitos inválidos
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@Saldo insuficiente.@@@")
            return False
        self.saldo -= valor
        return True

    
    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@Valor de depósito deve ser positivo.@@@")
            return False
        self.saldo += valor
        return True
    

# Criando o tipo de conta corrente, adicionando os limites
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite_saque, limite_saldo):
        super().__init__(numero_conta, cliente)
        self.limite_saque = limite_saque
        self.limite_saldo = limite_saldo

    @classmethod
    def nova_conta(cls, numero_conta, cliente, limite_saque=3, limite_saldo=0): # <--- Veja se o nome aqui é 'nova_conta'
        return cls(numero_conta, cliente, limite_saque=limite_saque, limite_saldo=limite_saldo)

# Ciado o armazenamento em list array para guardar os extratos
class Historico:
    def __init__(self):
        self._transacoes = []

    # Fazendo uma função que so permite ver as transações e não podendo modificar
    @property
    def transacoes(self):
        return self._transacoes
    
    # Aqui é criado o método de adicionar o extrato
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            }
        )
    # Fazendo o metodo para gerar o resultado desejado da pesquisa, caso pesquise sem pedir o tipo, ele mostra todos
    #def gerar_relatorio(self, tipo_transacao=None):
        #if tipo_transacao:
            #transacoes_filtradas = [t for t in self.transacoes if t["tipo"] == tipo_transacao]
        #else:
            #transacoes_filtradas = self.transacoes
        #return transacoes_filtradas 

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self.transacoes:
            # Se não pediu tipo nenhum, ou se o tipo combina:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
             yield transacao  # Entrega a transação atual e "pausa" aqui 


# Fazendo a obrigação dos métodos para as classes filhas que executão a operação do saque e depósito
class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        # O Saque PERGUNTA para a conta se pode descontar
        # A LÓGICA de subtrair e a MENSAGEM DE ERRO estão dentro de conta.sacar
        sucesso_da_operacao = conta.sacar(self.valor)

        # O Saque só se preocupa com uma coisa: Se deu certo, eu anoto.
        if sucesso_da_operacao:
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        # O Depósito PERGUNTA para a conta se pode adicionar
        # A LÓGICA de somar e a MENSAGEM DE ERRO estão dentro de conta.depositar
        sucesso_da_operacao = conta.depositar(self.valor)

        # O Depósito só se preocupa com uma coisa: Se deu certo, eu anoto.
        if sucesso_da_operacao:
            conta.historico.adicionar_transacao(self)
            return True
        return False


def log_transacao(func):
    def wrapper(*args, **kwargs):
        print(f"\n[{datetime.now():%H:%M:%S}]@@@Iniciando transação...@@@")
        resultado = func(*args, **kwargs)
        print(f"[{datetime.now():%H:%M:%S}]@@@Transação finalizada.@@@\n")
        return resultado
    return wrapper

def menu():
    print('''
===============================================
Selecione a operação desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo cliente
[nc] Nova conta
[lc] Listar contas
[q] Sair
          ''')
    return input("Digite a opção: ").lower()


def filtrar_cliente(cpf, clientes):
    # Procura na lista de clientes se algum tem o CPF digitado
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    # Se achou, retorna o primeiro. Se não, retorna None.
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(clientes):
    
    if not clientes.contas:
        return None
    
    # Se quiser que o usuário escolha, você faria um pequeno menu aqui
    # Mas para o desafio da DIO, retornar a conta[0] costuma ser o suficiente.
    return clientes.contas[0]

@log_transacao
def depositar(clientes):
    # 1. Pergunta quem é o dono do dinheiro
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # 2. Se não achar o cliente, ele para aqui
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # 3. Pergunta o valor
    valor = float(input("Informe o valor do depósito: "))
    
    # 4. Cria o "objeto" transação (o papel do depósito)
    transacao = Deposito(valor)

    # 5. Pega a conta desse cliente (Recuperar conta)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # 6. Manda o cliente realizar a operação
    # Isso vai ativar o registrar() do Deposito e o depositar() da Conta
    cliente.realizar_transacao(conta, transacao)
    
@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do saque: "))

    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@Cliente não encontrado.@@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("\n@@@Cliente não possui conta.@@@")
        return
    
    print("\n@@@Extrato do cliente:@@@")
    
    transacao = conta.historico.gerar_relatorio()

    extrato = ""
    if not transacao:
        extrato = "Não há transações para este cliente."
    else:
        for t in transacao:
            extrato += f"{t['data']} - {t['tipo']}: R${t['valor']:.2f}\n"

        print(extrato)
        print(f"\nSaldo: R${conta.saldo:.2f}")
        print("===============================================")

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        nome = input("Informe o nome do cliente: ")
        endereco = input("Informe o endereço do cliente: ")
        cliente = PessoaFisica(endereco, nome, cpf, None)
        clientes.append(cliente)
        print("\n@@@Cliente criado com sucesso!@@@")

    print("\n@@@Cliente já existe!@@@")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@Cliente não encontrado!@@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero_conta=numero_conta)
    contas.append(conta)
    # Aqui a gente tem que lembrar que o cliente tem uma lista de contas, então a gente tem que adicionar essa conta lá também
    cliente.contas.append(conta)
    print("\n@@@Conta criada com sucesso!@@@")

def listar_contas(contas):
    
    for conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []
   
    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando o programa...")
            break
        else:
            print("\n@@@Opção inválida. Por favor, tente novamente.@@@")


main()