# Criando um iterador personalizado que retorna o dobro dos números fornecidos
# feito para ser reutilizado em outros lugares, ele carrega o dado com forme vai passando pela interação
class MeuIterador:
    # Definindo class constructor que recebe uma lista de números e inicializa o índice
    def __init__(self, numeros=list[int]):
        self.numeros = numeros
        self.index = 0

    # Definindo o método __iter__ para retornar o próprio objeto iterador
    def __iter__(self):
        return self
    
    # Definindo o método __next__ para retornar o próximo número dobrado ou levantar StopIteration quando não houver mais números
    def __next__(self):
       
       # Usando try-except para lidar com o caso em que o índice ultrapassa a lista de números, levantando StopIteration para sinalizar o fim da iteração
       try:
            numero = self.numeros[self.index]
            self.index += 1
            return numero * 2
       # Se o índice ultrapassar o comprimento da lista, um IndexError será levantado, e nesse caso, levantamos StopIteration para indicar que a iteração terminou
       except IndexError:
               # Isso faz com que o loop for saiba que a iteração terminou e pare de chamar __next__
               raise StopIteration

# Exemplo de uso do MeuIterador para iterar sobre uma lista de números e imprimir o dobro de cada número
for i in MeuIterador(numeros=[1,2,3,4,5]):
    print(i)