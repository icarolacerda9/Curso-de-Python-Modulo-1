'''
	Exercício #025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = input('Digite o nome de uma pessoa: ').strip()

tem_silva = 'SILVA' in nome.upper()

print(f'O nome da pessoa tem "SILVA"? {tem_silva}')