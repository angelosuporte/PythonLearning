lista = [ 11, 13, 1, 2, 3, 5, 7]
lista_animal = ['camelo', 'serpente', 'abutre']
print(lista_animal[0])

print('criando uma nova lista com os itens multiplicados por 3')
nova_lista = lista_animal * 3
print(nova_lista)

print('Exemplos de soma')
#Exemplo 1
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

#Exemplo 2
# somaLista = sum(lista)
# print(somaLista)

#Exemplo 3
print(sum(lista))

print('Encontrando valor minimo e valor maximo')
print(min(lista))
print(max(lista))

print('Validando(verificando se há) um item na lista')
if 'leao' in lista_animal:
    print('Existe na lista')
else:
    print('Não existe na lista')
    lista_animal.append('leao')
    print('Incluido animal na lista')
    print(lista_animal)

print('Retirando o ultimo item ou um item da lista pela posicao')
lista_animal.pop(1)
print(lista_animal)
print('Retirando um elemento que sei o nome')
lista_animal.remove('abutre')
print(lista_animal)

print('Ordenando e revertendo a lista')
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

print('Contando elementos na lista')
print(len(lista_animal))

print('Trabalhando com tuplas')
tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))

print('Convertendo uma lista em tupla')
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

print('Convertendo a tupla em lista')
lista_num = list(tupla)
print(type(lista_num))
print(lista_num)

