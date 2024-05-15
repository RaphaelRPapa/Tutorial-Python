# Criando um dicionário vazio e adicionando itens posteriormente
dicionario_vazio = {}
dicionario_vazio["chave1"] = "valor1"
dicionario_vazio["chave2"] = "valor2"
print("Dicionário após adicionar itens:", dicionario_vazio)

# Criando um dicionário com chaves e valores pré-definidos
dicionario = {"a": 1, "b": 2, "c": 3}
print("Dicionário pré-definido:", dicionario)

# Obtendo as chaves de um dicionário
chaves = dicionario.keys()
print("Chaves do dicionário:", chaves)

# Obtendo os valores de um dicionário
valores = dicionario.values()
print("Valores do dicionário:", valores)

# Mesclando dois dicionários
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionario1.update(dicionario2)
print("Dicionário após mesclar com outro dicionário:", dicionario1)
