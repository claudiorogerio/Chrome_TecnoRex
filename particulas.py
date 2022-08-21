"""! @brief Clima do cenario do chrome TREX"""

##
# @file particulas.py
#
# @brief Arquivo responsavel por importar o clima para o cenario do jogo
#
# @section Descrição
# Este arquivo possui informacoes de rendedizacao de chuva, raio, neve e nublado
#
# @author Claudio Rogerio 15.03.2020
#
# @subsection TODO
#   - Raios
#   - Neve
#   - Ensolarado
#
# @subsection MAKED
#   - Chuva

import pygame
import numpy as np

def create_particulas( total, display ):
    '''
    Cria particulas com referencias para a dimensao 2D: x e y

    Args:
        total: numero de particulas

    Returns:
        Array de Posicoes iniciais 2D de cada particula
    '''

    return np.random.randint( -40, display[0]-10, total ), np.random.randint( -150, 20, total )


def update_particulas( cenario, modelo, partc_x, partc_y, color ):
    '''
    Desenha particulas e atualiza sua posicao

    Args:
        cenario: area de renderizacao
        modelo: tipo de particula
        partc_x: posicao no eixo da abscissa da particula
        partc_y: posicao no eixo da ordenada da particula
        update: True/False para atualizar posicionamento da particula

    Returns:
        Posicao atualizada da particula
    '''
    ## Atualiza ou mantem a posicao das particulas

    update_part = True
    #new_x = part_x
    #new_y = part_y
    if np.random.randint(0,2) > 0:
        update_part = True

    if update_part:
        if modelo is 'chuva':
            x,y = np.random.randint( 1, 4, len(partc_x) ), np.random.randint( 4, 7, len(partc_y) )
        partc_x += x
        partc_y += y

    color = (color[0]+7, color[1]+7, color[2]+7 )
    for p in range( len(partc_x) ):
        ## modifica cor da particula
        #color = (70, np.random.randint( 1, 200), 70)
        ## desenha particula em nova posicao
        pygame.draw.line( cenario, color, (partc_x[p], partc_y[p]), (partc_x[p]+1, partc_y[p]+2 ), 1 )
        #pygame.draw.rect( cenario, color, pygame.Rect( partc_x[p], partc_y[p], 1, 5 ), 2 )

    ## retorna a nova posicao 2D
    return partc_x, partc_y, color



# ################## nao utilizado
def draw_particulas( cenario, part_x, part_y, update ):
    '''
    Desenha particulas e atualiza sua posicao

    Args:
        part_x: posicao no eixo da abscissa da particula
        part_y: posicao no eixo da ordenada da particula
        update: True/False para atualizar posicionamento da particula

    Returns:
        Posicao atualizada da particula
    '''

    new_x = part_x
    new_y = part_y
    if update:
        x,y = np.random.randint( -2, 2, len(part_x) ), np.random.randint( -7, 10, len(part_y) )
        new_x += x
        new_y += y

    for p in range( len(new_x) ):
        ## modifica cor da particula
        color = (70, np.random.randint( 1, 200), 70)
        ## desenha particula em nova posicao
        pygame.draw.rect( cenario, color, pygame.Rect( new_x[p], new_y[p], 1, 3 ), 2 ) #fazer teste aqui

    ## retorna a nova posicao 2D
    return new_x, new_y, cor
