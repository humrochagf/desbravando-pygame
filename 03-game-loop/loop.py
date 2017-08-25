# -*- coding: utf-8 -*-

import pygame

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0, 0, 255)
GREEN = (0, 255, 0)
RED =   (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Game Loop')

# variáveis da bola
position_x = 300
position_y = 200
velocity_x = 1
velocity_y = 1

# iniciando o loop de jogo
while True:
    # PROCESSAMENTO DE ENTRADA

    # capturando eventos
    event = pygame.event.poll()
    # caso o evento QUIT (clicar no x da janela) seja disparado
    if event.type == pygame.QUIT:
        # saia do loop finalizando o programa
        break

    # ATUALIZAÇÃO DO JOGO

    # movendo a bola
    position_x += velocity_x
    position_y += velocity_y

    # mudando a direção no eixo x nas bordas
    if position_x > 600:
        velocity_x = -1
    elif position_x < 0:
        velocity_x = 1

    # mudando a direção no eixo y nas bordas
    if position_y > 440:
        velocity_y = -1
    elif position_y < 0:
        velocity_y = 1

    # DESENHO

    # preenchendo o fundo com preto
    screen.fill(BLACK)

    # desenhando a bola
    pygame.draw.ellipse(screen, RED, [position_x, position_y, 40, 40])

    # atualizando a tela
    pygame.display.flip()
