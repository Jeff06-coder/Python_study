#Super Class
class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} atacando!")

#Sub Class
class Guerreiro(Personagem):

    def atacar(self):
        print(f"{self.nome} atacando com espada!")

class Mago(Personagem):

    def atacar(self,):
        print(f"{self.nome} atacando com magia!")


# Função que demonstra o polimorfismo
def batalha(personagem, inimigo):
    print(f"Batalha entre {personagem.nome} e {inimigo.nome}!")
    inimigo.atacar()
    personagem.atacar()

# Criando instâncias das subclasses
guerreiro = Guerreiro("Aragorn")
mago = Mago("Liliz")

# Iniciando a batalha
batalha(guerreiro, mago)
