a = int(input('First  value: '))
b = int(input('Second value: '))
c = int(input('Third  value: '))

if a > b and a > c:
    print('The largest number is: {}'.format(a))
elif b > a and b > c:
    print('The largest number is: {}'. format(b))
else:
    print('The largest number is: {}'. format(c))

print('Finished program')