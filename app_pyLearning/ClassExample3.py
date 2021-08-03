class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal += 1
    def diminui_canal(self):
        self.canal -= 1

televisao = Televisao()

print('Está ligada? {}'.format(televisao.ligada))
print('Por favor, aperte o botão Power!')
televisao.power()#<---aperte
print('Está ligada? {}'.format(televisao.ligada))
print('Está em qual canal? Precisamos testar o canal 4 e o canal 7')
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
print('Os canais estão Ok')
print('Ótimo, agora pode desligar por favor!')
televisao.power()#<---aperte
print('Esta ligada? {}'. format(televisao.ligada))
print('Teste da tv OK')