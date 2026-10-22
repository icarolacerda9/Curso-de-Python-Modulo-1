'''
	Exercício #011
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))

print('A largura de {}m e altura {} m tem uma área igual a {:.3f} metros quadrados.\n'.format(largura, altura, largura * altura)) 
print('Para pintar essa parede, você precisara de {:.3f} litros de tinta'.format(largura * altura / 2))

