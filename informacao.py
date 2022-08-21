'''
@claudiorogerio: 10.03.21

Importacao das nuvens para compor o cenario principal do chrome_rex
As nuvens sao atualizadas a cada momento
'''

import pygame
import numpy as np

pygame.init()

font = pygame.font.Font('font/joystix monospace.ttf', 10)

text = font.render('Pressione espaço para rodar a roleta...', True, color2 )
cenario.blit( text, (10, 30) )
