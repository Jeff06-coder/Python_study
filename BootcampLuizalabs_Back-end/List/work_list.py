numbers = [1, 30, 12, 13, 67, 89, 50, 26, 16, 40]
pares = []

for number in numbers:
    if number % 2 == 0:
        pares.append(number) # .append faz com que o conteudo seja colocado dentro da outra lista

print(numbers)
print(pares)

# Esse código cria uma lista com números e uma lista sem nada, depois vasculha a lista com números reconhecendo qual é par, assim colocando na outra lista

numbers.extend(pares) # .extend faz com que o conteudo seja colocado dentro da outra lista, mas sem criar uma nova lista dentro da outra, como o .append
print(numbers)  

print(numbers.index(67)) # .index mostra o índice do número que você quer, nesse caso o número 67

print(numbers.pop(12)) # .pop remove o número do índice que você quer, e mostra o número que foi removido

pares.sort(key=lambda x: x) # .sort ordena os números da lista, nesse caso do menor para o maior, e o key=lambda x: x faz com que a ordenação seja feita pelo valor dos números, e não por outro critério, como o tamanho dos números, por exemplo.
print(pares)
numbers.sort(key=lambda x: x, reverse=True) # .sort ordena os números da lista, nesse caso do maior para o menor, e o key=lambda x: x faz com que a ordenação seja feita pelo valor dos números, e não por outro critério, como o tamanho dos números, por exemplo. O reverse=True faz com que a ordenação seja feita do maior para o menor.
print(numbers)