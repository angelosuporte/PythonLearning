import time
from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print('Carro1: ', piloto, trajeto)
        trajeto += velocidade
        time.sleep((0.5))
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))

t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[2, 'Maquina'])

t_carro1.start()
t_carro2.start()
