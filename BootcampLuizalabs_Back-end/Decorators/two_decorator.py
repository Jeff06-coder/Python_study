# 
import functools

# Decorador que vai rodar as outras functions
def decorador(funcao):
    # Um decorador para preservar o nome original da função decorada
    @functools.wraps(funcao)
    def executando(*args, **kwargs):
        print("Antes da função ser chamada.")
        resultado = funcao(*args, **kwargs)
        print("Depois da função ser chamada.")
        return resultado

    return executando

# Decorando a função com o decorador
@decorador
def minha_funcao(comParametro, outroParametro):
    print(f"Esta é a minha função com parâmetros: {comParametro}, {outroParametro}")
    return comParametro.upper()

# Chamando a função decorada e colocando ela pra ser um objeto
resltado = minha_funcao("Olá, mundo!", 1000)
print(resltado)
# Mostrando original name da função decorada
print(minha_funcao.__name__)

