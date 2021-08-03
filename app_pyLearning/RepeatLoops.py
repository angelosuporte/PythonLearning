# for x in range(100):
#     print(x)


#Descobrir se um número é um número primo

# a = int(input('Informe o número: '))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2 :
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))


#-->Descobrir os números primos até um número informado

# a = int(input('Informe o número: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, a):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)
#------------------------------------------------------
a = 0
while a <=10:
    print(a)
    a += 1