'''
	Exercício #032
Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.
'''

ano = int(input('Digite o ano de nascimento: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))

# Resolução 2
'''
import datetime
ano = int(input('Digite o ano de nascimento: '))

if ano == 0:
    ano = datetime.date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))

'''