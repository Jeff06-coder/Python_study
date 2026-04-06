# Criação do menu base
def menu ():
    print('''
          ============MENU==============
         [cu] Criar usuário
         [cc] Criar conta
         [ent] Entrar na conta
         [d] Depositar
         [s] Sacar
         [e] Extrato
         [q] Sair
          ==============================\n''')
    option = input('Escolha uma opção: ')
    return option

# Criando a função de criar usuário para ser possivel usar o banco
def create_user(name, cpf, birth_date, address, list_users):
    
    # Código: Verifica se tem cpf existente na lista de usuários, usa any como indentificador de qualquer "coisa" igual,
    #  é usado um for de uma linha so chamado de compreshension
    if any(user['cpf'] == cpf for user in list_users):
        print("CPF já cadastrado. Não é possível criar usuário.")
        return None
    
    user = {
        'cpf': cpf,
    }

    # Adiciona o usuário à lista de usuários
    list_users.append(user)
    print("Usuário criado com sucesso.")

    return user
    
# Criando a função de criar conta para ser possivel usar o banco
def create_account(user, account_number, accounts):

    # Código: Verifica se o cpf do usuário existe na lista de usuários, se o número da conta já existe na lista de contas e se o cpf do usuário corresponde ao titular da conta.
    for u in list_users:
        # Verifica se o cpf do usuário existe na lista de usuários
        if u['cpf'] != user:
            print("/nERROR: CPF não encontrado. Não é possível criar conta.")
        # Verifica se o número da conta já existe na lista de contas usando any como indentificador de qualquer "coisa" igual, é usado um for de uma linha so chamado de compreshension
        elif any(acc['account_number'] == account_number for acc in accounts):
            print("/nNúmero de conta já existente. Não é possível criar conta.")
        # Verifica se o cpf do usuário corresponde ao titular da conta
        elif u['cpf'] == user:
            account = {
                'account_number': account_number,
                'user': u,
                'balance': 0.0,
                'agency': '0001',
            }
            # Adiciona a conta à lista de contas
            accounts.append(account)
            print("Conta criada com sucesso.")
            break

    return account

# Criando a função de depositar
# Obrigando os parametros antes da "/" a serem declarados em posição
def deposit(account, amount, /):
    # Verificando se valor é positivo ou negativo, se for positivo é adicionado no salto da conta colocada nos parametros
    if amount > 0:
        account['balance'] += amount
        print(f"Depósito de R${amount:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido. O valor deve ser positivo.")

# Criando a função de sacar
# Fazendo todos os parametros depois de "*" serem declarados como nomeados, ou seja, obrigando a declaração do nome do parametro na hora de chamar a função
def withdraw(*, account, amount):
    # Basicamente o mesmo processo do deposito, só que aqui tem a verificação de saldo suficiente para realizar o saque, e se o valor do saque é positivo ou negativo, se for positivo é retirado do saldo da conta colocada nos parametros
    if amount > account['balance']:
        print("Saldo insuficiente para realizar o saque.")
    elif amount <= 0:
        print("Valor de saque inválido. O valor deve ser positivo.")
    else:
        
        account['balance'] -= amount
        print(f"Saque de R${amount:.2f} realizado com sucesso.")

# Criando a função de extrato
def extract(account, cpf):

    for acc in accounts:

        if acc['user']['cpf'] == cpf and acc['account_number'] == account['account_number']:

            print("\n================ EXTRATO ================")
            print(f"Titular: {acc['user']['cpf']}")
            print(f"Saldo: R$ {acc['balance']:.2f}")
            print(f"Limite de saques: {LIMITE_SAQUES}")
            print("==========================================")

        else:
            print("CPF não corresponde ao titular da conta. Não é possível exibir o extrato.")

#
if __name__ == "__main__":


    list_users = []
    LIMITE_SAQUES = 3
    accounts = []

    while True:

        option = menu()

        if option == 'cu':
            name = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            birth_date = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
            address = input("Digite o endereço do usuário: ")
            user = create_user(name, cpf, birth_date, address, list_users)
            

        elif option == 'cc':
            person = input("Digite o CPF do usuário para criar a conta: ")
            c_number = input("Digite o número da conta: ")
            create_account(person, c_number, accounts)
            

        elif option == 'ent':
            pass

        elif option == 'd':
            value = float(input("Digite o valor do depósito: "))
            deposit(accounts[0], value)

        elif option == 's':
            value = float(input("Digite o valor do saque: "))
            withdraw(account=accounts[0], amount=value)

        elif option == 'e':
            number_person = input("Digite o CPF do titular da conta: ")
            extract(accounts[0], number_person)  # Pegando o numero da conta criada e vendo o extrato dela

        elif option == 'q':
            break

        else:
            print("Opção inválida!")

print(list_users, accounts)