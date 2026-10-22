'''
	Exercício #033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

num = int(input('Digite um número qualquer: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = max(num, num2, num3)
menor = min(num, num2, num3)

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
