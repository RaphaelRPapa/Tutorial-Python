# Criando uma lista vazia e adicionando elementos posteriormente
lista_vazia = []
lista_vazia.append("a")
lista_vazia.append("b")
lista_vazia.append("c")
print("Lista após adicionar elementos:", lista_vazia)

# Criando uma lista com elementos de diferentes tipos
lista_mista = [1, "Hello", True, 3.14]
print("Lista com elementos de diferentes tipos:", lista_mista)

# Removendo elementos pelo índice
lista = ["a", "b", "c", "d"]
del lista[2]  # Remove o elemento na posição 2 (o terceiro elemento)
print("Lista após remover o elemento na posição 2:", lista)

# Copiando uma lista
original = [1, 2, 3]
copia = original.copy()  # Também pode ser feito com copia = list(original)
print("Cópia da lista original:", copia)
