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

print(contatos.setdefault("idade", [30, 55, 22, 31, 18]))
# O método setdefault() retorna o valor da chave se ela existir, caso contrário, insere a chave com o valor padrão fornecido e retorna esse valor

print("----------------")

print(copy)
copy.update({"messi@exemplo.com": {'nome': 'Messi', 'telefone': '911654321'}})
print(copy)
# O método update() atualiza o dicionário com os pares chave-valor de outro dicionário, sobrescrevendo os valores existentes para as chaves correspondentes

print("----------------")

print(contatos)
search = 30 in contatos["idade"]
print(search)
# Verificando se o valor 30 está presente no valor associado à chave "idade"

print("----------------")

del contatos["idade"][0]
print(contatos)
# O comando del é usado para remover um item específico
