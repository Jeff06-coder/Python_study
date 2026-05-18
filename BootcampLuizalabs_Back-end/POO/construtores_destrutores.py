class Cachorro:
    def __init__(self, nome):
        print("Construtor chamado sempre em primeiro lugar")
        self.nome = nome

    # Executado no final, depois de ser usado o objeto
    def __del__(self):
        print("Destrutor chamado quando o objeto é destruído")
        print(f"{self.nome} foi destruído")

    def latir(self):
        print(f"{self.nome} está latindo: Au au!")


c = Cachorro("Rex")
# Destruindo objeto antes do final
#del c
c.latir()
    
