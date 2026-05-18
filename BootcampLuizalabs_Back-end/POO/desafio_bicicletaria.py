class Bicicleta:
    def __init__(self, cor, modelo, valor, ano):
      self.cor = cor
      self.modelo = modelo
      self.valor = valor
      self.ano = ano

    # Métodos
    def buzinar(self):
      print("Biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiip!")
    
    def parar(self):
      print("A bicicleta parou.")
    
    def correr(self):
      print("A bicicleta está correndo.")

    # def __str__(self):
       # return f"Bicicleta(cor={self.cor}, modelo={self.modelo}, valor={self.valor}, ano={self.ano})"


    # Método para facilitar a leitura do objeto, ou quando vc quiser ler os atributos da class
    def __str__(self):
        return f"{self.__class__.__name__}: {'; '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

# Objeto
bike = Bicicleta("vermelha", "caloi", 1000, 2020)

bike.buzinar()
bike.parar()
bike.correr()
# Acessando os atributos do objeto
print(bike.cor, bike.modelo, bike.valor, bike.ano)

# Possivel ler apenas com __str__ para facilitar a leitura do objeto
print(bike)