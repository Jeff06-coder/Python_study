#Class mãe
class Personagem:
    #Function construtora, onde define os atributos da classe
    def __init__(self, nome, vida):
        self.vida = vida
        self.nome = nome
    
    def atacar(self):
        print(f"{self.nome} está atacando!")

#Class filha
class Guerreiro(Personagem):
    #Function construtora da class filha
    def __init__(self, nome, vida, arma):
        #Chama o construtor da class mãe
        super().__init__(nome, vida)
        #Define o atributo específico da class filha
        self.arma = arma
    #Sobrescreve o método atacar da class mãe
    def atacar(self):
        print(f"{self.nome}, o guerreiro, está atacando com a arma {self.arma}!")

#Instancia um objeto da class mãe
personagem1 = Personagem("Aragorn", 100)
personagem1.atacar()
#Instancia um objeto da class filha
guerreiro1 = Guerreiro("Boromir", 120, "Espada")
guerreiro1.atacar()