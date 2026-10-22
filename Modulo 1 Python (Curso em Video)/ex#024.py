'''
	Exercício #024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

cidade = input('Digite o nome de uma cidade: ').strip()

# Converte para maiúsculas e verifica se começa com "SANTO"
comeca_com_santo = cidade.upper().startswith('SANTO')

print(f'A cidade começa com "SANTO"? {comeca_com_santo}')