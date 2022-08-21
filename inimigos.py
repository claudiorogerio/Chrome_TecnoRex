"""! @brief Inimigos do jogo Chrome TRex"""
##
# @file inimigos.py
#
# @brief Arquivo com imagens ds inimigos estaticos e dinamicos
#
# @section Descrição
# O arquivo é responsável pela importacao das imagens utilizadas como animações
# dos inimigos do jogo
#
# @author Claudio Rogerio 02.03.2020
#
# @subsection TODO
#   - Objetos estaticos
#   - Movimentacao de ir e vir do helicop
#
# @subsection MAKED
#   - Pipira
#   - Visagem
#   - Helicop
#   - Balas do helicop

import pygame
import numpy as np

def get_pos_pipira( display ):
#    print( 'pos pipira' )
    if np.random.randint(0,10) > 7: 
        return ( display[0]+60, display[1]-100-25 )
    else: 
        return ( display[0]+60, display[1]-100+5 )

def get_pos_visagem( display ):
    return ( display[0]+80, display[1]-110 )

def get_pos_helic( display ):
    return ( display[0]-10, display[1]-310+np.random.randint( -5, 5 ) )

def update_pipira( cenario, play_game, display, active, pos_pipira, idx_pip, vel_pip ): 

    if active:
        cenario.blit( pipira[idx_pip], ( (pos_pipira[0], pos_pipira[1]) ) )
#        if not perdeu: # atualiza quando estiver ativo o jogo
        if play_game:
            pos_pipira = ( int(pos_pipira[0])-vel_pip, pos_pipira[1] )
        else: ## tela inicial
            if np.random.randint(0,10) > 7: 
                pos_pipira = ( int(pos_pipira[0])-vel_pip, pos_pipira[1]+np.random.randint(-15,10) )
            else:
                pos_pipira = ( int(pos_pipira[0])-vel_pip, pos_pipira[1]+np.random.randint(-5,5) )
        # parar o act_pipr apos alguma posicao que tenha saido completamente do cenario
        if pos_pipira[0] < -100.0 :
            active = False
            pos_pipira = get_pos_pipira( display )

        idx_pip += 1
        if idx_pip > 4: idx_pip = 0
        
        return pos_pipira, active, idx_pip


def update_visa( cenario, play_game, display, active, pos_visa, idx_visa ): 
    if active:
        cenario.blit( visagem[idx_visa], ( (pos_visa[0], pos_visa[1]) ) )
#        if not perdeu:
        if play_game:
            pos_visa = ( int(pos_visa[0])-vel_visa, pos_visa[1]+np.random.randint(-1,2) )
            
        else: ## janela inicial
            if np.random.randint(0,10) > 8:
                pos_visa = ( int(pos_visa[0])+vel_visa, pos_visa[1]+np.random.randint(-2,2) )
            else: 
                pos_visa = ( int(pos_visa[0])-vel_visa, pos_visa[1]+np.random.randint(-2,2) )

        # parar o act_pipr apos alguma posicao que tenha saido completamente do cenario
        if pos_visa[0] < -50.0 :
            active = False
            pos_visa = get_pos_visagem( display )

        idx_visa += 1
        if idx_visa > 3: idx_visa = 0
    
    return pos_visa, active, idx_visa 


def update_helic( cenario, display, active, pos_helc, idx_helc, act_dispr, pos_disp, idx_disp ):

    ## ativar o aparecimento do helicoptero
    if np.random.randint( 0,20 ) > 15 and not active:
        active = True
        print( "Ativar helicoptero")
    if active:
        x,y = np.random.randint( -2, 2 ), np.random.randint( -1, 2 )
        pos_helc = ( pos_helc[0]+x-vel_helc, pos_helc[1]+y)
        cenario.blit( helicop[ idx_helc ], ( pos_helc ) )
        idx_helc += 1
        if idx_helc > 3: idx_helc = 0

    ## desativar voo do helicoptero
    if pos_helc[0] < -50 or pos_helc[0] > display[0]+50:
        active = False
        pos_helc = get_pos_helic( display )

    ## ativar o disparo de bala
    if np.random.randint( 0,50 ) > 45 and not act_dispr and active:
        act_dispr = True
        print( "Ativar tiro do helic")
        pos_disp = ( pos_helc[0], pos_helc[1] )
    if act_dispr:
        pos_disp = ( pos_disp[0]-vel_disp, pos_disp[1]+5 )
        cenario.blit( helicop_arma[ idx_disp ], ( pos_disp ) )
        idx_disp += 1
        if idx_disp > 2: idx_disp = 0

    ## desativar disparo a partir das margens
    if pos_disp[0] < -20 or pos_helc[1] > display[1]:
        act_dispr = False


    return pos_helc, active, idx_helc, pos_disp, act_dispr, idx_disp

