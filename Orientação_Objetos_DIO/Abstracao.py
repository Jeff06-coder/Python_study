#Class Pai Abstrata
class Personagem:
    #Função construtora
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    #Método abstrato/subjetivo
    #Faz com que as classes filhas implementem esse método obrigatoriamente
    def atacar(self):
        raise NotImplementedError("Subclasses devem implementar este método")

    def receber_dano(self, dano):
        print(f"{self.nome} recebeu {dano} de dano!")

#Class Filha
class Guerreiro(Personagem):
    def atacar(self):
        print(f"{self.nome} ataca com uma espada!")


#Apresentando o uso das classes
person1 = Guerreiro("Thorin", 5)
person1.atacar()
person1.receber_dano(15)
