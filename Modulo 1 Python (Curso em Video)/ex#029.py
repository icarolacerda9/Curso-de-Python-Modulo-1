'''
	Exercício #029
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

vel_carro = int(input('Digite a velocidade de um carro: '))

if vel_carro > 80:
    print('Você foi multado. Sua multa vai ser de {} reais'.format((vel_carro - 80) * 7))
else:
    print('Você está dentro do limite de velocidade. ')
