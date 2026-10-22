''' 	
            Exercício #004
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações 
possíveis sobre ele.
'''

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))   # Mostra o tipo daquele valor
print('Só tem espaços? ', a.isspace())      # Mostra se tem espaços
print('É um número? ', a.isnumeric())       # Mostra se é um número ou tem apenas números
print('É alfabético? ', a.isalpha())        # Mostra se é alfabetico
print('É alfanumérico? ', a.isalnum())      # Mostra se é alfanúmerico ou tem letras e numeros
print('É maiusculo? ', a.isupper())          # Mostra se é Maiusculo
print('É maiusculo? ', a.islower())          # Mostra se é Minusculo
print('Está capitalizada? ', a.istitle())    # Mostra se está Capitalizada
