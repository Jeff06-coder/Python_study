def mensagem(nome):
    print("Mensagem enviada com sucesso!")
    return f"Olá {nome}!"

def decorador(funcao, nome):
    print("Executando o decorador...")
    return funcao(nome)

decorador(mensagem, "Luizalabs")