# Heranla multipla
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")


class Mamifero(Animal):
    def __init__(self, quantidade_leite, **kwargs,):
        super().__init__(**kwargs)
        self.quantidade_leite = quantidade_leite
    
        print(f"O {self.nome} tem {self.quantidade_leite} litros de leite.")

class Ave(Animal):
    def __init__(self, asas, **kwargs):
        super().__init__(**kwargs)
        self.asas = asas

        print(f"O {self.nome} tem {self.asas} asas.")

class Cachorro(Mamifero):
    pass

class Ornintorrinco(Mamifero, Ave):
    pass

cachorro = Cachorro(nome="Rex", quantidade_leite=5)
cachorro.comer()


doido = Ornintorrinco(nome="Perry", asas=2, quantidade_leite=3)
doido.comer()
doido.dormir()
