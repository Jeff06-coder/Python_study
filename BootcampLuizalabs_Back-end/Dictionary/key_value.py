pessoa = {"name": "Jeff", "years_old": 30}
print(pessoa)
# criando um dicionário usando as chaves e os valores

pessoa2 = dict(name="Alice", years_old=22)
print(pessoa2)
# Criando um dicionário usando a função dict() e passando os pares chave-valor como argumentos

pessoa["number"] = 123456789
print(pessoa)
# Adicionando um novo par chave-valor ao dicionário pessoa

contatos = {
    "jeff@exemplo.com": {'nome': 'Jeff', 'telefone': '123456789'}
    }
print(contatos)
# Criando um dicionário aninhado, onde a chave é um email e o valor é outro dicionário contendo informações de contato