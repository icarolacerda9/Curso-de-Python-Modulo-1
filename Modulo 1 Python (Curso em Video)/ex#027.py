'''
	Exercício #027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

nome_completo = str(input('Digite o nome completo: ')).strip().split()

print(nome_completo)
print('primeiro = ', nome_completo[0])
print('último = ', nome_completo[-1])

