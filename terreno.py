"""! @brief Terreno do jogo Chrome TRex"""
##
# @file terreno.py
#
# @brief Arquivo com imagens do terreno do jogo
#
# @author Claudio Rogerio 02.03.2020
#
# @subsection TODO
#   -
#
# @subsection MAKED
#   -

import pygame
import numpy as np

pygame.init()

DEBUG_terreno = 0

act_terr = False
pos_piso = (1, 0)
## posicao relativa do terreno utilizada para complementar toda a area
pos_rel_x = 1

piso_0 = pygame.image.load('./img/1/piso/piso_00.png').convert()
piso_00 = pygame.transform.rotozoom( piso_0, 0, 0.5).convert()

arv_11_0 = pygame.image.load('./img/1/arvores/acai_0.png')
arv_10 = pygame.transform.rotozoom( arv_11_0, 0, 0.12 )

## importar tipos de arvores
arv_00_0 = pygame.image.load('./img/1/arvores/cacto_0.png')
arv_00 = pygame.transform.rotozoom( arv_00_0, 0, 0.5 )
arv_01 = pygame.transform.flip( arv_00, True, False )
arv_02 = pygame.transform.rotozoom( arv_00_0, 0, 0.4 )
arv_03 = pygame.transform.flip( arv_02, True, False )
arv_04 = pygame.transform.rotozoom( arv_00_0, 0, 0.3 )
arv_05 = pygame.transform.flip( arv_04, True, False )
arv = [ arv_00, arv_01, arv_02, arv_03, arv_04, arv_05, arv_10 ]

def get_pos_arv( display ):
    return (display[0]+10, display[1]-85+np.random.randint(-2, 3) )


def update_terreno( cenario, display, vel_piso, act_terr, status, direction ):
    global pos_piso
    global piso_00

    if act_terr and not status :
        ## dimensao da imagemm
        w = int( piso_00.get_rect().width )

        ## posicao relativa ao tamanho da imagem
        pos_rel_x = int( pos_piso[0] ) % w
        cenario.blit( piso_00, ( pos_rel_x - w, pos_piso[1] ) ) #pos inicial

        if pos_rel_x < display[0]:
            cenario.blit( piso_00, ( pos_rel_x, pos_piso[1] ) ) #pos final

        if DEBUG_terreno:
            print( 'Posicoes', pos_rel_x - w, pos_rel_x, w)
        if direction == True:
            pos_piso = ( (pos_piso[0]-vel_piso ), pos_piso[1] ) # atualizacao de posicao
        else:
            pos_piso = ( (pos_piso[0]+vel_piso ), pos_piso[1] )
    else:
        pos_piso = ( 0, display[1]-60 )
        cenario.blit( piso_00, ( pos_piso ) )    #pos final


def update_arvore( cenario, display, pos_arv, vel_arv, act_arv, arv_type, status, direction ):

    # atualiza posicao arvore
    if act_arv:
        if direction:
            pos_arv = ( pos_arv[0]-vel_arv, pos_arv[1] )
        else:
            pos_arv = ( pos_arv[0]-vel_arv+1, pos_arv[1] )
        if pos_arv[0] < -30.0:
            act_arv = False
    # importa nova posicao
    else:
        if np.random.randint(0, 10) > 7:
            act_arv = True
            pos_arv = get_pos_arv( display )
            arv_type = np.random.randint(0, len(arv))   # qual arvore

            ## unir arvores menores com 2 ou 3
            if arv_type == 4 or arv_type == 5 :
                pos_arv = (pos_arv[0], pos_arv[1]+5 )

            ## igual ao ultimo indice, arvore de acai
            if arv_type == len(arv)-1:
                pos_arv = (pos_arv[0], pos_arv[1]-17)

    ## update position
    if status:
        cenario.blit( arv[arv_type], ( pos_arv ) )
        ## add arvores pequenas
        if arv_type == 4:
            cenario.blit( arv[3], ( pos_arv[0]-20, pos_arv[1] +4 ) )
            cenario.blit( arv[5], ( pos_arv[0]-30, pos_arv[1] +2 ) )
        ## add arvores menores
        if arv_type == 5:
            cenario.blit( arv[2], ( pos_arv[0]-18, pos_arv[1] +3 ) )
            cenario.blit( arv[4], ( pos_arv[0]-32, pos_arv[1] +1 ) )

    return pos_arv, act_arv, arv_type
