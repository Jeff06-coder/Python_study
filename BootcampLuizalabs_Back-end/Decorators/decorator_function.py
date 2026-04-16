def meu_decorador(funcao):
    def fazendo():
        print("Antes da função ser chamada.")
        funcao()
        print("Depois da função ser chamada.")

    return fazendo

def minha_funcao():
    print("Esta é a minha função.")

minha_funcao()

decorated_function = meu_decorador(minha_funcao)
decorated_function()