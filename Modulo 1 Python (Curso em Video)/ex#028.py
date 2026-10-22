'''
	Exercício #028
Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
import time

computador = random.randint(0, 5)

print('-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar: ')

num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)

if num == computador:
	print('Você venceu')
else:
	print('Você perdeu. Você colocou {} e eu pensei em {}'.format(computador, num))

