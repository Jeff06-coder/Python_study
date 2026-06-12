# Biblioteca para criar classes abstratas
from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    # Obriga as classes filhas a implementarem os métodos da classe pai, ou seja, a classe abstrata.
    @abstractmethod
    def ligar(self):
        print("Ligando o controle remoto")

    @abstractmethod
    def desligar(self):
        print("Desligando o controle remoto")

    # O property é um decorador que transforma um método em um atributo, ou seja,
    # ele permite que você acesse o método como se fosse um atributo, sem precisar chamar o método com parênteses
    @property
    def volume(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando o controle remoto")

    def desligar(self):
        print("Desligando o controle remoto")

    @property
    def volume(self):
        return "Aumentando o volume da TV"

controle = ControleTV()
print(controle.volume)

controle = ControleTV()
controle.ligar()
controle.desligar()