pipira_0 = pygame.image.load( './img/1/pipira_00.png' )
pipira_1 = pygame.image.load( './img/1/pipira_01.png' )
pipira_2 = pygame.image.load( './img/1/pipira_02.png' )
pipira_3 = pygame.image.load( './img/1/pipira_03.png' )
pipira_4 = pygame.image.load( './img/1/pipira_04.png' )

pipira_0 = pygame.transform.rotozoom( pipira_0, 0, 0.3 )
pipira_1 = pygame.transform.rotozoom( pipira_1, 0, 0.3 )
pipira_2 = pygame.transform.rotozoom( pipira_2, 0, 0.3 )
pipira_3 = pygame.transform.rotozoom( pipira_3, 0, 0.3 )
pipira_4 = pygame.transform.rotozoom( pipira_4, 0, 0.3 )
pipira = [ pipira_0, pipira_1, pipira_2, pipira_3, pipira_4 ]

idx_pip = 0
vel_pip = 20

visagem_0 = pygame.image.load( './img/1/visagem_00.png' )
visagem_1 = pygame.image.load( './img/1/visagem_01.png' )
visagem_2 = pygame.image.load( './img/1/visagem_02.png' )
visagem_3 = pygame.image.load( './img/1/visagem_03.png' )

visagem_0 = pygame.transform.rotozoom( visagem_0, 0, 0.3 )
visagem_1 = pygame.transform.rotozoom( visagem_1, 0, 0.3 )
visagem_2 = pygame.transform.rotozoom( visagem_2, 0, 0.3 )
visagem_3 = pygame.transform.rotozoom( visagem_3, 0, 0.3 )
visagem = [ visagem_0, visagem_1, visagem_2, visagem_3 ]

idx_visa = 0
vel_visa = 15

## helicoptero
helicop_0 = pygame.image.load( './img/1/inimigos/helicop_00.png' )
helicop_1 = pygame.image.load( './img/1/inimigos/helicop_01.png' )
helicop_2 = pygame.image.load( './img/1/inimigos/helicop_02.png' )

helicop_0 = pygame.transform.rotozoom( helicop_0, 0, 0.2 )
helicop_1 = pygame.transform.rotozoom( helicop_1, 0, 0.2 )
helicop_2 = pygame.transform.rotozoom( helicop_2, 0, 0.2 )
helicop_0 = pygame.transform.flip( helicop_0, True, False )
helicop_1 = pygame.transform.flip( helicop_1, True, False )
helicop_2 = pygame.transform.flip( helicop_2, True, False )

helicop = [helicop_0, helicop_1, helicop_0, helicop_2]
idx_helc = 0
vel_helc = 5

## bala do helicoptero
helicop_arma_0 = pygame.image.load( './img/1/inimigos/helicop_arma_00.png' )
helicop_arma_1 = pygame.image.load( './img/1/inimigos/helicop_arma_01.png' )
helicop_arma_2 = pygame.image.load( './img/1/inimigos/helicop_arma_02.png' )

helicop_arma_0 = pygame.transform.rotozoom( helicop_arma_0, 0, 0.5 )
helicop_arma_1 = pygame.transform.rotozoom( helicop_arma_1, 0, 0.5 )
helicop_arma_2 = pygame.transform.rotozoom( helicop_arma_2, 0, 0.5 )
helicop_arma = [ helicop_arma_0, helicop_arma_2, helicop_arma_1, helicop_arma_2 ]

## index inicial de renderizacao
idx_disp = 0
## velocidade de disparo
vel_disp = 10
