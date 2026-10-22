'''
	Exercício #022
Crie um programa que leia o nome completo de uma pessoa e mostre:

-O nome com todas as letras maiúsculas 
-O nome com todas minúsculas 
-Quantas letras ao todo (sem considerar espaços)
-Quantas letras tem o primeiro nome
'''

nome = str(input('Digite seu nome completo: ')).strip()

# 1. O nome com todas as letras maiúsculas
print(f'Seu nome em maiúsculas é: {nome.upper()}')

# 2. O nome com todas minúsculas
print(f'Seu nome em minúsculas é: {nome.lower()}')

# 3. Quantas letras ao todo (sem considerar espaços)
# Removemos os espaços com replace antes de contar com o len
qtd_letras = len(nome.replace(' ', ''))
print(f'Seu nome tem ao todo {qtd_letras} letras.')

# 4. Quantas letras tem o primeiro nome
# Dividimos o nome em uma lista de palavras e pegamos o primeiro item ([0])
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')