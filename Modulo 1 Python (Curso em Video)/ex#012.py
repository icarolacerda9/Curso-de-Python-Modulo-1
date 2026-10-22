'''
	Exercício #012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5 % de desconto.
'''

preco = float(input('Digite o preço de um produto qualquer: '))

print('O produto de {} reais, vai ter um desconto de 5 % que vai ser igual a {:.2f} reais'.format(preco, (preco*5/100)))
print('O preço final com o desconto aplicado vai ser {:.2f} reais'.format(preco - (preco*5/100)))