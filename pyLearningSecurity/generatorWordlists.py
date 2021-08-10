import itertools

resultado = itertools.permutations('abcdf', 3)

for i in resultado:
    print(''.join(i))