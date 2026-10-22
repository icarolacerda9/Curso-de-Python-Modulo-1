'''
	Exercício #015
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

dias = int(input("Digite quantos dias vc alugou o carro: "))
distancia = float(input("Digite quantos km vc andou no total: "))
pago = dias * 60

print('\033[0;33;40mO total a pagar é de R${:.2f}'.format(pago))
