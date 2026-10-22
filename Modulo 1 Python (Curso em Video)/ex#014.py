'''
	Exercício #014
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

c = float(input('Digite a temperatura em  °C: '))

print('\033[4;36mA temperatura de {} °C corresponde a {:.1f} °F'.format(c, (c*9/5) + 32))