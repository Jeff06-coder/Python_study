# Banco com as seguintes funcionalidades:
def menu():
    print('''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [cc] Criar Conta
    [cu] Criar Usuário
    [ent] Entrar na Conta     
     ''')
    
    option = input('Escolha uma opção: ')
    return option

# class Banco onde armazena os usuários e as contas e tem os métodos para criar usuários e contas
class Bank:
    def __init__(self):
       self.users = []
       self.accounts = []

    # Criando o método para criar usuário, onde recebe o nome, cpf e data de nascimento do usuário e verifica se o usuário já existe, caso contrário, cria um novo usuário e adiciona na lista de usuários
    def create_user(self, name, cpf, birth_date):
        user = self.find_user(cpf)

        # Verificando se o user ja existe
        if user:
            print('Usuário já existe!')
            return
        
        # Adicionando o novo usuário na lista de usuários
        new_user =  User(name, cpf, birth_date)
        self.users.append(new_user)
        print('Usuário criado com sucesso!')

    # Passando na lista de usuarios para ver se ja existe
    def find_user(self, cpf):
        for user in self.users:
            if user.cpf == cpf:
                return user
        return None
    
    # Criando o método para criar a conta
    def create_account(self, agency, number, cpf):
        user = self.find_user(cpf)

        # Verificando se o usuário existe, caso contrário, não é possível criar a conta
        if not user:
            print('Usuário não encontrado!')
            return
        
        # Criando a conta e adicionando na lista de contas e na lista de contas do usuário
        account = Account(agency, number, user)
        self.accounts.append(account)
        user.accounts.append(account)
        print('Conta criada com sucesso!')


    def find_account(self, number):
        for account in self.accounts:
            if account.number == number:
                return account
        return None

# Criando a classe user para armazenar as informações
class User:
    def __init__(self, name, cpf, birth_date):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date
        self.accounts = []

# Class account para armazenar as informações da conta e os métodos para depositar, sacar e extrato
class Account:
    def __init__(self, agency, number, user, balance=0):
        self.agency = agency
        self.number = number
        self.user = user
        self._balance = balance
    
    # Metodo depositar
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Depósito de R$ {amount:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito inválido!')
    

    # Metodo sacar
    def withdraw(self, amount):
        if amount > self._balance:
            print('Saldo insuficiente!')
        elif amount <= 0:
            print('Valor de saque inválido!')
        else:
            self._balance -= amount
            print(f'Saque de R$ {amount:.2f} realizado com sucesso!')
    
    # Metodo extrato
    def extract(self):
        print(f'Saldo atual: R$ {self._balance:.2f}')



if __name__ == '__main__':

    current_account = None

    bank = Bank()
   

    while True:

        option = menu()

        if option == 'd':
            amount = float(input('Informe o valor do depósito: '))
            current_account.deposit(amount)

        elif option == 's':
            amount = float(input('Informe o valor do saque: '))
            current_account.withdraw(amount)

        elif option == 'e':
            current_account.extract()

        elif option == 'ent':
            current_account = input('Informe o número da conta: ')
            current_account = bank.find_account(current_account)

        elif option == 'cu':
            name = input('Informe o nome do usuário: ')
            cpf = input('Informe o CPF do usuário: ')
            birth_date = input('Informe a data de nascimento do usuário (dd/mm/yyyy): ')
            bank.create_user(name, cpf, birth_date)

        elif option == 'cc':
            agency = input('Informe a agência da conta: ')
            number = input('Informe o número da conta: ')
            cpf = input('Informe o CPF do usuário: ')
            bank.create_account(agency, number, cpf)

        elif option == 'q':
            break

        else:
            print('Opção inválida!')