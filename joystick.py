"""! @brief Controle do personagem por JoyStick """
##
# @file joystick.py
#
# @brief Arquivo responsável pela inicializacao do JoyStick
#
# @author: Claudio Rogerio 02.03.2020
#
# @subsection TODO
#   -
#
# @subsection MAKED
#   - Start
#   - Cima
#   - Baixo
#   - Arma
#

import pygame

def init_joystick():
    '''
    Inicializa o joystick

    Returns:
        Lista de joysticks ativos
    '''

    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    return joysticks
