'''
	Exercício #010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ele pode comprar.
Considere US$ 1,00 = R$ 3,27
'''

total_dinheiro = float(input('Digite seu valor total em reais: '))

print('\033[4;33mEstando com {} reais, convertendo em dolares voce tem {:.2f} dolares'.format(total_dinheiro, total_dinheiro / 3.27))