'''
	Exercício #017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa.
'''

import math

cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.sqrt(math.pow(cat_oposto, 2) + (math.pow(cat_adjacente, 2)))
'''
math.pow - Calcula a potenciação de um numero elevado a um expoente. Ex: math.pow(2, 4) = 16

math.sqrt - Calcula a raiz quadrada de um número. Ex: math.sqrt(25) = 5

math.hypot - Calcula a hipotenusa de um cateto oposto e cateto adjacente, sem precisar colocar a fórmula completa

math.ceil - Faz o arredondamento de um número para cima

math.floor - Faz o arredondamento de um número para baixo

math.factorial - Calcula uma fatorial de um número
'''

# hipotenusa = math.hypot(cat_oposto, cat_adjacente)

print('\033[4;35mO valor da hipotenusa é igual a {:.2f}'.format(hipotenusa))