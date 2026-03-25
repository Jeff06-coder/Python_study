contatos = {
    "jeff@exemplo.com": {'nome': 'Jeff', 'telefone': '123456789'}
    }
print(contatos)

copy = contatos.copy()
copy["jeff@exemplo.com"] = {'nome': 'Jeej', 'telefone': 'ERROR'}
print(copy)

print("----------------")

print(dict.fromkeys(["a", "b", "c"], 0))
# Criando um dicionário usando o método fromkeys(), onde as chaves são "a", "b" e "c" e o valor padrão é 0
print(dict.fromkeys(["abc", "valor"]))
# Criando um dicionário usando o método fromkeys(), onde as chaves são "abc" e "valor" e o valor padrão é None

print("----------------")

# print(contatos[chave]) # KeyError
print(copy.get("jeff@exemplo.com"))
print(copy.get("chave"))
# get pode ser usado para acessar o valor de uma chave, e retorna None se a chave não existir, evitando o erro KeyError

print("----------------")

print(contatos.keys())
# O método keys() retorna uma visão das chaves do dicionário

print("----------------")

print(contatos.popitem())
# Remove e mostra oq foi removido

print("----------------")

print(contatos.setdefault("idade", 30))
# O método setdefault() retorna o valor da chave se ela existir, caso contrário, insere a chave com o valor padrão fornecido e retorna esse valor
