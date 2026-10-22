'''
	Exercício #013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15 % de aumento.
'''

salario = float(input('Digite o preço de um salario mensal: '))

print('O salario inicial de {} reais, vai ter um aumento de 15 % que vai ser igual a {:.2f} reais'.format(salario, (salario*15/100)))
print('O novo salario aplicado com o aumento vai ser {:.2f} reais'.format(salario + (salario*15/100)))