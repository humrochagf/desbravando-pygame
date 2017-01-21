# -*- coding: utf-8 -*-

import time

import pygame

# iniciando a biblioteca
pygame.init()

# definindo a tela do tamanho 640x480
screen = pygame.display.set_mode([640, 480])

# escrevendo Olá mundo no titulo da janela
pygame.display.set_caption('Olá mundo')

# preenchendo a tela com a cor preta
screen.fill([0, 0, 0])

# copiando o buffer para a tela
pygame.display.flip()

# esperando 5 segundos antes de finalizar o programa
time.sleep(5)
