# Herança simples
class Veiculo:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def liga_motor(self):
        print("O veiculo está ligando o motor.")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("Honda", "CB500", "preta", 2021)
moto.liga_motor()