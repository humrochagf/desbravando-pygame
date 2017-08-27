# -*- coding: utf-8 -*-

import random
import time

import pygame

from game import game_of_life

# plano vazio
SEED = [[0 for _ in range(50)] for _ in range(50)]

# Glider
SEED[23][24] = 1
SEED[24][25] = 1
SEED[25][23] = SEED[25][24] = SEED[25][25] = 1

# Glider gun
# SEED[20][30] = 1
# SEED[21][28] = SEED[21][30] = 1
# SEED[22][18] = SEED[22][19] = SEED[22][26] = SEED[22][27] = SEED[22][40] = SEED[22][41] = 1
# SEED[23][17] = SEED[23][21] = SEED[23][26] = SEED[23][27] = SEED[23][40] = SEED[23][41] = 1
# SEED[24][6]  = SEED[24][7]  = SEED[24][16] = SEED[24][22] = SEED[24][26] = SEED[24][27] = 1
# SEED[25][6]  = SEED[25][7]  = SEED[25][16] = SEED[25][20] = SEED[25][22] = SEED[25][23] = SEED[25][28] = SEED[25][30] = 1
# SEED[26][16] = SEED[26][22] = SEED[26][30] = 1
# SEED[27][17] = SEED[27][21] = 1
# SEED[28][18] = SEED[28][19] = 1

# Rich's p16
# SEED[19][20] = SEED[19][21] = SEED[19][22] = SEED[19][26] = SEED[19][27] = SEED[19][28] = 1
# SEED[20][19] = SEED[20][23] = SEED[20][25] = SEED[20][29] = 1
# SEED[21][19] = SEED[21][23] = SEED[21][25] = SEED[21][29] = 1
# SEED[22][18] = SEED[22][20] = SEED[22][21] = SEED[22][22] = SEED[22][23] = SEED[22][25] = SEED[22][26] = SEED[22][27] = SEED[22][28] = SEED[22][30] = 1
# SEED[23][18] = SEED[23][19] = SEED[23][29] = SEED[23][30] = 1
# SEED[26][22] = SEED[26][23] = SEED[26][22] = SEED[26][25] = SEED[26][26] = 1
# SEED[27][21] = SEED[27][23] = SEED[27][25] = SEED[27][27] = 1
# SEED[28][22] = SEED[28][26] = 1

# Random
# SEED = [[random.choice([0, 1]) for _ in range(50)] for _ in range(50)]

pygame.init()

screen = pygame.display.set_mode((550, 550))


def draw_matrix(matrix):
    '''
    Função para desenhar o plano
    '''

    # preenche a tela de preto
    screen.fill([0, 0, 0])

    # percorre o plano desenhando as células com seus valores
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell:
                # caso a célula esteja viva, a pinte de branco
                pygame.draw.rect(screen, (255, 255, 255),
                                 (11*c, 11*r, 10, 10))


# define a seed como um dos valores de exemplo do começo
seed = SEED

# desenha o estado inicial de nossa seed
draw_matrix(seed)

pygame.display.flip()

# espera por 1 segundo para podermos contemplar o estado de partida
time.sleep(1)

while True:
    # PROCESSAMENTO DE ENTRADA
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        # finaliza o programa caso clique em fechar
        break
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        # finaliza o programa caso pressione a tecla ESC
        break

    # ATUALIZAÇÃO DO JOGO

    # aplica o game of life para processar a geração seguinte
    seed = game_of_life(seed)

    # DESENHO

    # desenha a nova geração na tela
    draw_matrix(seed)

    pygame.display.flip()

    # espera um breve momento antes de partir para o próximo ciclo
    time.sleep(0.05)
