"""! @brief Personagem principal do jogo Chrome TRex"""
##
# @file personagem.py
#
# @brief Arquivo com imagens do personagem principal
#
# @section Descrição
# O arquivo é responsável pela importacao das imagens utilizadas como animações do personagem TREX
#
# @author Claudio Rogerio 02.03.2020
#
# @subsection TODO
#   - Voar
#
# @subsection MAKED
#   - Movimentacao de pulo
#   - Movimentacao para baixo


import pygame

## importar imagens do personagem
t_rex_0 = pygame.image.load('./img/1/rex_01.0.1.png')
t_rex_1 = pygame.image.load('./img/1/rex_01.1.1.png')
t_rex_2 = pygame.image.load('./img/1/rex_01.2.1.png')
t_rex_3 = pygame.image.load('./img/1/rex_01.2.2.png') # perde

# redimensionamento da imagem
t_rex_0 = pygame.transform.rotozoom( t_rex_0, 0, 0.15)
t_rex_1 = pygame.transform.rotozoom( t_rex_1, 0, 0.15)
t_rex_2 = pygame.transform.rotozoom( t_rex_2, 0, 0.15)
t_rex_3 = pygame.transform.rotozoom( t_rex_3, 0, 0.15)
t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]

## movimentacao para trás
t_rex_0_180 = pygame.transform.flip( t_rex_0, True, False )
t_rex_1_180 = pygame.transform.flip( t_rex_1, True, False )
t_rex_2_180 = pygame.transform.flip( t_rex_2, True, False )
t_rex_3_180 = pygame.transform.flip( t_rex_3, True, False )

## para baixo
t_rex_4 = pygame.image.load('./img/1/rex_02.0.png') # perde
t_rex_5 = pygame.image.load('./img/1/rex_02.1.png') # perde
t_rex_4 = pygame.transform.rotozoom( t_rex_4, 0, 0.4 )
t_rex_5 = pygame.transform.rotozoom( t_rex_5, 0, 0.4 )

## funcao que retorna a posicao inicial do Personagem
def get_pos_rex( display ):
    return ( 50, display[1]-100 )

## velocidade de pulo
direcao = 15

## index da ordem de renderizacao da imagem do personagem
idx_rex = 0
