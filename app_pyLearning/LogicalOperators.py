a = int(input('First value: '))
b = int(input('Second value: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('An even number was entered')
else:
    print('No even number was entered')

