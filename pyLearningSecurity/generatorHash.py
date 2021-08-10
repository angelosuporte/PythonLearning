import hashlib

texto = input('Informe o texto para gerar hash: ')

menu = int(input('''#### MENU - ESOLHA O TIPO DE HASH ####
                1)MDR
                2)SHA1
                3)SHA256
                4)SHA512
                Informe o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print('O hash da string: ', texto, 'é: ', resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print('O hash da string: ', texto, 'é: ', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print('O hash da string: ', texto, 'é: ', resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print('O hash da string: ', texto, 'é: ', resultado.hexdigest())

else:
    print('Aconteceu um erro!')
