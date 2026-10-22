'''
	Exercício #020
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

# Lendo o nome dos quatro alunos
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

# Agrupando os nomes em uma lista
lista = [aluno1, aluno2, aluno3, aluno4]

# Embaralhando a ordem dos alunos na lista
random.shuffle(lista)    # random.shuffle - Vai ordenar/embaralhar uma lista

print('A ordem de apresentação dos trabalhos é:')
print(lista)
