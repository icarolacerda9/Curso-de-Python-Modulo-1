'''
	Exercício #021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
'''
Para o código funcionar, basta baixar a biblioteca pygame no terminal. 

Com isso, basta seguir este caminho: Terminal > New Terminal > digitar pip install pygame > tecla enter
'''


import pygame  # Biblioteca / Módulo para criação de jogos e músicas
import time

# Inicializa apenas o módulo de áudio (mais rápido e limpo)
pygame.mixer.init()

# Carrega o seu arquivo MP3 (Escolhi a música Remember Summer Days da Anri, um classico do City Pop)
pygame.mixer.music.load('Anri- Remember Summer Days.mp3')

# Inicia a reprodução
pygame.mixer.music.play()

print("Tocando 'Remember Summer Days'... Pressione Ctrl+C para parar.")

# Mantém o programa aberto enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)

