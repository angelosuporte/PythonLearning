import hashlib

resultado = hashlib.md5(b'Python')
# b vai converter em bytes

print('O hash da string é: ', resultado.hexdigest())