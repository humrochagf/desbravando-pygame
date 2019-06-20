# -*- coding: utf-8 -*-


def cell_check(section):
    '''
    Executa as regras do game of life em um recorte 3x3 para
    saber o estado da célula central
    '''
    # contador de vizinhos
    neighbours = 0
    # referência para o centro do recorte
    center = section[1][1]

    # somando todos os elementos do grupo
    for row in section:
        for cell in row:
            neighbours += cell

    # removendo o valor da célula central para que sobre somente
    # a soma dos vizinhos
    neighbours -= center

    # aplicando as regras do game of life
    # note que a regra dois não precisa ser ativamente aplicada, pois
    # ela não altera o estado da célula avaliada
    if neighbours <= 1:
        # menos de dois vizinhos a célula central morre por baixa população
        center = 0
    elif neighbours == 3:
        # exatamente três a célula nasce por reprodução
        center = 1
    elif neighbours >= 4:
        # mais que três a célula morre de super população
        center = 0

    # retorna o valor da célula central
    return center


def get_section(matrix, row, col):
    '''
    Extrai um recorte 3x3 em um plano tratando as extremidades do plano
    como células sempre mortas
    '''
    # monta um plano 3x3 somente com células mortas para fazer uma cópia
    # da área a ser analizada
    section = [[0 for _ in range(3)] for _ in range(3)]

    # percorre as redondezas da célula de posição row x col
    # copiando seu valor para section
    for sec_r, r in enumerate(range(row-1, row+2)):
        for sec_c, c in enumerate(range(col-1, col+2)):
            section[sec_r][sec_c] = matrix[r % 50][c % 50]

    # devolve o recorte 3x3 do plano
    return section


def game_of_life(seed):
    '''
    Recebe uma seed de um plano 50x50 executa o game of life e devolve
    a geração seguinte
    '''
    # cria um plano vazio para armazenar a nova geração pois não podemos
    # operar diretamente na geração corrente para não gerar efeito colateral
    next_gen = [[0 for _ in range(50)] for _ in range(50)]

    # percorre o plano tirando recortes 3x3 da vizinhança da célula central
    # e os avaliando para descobrir a geração seguinte de cada célula
    for r, row in enumerate(seed):
        for c, col in enumerate(row):
            next_gen[r][c] = cell_check(get_section(seed, r, c))

    # devolve a geração seguinte
    return next_gen
