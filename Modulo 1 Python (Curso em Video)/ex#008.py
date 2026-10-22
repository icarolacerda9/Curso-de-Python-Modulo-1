'''
	Exercício #008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

a = float(input('Digite um valor em metros: '))

print('\033[0;31;40mO valor {} em centimetros é igual a {} centimetros'.format(a, a*100))
print('\033[0;31;40mO valor {} em milimetros é igual a {} milimetros'.format(a, a*1000))