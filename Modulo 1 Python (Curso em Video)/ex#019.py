'''
	Exercício #019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome deles e escrevendo o nome do escolhido.
'''

import random  # Biblioteca / Módulo para números ou valores aleatórios

# Lendo o nome dos quatro alunos
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

# Agrupando os nomes em uma lista
lista = [aluno1, aluno2, aluno3, aluno4]

# Sorteando um dos alunos da lista
escolhido = random.choice(lista)   # random.choice - Escolhe um valor aleatório

print('\033[0;36mO aluno que vai apagar o quadro é: {}'.format(escolhido))