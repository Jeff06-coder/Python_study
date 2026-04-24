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
Both forms create the dictionary 

(Ambas formas criam o dicionário)

### pessoa["Add_NewKey"] = "Add_NewValue"
Add new value to dictionary

### copy = pessoa.copy()
Exactly copies the dictionary, but being another 

(Copia exatamente o dicionario, mas sendo outro)

### dict.fromkeys(["a", "b", "c"], 0) | dict.fromkeys(["abc", "valor"]) # 0 | # None
Sets the value for everyone in the dictionary 

(Define o valor para todos no dicionário) 

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
To add if it does not exist, if it exists returns the value that is there

(Para adicionar se não existir, se existir retorna o valor que está aí)

### y_dict.update({"KeyName_or_newKeyName": {"new_key": "new_value"}})
Update existing data based on what you enter 

(Atualize os dados existentes de acordo com o que você insere)

### y_d.values()
Return only values

### foud = "what_do_you_want" in your_dict[NameKey_to_search]
Checking if you have the key you want in the dictionary with "in"

(Verificando se você tem a chave desejada no dicionário com "in")

### del your_dict["nameKey"]["phone"]
Remove the values or key placed

### .item()
Take the key and value together and make tuples of them like this

(Junte a chave e o valor e faça tuplas deles assim)

## Functions

### def function (*args, **kwargs)
args = Receives several values ​​and transforms them into tuples 

(Recebe vários valores e transforma em tuplas)

kwargs = Receives several values ​​and transforms them into dictionaries (key: value) 

(Recebe vários valoes e tranforma em dicionários (chave : valor))

### def sep_function (name, date, /, year_old, job)
A / separates in the function which values ​​are received by position and which ones have to be named

(A / separa na função quais valores são recebidos por posição e quais devem ser nomeados)

## Decorators

### def mensagem_para_guilherme(function_mensager)
        return function_mensager("Guilherme")
This function returns a function and can be used within another function, the data generated from the result of this function will serve as a parameter for the other that uses it.

(Esta função retorna uma função e pode ser utilizada dentro de outra função, os dados gerados a partir do resultado desta função servirão de parâmetro para a outra que a utiliza.)

## Iteradores
It is to make a class that reads lists and performs methods using __iter__ and __next__, so that to transform the data into an object, read the next item and only load the data for each pass and then discard it, this is improved in the use of RAM, used for very complex calculations and for reuse.

(É fazer uma class que leia listas e realiza métodos utilizando __iter__ e __next__, para que o for transforme o dado em objeto, leia o próximo item e só carrega o dado por cada passagem e depois descarta, isso melhora na utilização da RAM, usado para calculos muito complexos e para reutilizações.)

The *Generator* is a type of Interator, but simpler and for simpler actions. It carries out the process, capturing the result, delivering it and automatically deleting it when it moves on to the next step.

(O *Gerador* é um tipo de Interador, só que mais simples e para ações mais simples. Ele faz o processo, capitando o resultado, entregando e automaticamente deletando ele quando passa para o próximo passo.)
