'''
	Exercício #007
Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre a sua média.
'''

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = ((nota_1 + nota_2) / 2)

print('\033[1;34mA média de {} e {} é igual a {}'.format(nota_1, nota_2, media))