'''
	Exercício #035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

a = int(input('Digite o valor de comprimento 1 do triângulo: '))
b = int(input('Digite o valor de comprimento 2 do triângulo: '))
c = int(input('Digite o valor de comprimento 3 do triângulo: '))

# Verificando a condição de existência do triângulo
if (a < b + c) and (b < a + c) and (c < a + b):
  print("Os comprimentos podem formar um triângulo.")

  # Classificação opcional do tipo de triângulo
  if a == b == c:
    print("Tipo: Triângulo Equilátero (3 lados iguais)")
  elif a == b or b == c or a == c:
    print("Tipo: Triângulo Isósceles (2 lados iguais)")
  else:
    print("Tipo: Triângulo Escaleno (3 lados diferentes)")
else:
  print("Os comprimentos NÃO podem formar um triângulo.")