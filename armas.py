"""! @brief Armas do personagem do jogo Chrome TRex"""
##
# @file armas.py
#
# @brief
# Arquivo com imagens das armas do personagem
#
# @author Claudio Rogerio 02.03.2020
#
# @section TODO
#   - Voar por alguns instantes
#   - Pontuacao precisa de ajustes
#
# @section MAKED
#   - Fogo

import pygame
import numpy as np

ajuda_0 = pygame.image.load('./img/1/fogo/fogo_info_00.png')
ajuda_1 = pygame.image.load('./img/1/fogo/fogo_info_01.png')
ajuda_2 = pygame.image.load('./img/1/fogo/fogo_info_02.png')
ajuda_3 = pygame.image.load('./img/1/fogo/fogo_info_03.png')

ajuda_0 = pygame.transform.rotozoom( ajuda_0, 0, 0.10)
ajuda_1 = pygame.transform.rotozoom( ajuda_1, 0, 0.10)
ajuda_2 = pygame.transform.rotozoom( ajuda_2, 0, 0.10)
ajuda_3 = pygame.transform.rotozoom( ajuda_3, 0, 0.10)

ajuda = [ ajuda_0, ajuda_1, ajuda_2, ajuda_3 ]
idx_ajuda = 0

# ###################################################

fogo_0 = pygame.image.load('./img/1/fogo/fogo_00.png')
fogo_1 = pygame.image.load('./img/1/fogo/fogo_01.png')
fogo_2 = pygame.image.load('./img/1/fogo/fogo_02.png')
fogo_3 = pygame.image.load('./img/1/fogo/fogo_03.png')

fogo_0_0 = pygame.transform.rotozoom( fogo_0, 0, 0.10)
fogo_0_1 = pygame.transform.rotozoom( fogo_1, 0, 0.10)
fogo_0_2 = pygame.transform.rotozoom( fogo_2, 0, 0.10)
fogo_0_3 = pygame.transform.rotozoom( fogo_3, 0, 0.10)

fogo_1_0 = pygame.transform.rotozoom( fogo_0, 0, 0.15)
fogo_1_1 = pygame.transform.rotozoom( fogo_1, 0, 0.15)
fogo_1_2 = pygame.transform.rotozoom( fogo_2, 0, 0.15)
fogo_1_3 = pygame.transform.rotozoom( fogo_3, 0, 0.15)

fogo_2_0 = pygame.transform.rotozoom( fogo_0, 0, 0.20)
fogo_2_1 = pygame.transform.rotozoom( fogo_1, 0, 0.20)
fogo_2_2 = pygame.transform.rotozoom( fogo_2, 0, 0.20)
fogo_2_3 = pygame.transform.rotozoom( fogo_3, 0, 0.20)

fogo = [ [ fogo_0_0, fogo_0_1, fogo_0_2, fogo_0_3 ], [ fogo_1_0, fogo_1_1, fogo_1_2, fogo_1_3 ], [ fogo_2_0, fogo_2_1, fogo_2_2, fogo_2_3 ] ]

def get_pos_fogo( display ):
    return ( 90, display[1]-10 )

fogo_view = fogo[0]
idx_fogo = 0
vel_fogo = 15

## total de balas
balas = 2
## utilizado para ciclos de reutilizacao da arma
recarregar_balas = 0
## controle visual da arma
cont_disparo = 0
