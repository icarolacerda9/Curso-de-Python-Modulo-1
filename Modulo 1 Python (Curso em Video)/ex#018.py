'''
	Exercício #018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math

angulo = int(input('Digite o valor de um angulo: '))

# Conversão em radianos

''' 
math.radians - Converte um angulo qualquer de graus p/ radianos    
'''
rad = math.radians(angulo)   # Converte o angulo em graus para radianos

seno = math.sin(rad)        # math.sin -  Calcula o seno de um número
cosseno = math.cos(rad)     # math.cos - Calcula o cosseno de um número
tangente = math.tan(rad)    # math.tan - Calcula a tangente de um número

print('O angulo de {} vai ter o seno igual a {:.1f}'.format(angulo, seno))
print('O angulo de {} vai ter o cosseno igual a {:.1f}'.format(angulo, cosseno))
print('O angulo de {} vai ter o tangente igual a {:.1f}'.format(angulo, tangente))
