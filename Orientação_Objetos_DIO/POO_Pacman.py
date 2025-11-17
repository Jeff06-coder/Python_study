# Definição da classe FantasmaPacman que é a Class mãe
class FantasmaPacman:
    def __init__(self, nome, cor, movimentacao):
        self.nome = nome
        self.cor = cor
        self.movimentacao = movimentacao

    # Método para apresentar o fantasma
    def apresentar(self):
        print(f"Olá, eu sou o fantasma {self.nome}, minha cor é {self.cor} e meu modo de movimentação é {self.movimentacao}.")

    # Método para mover o fantasma
    def mover(self):
        print(f"{self.nome} está se movendo de forma {self.movimentacao}.")

# Instanciando objetos da classe FantasmaPacman
fantasma1 = FantasmaPacman("Blinky", "Vermelho", "Rápida")
fantasma2 = FantasmaPacman("Pinky", "Rosa", "Estratégica")
fantasma3 = FantasmaPacman("Inky", "Azul", "Imprevisível")

# Apresentando os fantasmas
fantasma1.apresentar()
fantasma2.apresentar()
fantasma3.apresentar()
# Movendo os fantasmas
fantasma1.mover()
fantasma2.mover()
fantasma3.mover()



    
