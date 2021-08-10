import itertools

texto = input('Informe a string a ser permutada: ')
resultado = itertools.permutations(texto, len(texto))

for i in resultado:
    print(''.join(i))