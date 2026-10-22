'''
	Exercício #031
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.
'''

distancia_km = float(input('Digite a distancia percorrida em Km: '))

if distancia_km <= 200:
    print('O preço da passagem de {} km, vai ser {} reais'.format(distancia_km, (distancia_km * 0.50)))
else:
    print('O preço da passagem de {} km, vai ser {} reais'.format(distancia_km, (distancia_km * 0.45)))
