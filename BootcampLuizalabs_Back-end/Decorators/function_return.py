

def calculadora(operacao):
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        return a / b

    match operacao:
        case "soma":
            return soma
        case "subtracao":
            return subtracao
        case "multiplicacao":
            return multiplicacao
        case "divisao":
            return divisao
        case _:
            print("Operação inválida")
            return None

print(calculadora("soma")(10, 5))

op = calculadora("subtracao")
print(op(11, 5))