"""! @brief Nuvens do cenário """
##
# @file nuvens.py
#
# @brief Arquivo responsável pela importacao das imagens de nuvens
# Importacao das nuvens para compor o cenario principal do chrome_rex
# As nuvens sao atualizadas a cada momento
#
# @author Claudio Rogerio 02.03.2020
#
# @subsection TODO
#   - Trovoes
#
# @subsection MAKED
#   - Aleatoriedade
#   - Velocidade das nuvens

import pygame
import numpy as np

nuvem_0 = pygame.image.load( './img/1/nuvens/nuvem_00.png' )
nuvem_0_0 = pygame.transform.rotozoom( nuvem_0, 0, 0.2 )

nuvem_1 = pygame.image.load( './img/1/nuvens/nuvem_01.2.png' )
nuvem_0_1 = pygame.transform.rotozoom( nuvem_1, 0, 0.08 )

nuvem_3 = pygame.image.load( './img/1/nuvens/nuvem_03.png' )
nuvem_0_3 = pygame.transform.rotozoom( nuvem_3, 0, 0.10 )

nuvem_4 = pygame.image.load( './img/1/nuvens/nuvem_06.png' )
nuvem_0_4 = pygame.transform.rotozoom( nuvem_4, 0, 0.2 )

nuvem_6 = pygame.image.load( './img/1/nuvens/nuvem_08.png' )
nuvem_0_6 = pygame.transform.rotozoom( nuvem_6, 0, 0.1 )

nuvens = [ nuvem_0_0, nuvem_0_1, nuvem_0_3, nuvem_0_4, nuvem_0_6 ]
nuvens_total = 5

## pos inicial da nuvem
def get_pos_nuvem( display ):
    return ( display[0]+np.random.randint( -10, 700 ), 10+np.random.randint( -5, 70 ) )

## selecao de nuvens aleatoriamente do total de nuvens e suas posicoes iniciais
def iniciar_nuvens( display ):
    n_nuvens = []

    for i in range( 0, np.random.randint( 2, 4 ) ):
        aux = [ np.random.randint( 0, nuvens_total ) , get_pos_nuvem( display ) ]
        n_nuvens.append( aux )

    for n, item in enumerate( n_nuvens ):
        print( 'nuvens', n, item[0], item[1], n_nuvens[n][1][0], n_nuvens[n][1][1] )

    return n_nuvens
