class Estudantes:
    escola = "DIO"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Estudante: {self.nome}, Idade: {self.idade}, Escola: {self.escola}"
    
estudante1 = Estudantes("João", 20)
estudante2 = Estudantes("Maria", 22)

print(estudante1, estudante2)

# Modificando o atributo de classe
Estudantes.escola = "Outra Natural"
estudante1.escola = "Outra Escola"
print(estudante1, estudante2)