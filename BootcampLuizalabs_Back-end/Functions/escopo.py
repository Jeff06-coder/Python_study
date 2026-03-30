salario = 1000

def calcular_bonus(bonus):
    global salario # falando para function que a variavel de fora serve para aq dentro
    salario += bonus
    print(f"Salário com bônus: {salario}")

calcular_bonus(700)