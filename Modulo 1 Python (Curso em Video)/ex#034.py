'''
	Exercício #034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de 10 %.

Para os inferiores ou igual, o aumento é de 15 %
'''

salario = float(input('Digite o valor de um salário qualquer: '))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f'O salário inicial de R$ {salario:.2f} terá um aumento de R$ {aumento:.2f}.')
print(f'O novo salário será de R$ {novo_salario:.2f}.')