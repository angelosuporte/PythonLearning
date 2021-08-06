#Tratamento de exceções

lista = [1, 10]

try:
    arquivo = open('Teste.txt', 'r')
    texto = arquivo.read()
   # divisao = 10 / 0
    numero = lista[3]
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero')
#except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()