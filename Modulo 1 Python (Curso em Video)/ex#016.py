'''
	Exercício #016
Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex: Digite um numero: 6127
O numero 6.127 tem a parte inteira 6.
'''

import math  # Principal biblioteca / Módulo para funções matematicas 
# outra maneira de colocar uma função de uma biblioteca / método qualquer é digitar: from math import trunc

num = float(input('Digite um numero real: '))

num_trunc = math.trunc(num)   # O metodo trunc permite truncar o numero real para inteiro

print('O número {} tem a parte inteira igual a {}'.format(num, num_trunc))