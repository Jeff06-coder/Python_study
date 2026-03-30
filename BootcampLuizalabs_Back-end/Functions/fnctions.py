def somar (a, b):
    return a + b

def function(a, b, f):

    resultado = f(a, b)
    print(f"O resultado da função é: {resultado}")

function(5, 3, somar)
# A função "function" recebe dois números (a e b) e uma função (f) como argumentos. Ela chama a função f, passando a e b como parâmetros,
# e imprime o resultado. No exemplo, a função "somar" é passada como argumento, então o resultado será a soma de 5 e 3, que é 8.

OP = somar

print(OP(5, 3))
# A variável OP é atribuída à função "somar". Isso significa que OP agora é uma referência à função "somar". Quando chamamos OP(5, 3),
# estamos efetivamente chamando a função "somar" com os argumentos 5 e 3, o que resulta em 8.