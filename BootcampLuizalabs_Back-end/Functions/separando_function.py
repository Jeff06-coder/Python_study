def separados(carro, ano, marca, /, motor, combustivel):
    print(f"Carro: {carro}")
    print(f"Ano: {ano}")
    print(f"Marca: {marca}")
    print(f"Motor: {motor}")
    print(f"Combustível: {combustivel}")

separados("Fusca", 1980, "Volkswagen", motor="1.6L", combustivel="Gasolina")
# A barra (/) é usada para indicar que os parâmetros anteriores a ela são posicionais, ou seja, devem
# ser passados na ordem correta e não podem ser nomeados. Já os parâmetros após a barra podem ser passados como argumentos nomeados,
# permitindo maior flexibilidade na chamada da função.