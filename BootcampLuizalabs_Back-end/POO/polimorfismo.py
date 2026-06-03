class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print("O pássaro está voando.")

class Pinguim(Passaro):
    def voar(self):
        print("O pinguim não pode voar.")
        

class Pideoty(Passaro):
    def voar(self):
        super().voar()




def plano_de_voo(obj):
    obj.voar()

passaro = Passaro("Canário")
pinguim = Pinguim("Pinguim")
plano_de_voo(passaro)  # Saída: O pássaro está voando.
plano_de_voo(pinguim)  # Saída: O pinguim não