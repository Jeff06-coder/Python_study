#Criando o menu de visualização
def menu():
    print("""\n
         [cu] Criar usuário
         [cc] Criar conta
         [ent] Entrar na conta
         [d] Depositar
         [s] Sacar
         [e] Extrato
         [q] Sair
        \n""")
    option = input('Informe a opção desejada: ')
    return option

def users(name, cpf, birth_date, adress):

    pass

def accounts():
    pass

def deposit():
    pass

def withdraw():
    pass

def statement():
    pass

if __name__ == '__main__':

    menu()