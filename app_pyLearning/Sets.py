print('Conjuntos')

conjunto = {1, 2, 3, 4, 5, 6, 7}
#adicionando
conjunto.add(8)
#removendo
conjunto.discard(7)
print(conjunto)

print('Union')
conjunto2 = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

print('Instersection')
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

print('Diference')
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca1)
print(conjunto_diferenca2)

print('Difference symmetric')
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)

print('Subset and superset')
conjunto_subset = conjunto.issubset(conjunto2) #Pergunta: o conjunto é subconjunto de conjunto2?
print(conjunto_subset)
conjunto_superset = conjunto2.issuperset(conjunto)
print(conjunto_superset)

print(('List to sets and sets to list'))
lista = ['cachorro', 'gato', 'galinha', 'cachorro', 'galinha']
conjunto_animal = set(lista)
print(conjunto_animal)
lista_animal = list(conjunto_animal)
print(lista_animal)
