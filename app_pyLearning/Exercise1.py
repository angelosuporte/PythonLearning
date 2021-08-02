a = int(input('Primeiro bimestre: '))
if a > 10:
    int(input('Você digitou um número errado. Digite novamente: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    int(input('Você digitou um número errado. Digite novamente: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    int(input('Você digitou um número errado. Digite novamente: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    int(input('Você digitou um número errado. Digite novamente: '))

media = ( a + b + c + d ) / 4

print('Média: {}'.format(media))
