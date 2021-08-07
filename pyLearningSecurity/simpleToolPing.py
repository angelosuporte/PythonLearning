import os

print('#' * 100)

ip_or_host = input('Informe o ip ou host para verificação: ')

print('-' * 100)
os.system('ping -n 6 {}'.format(ip_or_host))

print('-' * 100)
