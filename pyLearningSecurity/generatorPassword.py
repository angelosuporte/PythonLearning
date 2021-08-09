import random
import string

tamanho = int(input('Informe a quantidade de caracteres que deseja na senha: '))

chars = string.ascii_letters + string.digits + 'Senha a ser gerada'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
