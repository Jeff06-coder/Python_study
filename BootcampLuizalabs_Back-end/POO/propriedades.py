class Foo:
    def __init__(self, x=None):
        self._x = x

    # Para retornar o valor de x, usamos o decorador @property
    @property
    def x(self):
        return self._x or 0
    
    # Para modificar o valor de x, usamos o decorador @x.setter
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)  # Acessando o valor de x usando o método
foo.x = 20  # Modificando o valor de x usando o método 
print(foo.x)  # Acessando o valor de x novamente para verificar a modificação
del foo.x  # Deletando o valor de x usando o método
print(foo.x)  # Acessando o valor de x após deletar para verificar a modificação