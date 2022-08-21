"""! @brief Janela inicial do jogo Chrome TRex"""
##
# @file initial.py
#
# @brief
# Arquivo com funcoes de apresentacao do jogo
#
# @author Claudio Rogerio 18.11.2021
#
# @section TODO
#   - Adicionar botoes
#   - Funcao de ajuda
#
# @section MAKED
#   - Botoes especializados

import pygame
import numpy as np

play_off= pygame.image.load('./img/1/initial/button_play_off_4.png')
play_on = pygame.image.load('./img/1/initial/button_play_on_4.png')
play_pr = pygame.image.load('./img/1/initial/button_play_pr_4.png')

play_off= pygame.transform.rotozoom( play_off, 0, 0.45) 
play_on = pygame.transform.rotozoom( play_on, 0, 0.45) 
play_pr = pygame.transform.rotozoom( play_pr, 0, 0.45) 

play = [play_off, play_on, play_pr]

id_play = 0

def get_pos_play( display ):
    return [ int(display[0]/2) -70, int( display[1]/4) ]

