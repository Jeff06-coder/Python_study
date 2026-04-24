# Geradores são uma forma de criar iteradores de maneira mais simples e eficiente. 
# Eles permitem que você crie uma sequência de valores sob demanda, em vez de armazenar todos os valores na memória de uma vez.
# Isso é especialmente útil quando você está lidando com grandes conjuntos de dados ou quando a geração dos valores é computacionalmente cara.
def meu_gerador(numeros: list[int]):
    # yield seria o retiurn, mas faz entender que ele pega o dado, devolve e joga fora
    for num in numeros:
        yield num * 2

for i in meu_gerador(numeros=[3,5,7,8]):
    print(i)