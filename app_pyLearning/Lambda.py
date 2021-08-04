#Exemplo de contador de letras - compare com o MethodExample.py
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'rato', 'gato']
print(contador_letras(lista_animais))

#Exemplo de calculo
# soma = lambda a, b: a + b
# print(soma(5,10))

#Calculadora
Calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,

}
print(type(Calculadora))
soma = Calculadora['soma']
subtracao = Calculadora['subtracao']
multiplicacao = Calculadora['multiplicacao']
divisao = Calculadora['divisao']
print('A soma é: {}'.format(soma(10, 5)))
print('A subtracao é: {}'.format(subtracao(10, 5)))
print('A multipicação é: {}'.format(multiplicacao(10, 5)))
print('A divisão é: {}'.format(divisao(10, 5)))