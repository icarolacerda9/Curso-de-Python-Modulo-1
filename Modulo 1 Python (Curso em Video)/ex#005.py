'''
	Exercício #005
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

# Resolução 1
num = int(input('Digite um número: '))

sucessor = num + 1
antecessor = num - 1

print('O sucessor de {} é {}'.format(num, sucessor))
print('O antecessor de {} é {}'.format(num, antecessor))

# Resolução 2
num = int(input('Digite um número: '))

print('O sucessor de {} é {}'.format(num, num+1))
print('O antecessor de {} é {}'.format(num, num-1))