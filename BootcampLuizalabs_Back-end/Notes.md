# Methods of Python

## String

### .strip() | .lstrip() | .rstrip()
Remove all space stringh | Remove left space stringh | Remove right space stringh

### .upper() | .lower() | .title()
Capitalize stringh | Lowercase stringh | Correctly put stringh

(Capitalizar stringh | Stringh minúscula | Coloque stringh corretamente)

### .center(10, "$")
Center stringh and fill spaces with whatever you want

(Centralizar stringh e preencher espaços com o que você quiser)

### ".".join(var)
Keep putting it for each item ".", type a for (The point can be changed)

(Vai colocando a cada item ".", tipo um for (O ponto pode ser trocado))

### stringName[:5:2]  # sr
Using the string like this makes only the requested characters appear, the numbers are like selected vectors and each character is the value in the vector (The last one is used to "skip" certain spaces)

(Usar a string assim faz aparecer apenas os caracteres solicitados, os números são como vetores selecionados e cada caractere é o valor do vetor (O último é usado para "pular" determinados espaços))

### multiple_string = f''' {name} '''
In addition to preserving the structure of the string placed, it is possible to use another string within it

(Além de preservar a estrutura do string colocado, é possível utilizar outra string dentro dela)

## List

### .copy
Copies the list but with different "addresses" (Copia a lista mas com "endereços" diferentes)

### .count
Count the elements

### .append
Add element to list

### .extend
Combine one list with another

### .index | .reverse
Find the location of the item | Invert the data

### .pop | .remove
Remove the object by placing its index | Remove the object by placing its name

### .sort() | .len(list)
Sort the list (Ordena a lista) | To see the size of the list

## Tuple

### tuple("Hello", 1, 2, 3) | or | tupleVar = ("rice", "beans", "fruit")
It is the value of a list that cannot be changed

## Dictionary

### pessoa {"Key": "value"} | or | pessoa = dict(key="value")
Both forms create the dictionary (Ambas formas criam o dicionário)

### pessoa["Add_NewKey"] = "Add_NewValue"
Add new value to dictionary

### copy = pessoa.copy()
Exactly copies the dictionary, but being another (Copia exatamente o dicionario, mas sendo outro)

### dict.fromkeys(["a", "b", "c"], 0) | dict.fromkeys(["abc", "valor"]) # 0 | # None
Sets the value for everyone in the dictionary (Define o valor para todos no dicionário) 

### your_dict.get("KeyName")
Returns the key value or None if it finds nothing (you can enter a value for it to return if it finds nothing)

Retorna valor da chave ou None se não encontrar nada (pode-se colocar um valor para ele retornar se não achar nada)

### your_dict.keys()
Shows existing keys

### your_dict.pop("KeyName", {})
Remove the key or return the value entered if there is no key ({})

Remova a chave ou volta o valor informado se não houver a chave ({})

### your_dict.popitem()
Remove items in order

### your_dict.setdefaoult("KeyName", "Value")
