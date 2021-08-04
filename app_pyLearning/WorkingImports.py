from ClassExample3 import Televisao
from ClassExample1 import Calculadora
from MethodExample import contador_letras

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

calculadora = Calculadora(10,5)
print(calculadora.soma())

lista = ['cachorro', 'gato', 'elefante']
total_letras = contador_letras(lista)
print(total_letras)

