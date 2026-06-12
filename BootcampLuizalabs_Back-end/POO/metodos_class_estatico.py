class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Quando vc quer usar no metodo informações da class
    @classmethod
    # CLS para n precisar definir valores usando Pessoa().metodo(), pode se usar Pessoa.metodo()
    def criar_apartir_data(cls, nome, data_nascimento):
        idade = 2024 - data_nascimento
        return cls(nome, idade)
    
    # Quando vc quer usar o metodo sem precisar de informações da class, ou seja, sem usar self ou cls
    @staticmethod
    def calcular_idade(money):
        return 1999 - money
    
p = Pessoa("João", 30)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data("Maria", 1990)
print(p2.nome, p2.idade)

idade_calculada = Pessoa.calcular_idade(1990)
print(idade_calculada)