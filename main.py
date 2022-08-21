"""! @brief Jogo adaptado do chrome TREX"""

##
# @file main.py
#
# @brief Arquivo principal do jogo Chrome Trex
#
# @section Descrição
# O objetivo do jogo é alcançar o máximo de pontos possíveis gerando sonoridade única.
# Para isso, o jogador controla o personagem Trex que deve continuamente correr e pular
# ou ainda utilizar as armas que possue para continuar vivo no jogo.
# O participante controla apenas o TRex, podendo atirar bolas de fogo e pular obstáculos.
#
# @author Claudio Rogerio 02.03.2020
#
# @subsection TODO
#   - Ações com joystck
#   - Audio sincronizado com acoes durante o jogo
#
# @subsection MAKED
#   - Totais de arvores
#   - Acoes de retorno do personagem
#   - Pontuacao max
#   - Tela inicial
#   - Ações com sensores
#   - Nuvens
#   - Terreno
#   - Movimentacao do TRex para baixo
#   - Tela inicial botao 'play'
#   - Animacao inicial
#   - Funcao de atualizacao de posicao de personagens


## biblioteca responsavel por renderizar o jogo
import pygame
## biblioteca responsavel para gerenciar acoes externas ao cenario de jogo
import sys
## biblioteca utilizada para gerar numeros aleatorios
import numpy as np
import operator

## Inicializacao do jogo
pygame.init()
## titulo da janela
pygame.display.set_caption( 'T_Rex' )
## criacao do cenario
display = ( 800, 400 )
cenario = pygame.display.set_mode( display )
## variavel de controle de FPS
clock = pygame.time.Clock()

## arquivo contendo armas para o Trex
from armas import *
## arquivo contendo a importacao do Trex
from personagem import *
## arquivo contendo os adversários do Trex
from inimigos import *
## arquivo contendo nuvens para a construcao do cenario
from nuvens import *
## arquivo contendo o terreno para a construcao do cenario
from terreno import *
## importa Inicializacao do JoyStick
from joystick import *
## arquivo com informacao de chuva, neblina
from particulas import *
from initial import *
from sensor import *
## musicas para cada personagem
#from audio import *

DEBUG = 0

## fonte utilizada para informar a pontuacao
font = pygame.font.Font( 'font/joystix monospace.ttf', 12 )
color_font = (50,50,50)

## variaveis globais de controle do cenario
i = 0
up_color = 1
conta = 23
delay = 50
vel_jogo = 10

## acoes do personagem
andar = False
pular = False
abaixar = False

disparo = False
perdeu = False

## piso do cenario
act_terr = False
## total de nuvens
vel_nuvem = 1
## criacao de nuvens
n_nuvens = iniciar_nuvens( display )
## criacao de n particulas
partc_x, partc_y = create_particulas( 100, display )
cor_part = ( 10, 10, 10 )

## ativar trex
act_trex = False
## direcao inicial para o pulo do personagem
direcao = 18
idx_rex = 0

## acoes dos inimigos
act_pipr = False
act_visa = False
act_helc = False
act_helc_disp = False       ## ativar disparo do helicp

## iniciar JoyStick
joys = init_joystick()

## posicoes iniciais de cada participante
pos_rex = get_pos_rex( display )
pos_fogo = get_pos_fogo( display )
pos_pipira = get_pos_pipira( display )
pos_visa = get_pos_visagem( display )
pos_helc = get_pos_helic( display )
pos_arv = get_pos_arv( display )
act_arv = False
arv_type = 0

## posicao atualizada a cada momento
pos_disp = ( 1, 1 )

## inicalizacao do mixer sonoro
pygame.mixer.init( 44100, -16, 4, 1024*4 )
musica_fundo = pygame.mixer.Sound( './audio/086_loose-playa-groove.wav' )
pygame.mixer.Channel(0).play( musica_fundo, loops = -1 )
## musica do cenario
#pygame.mixer.music.play( )
act_music = False

## controle do pulo do personagem
cont = 0

## controle de cores do ambiente e particulas
i= 0

## pontos maximos
f = open( 'points_max.txt', 'r' )
pontos_max = int( f.read() )
f.close()

## pontos adquiridos durante o jogo
pontos = 0

# tela inicial
play_game = False
pos_bt_play = get_pos_play( display )

sensor_1 = False
if sensor_1 == True:
    touch = start_sensor('/dev/ttyUSB0', 9600 )

## esquerda p direita
left_motion = True

## nao usado
def load_ini():
    act_pipr = False
    act_visa = False
    perdeu = False
    balas = 2
    vel_jogo = 10
    pos_pipira = get_pos_pipira( display )
    pos_visa = get_pos_visagem( display )
    pos_arv = get_pos_arv( display )
    n_nuvens = iniciar_nuvens( display )
    t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]

## inicio do jogo
while( True ):

    if play_game:
        ## eventos externos
        ## eventos de sensores
        if sensor_1 == True:
            sensor_0 = get_data_arduino( touch )
            if sensor_0 > 10.0:
                if not andar:
                    andar = True
                if andar and not abaixar:
                    pular = ~pular
                    print( 'Pula sensor' )
        if perdeu:
            act_pipr = False
            act_visa = False
            act_arv = False
            perdeu = False
            balas = 2
            vel_jogo = 10
            pos_pipira = get_pos_pipira( display )
            pos_visa = get_pos_visagem( display )
            pos_arv = get_pos_arv( display )
            n_nuvens = iniciar_nuvens( display )
            t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]
#        if perdeu:
            print( 'Perdeu!!!')
            mus_perdeu = pygame.mixer.Sound( './audio/lose.wav' )
            pygame.mixer.Channel(0).play( mus_perdeu )


        ## eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

            ## JoyStick acionado por botões
            if event.type == pygame.JOYBUTTONDOWN:
                print( "evento 0 --",event.button, type(event.button) )

                # JoyStick acionado por botão B """
                if event.button == 2:
                    print('Fogo')
                    if play_game and not disparo and balas >= 1 : # evitar duplo balas
                        disparo = True
                        balas -=1   # contagem de balas utilizados
                        pos_fogo = (pos_fogo[0], pos_rex[1]+8) # para atualizar a posicao atual do rex na vertical
                ## botao 'start'
                if event.button == 9:
                    if play_game and not andar:
                        andar = True

            ## movimentacao dos eixos
            if event.type == pygame.JOYAXISMOTION:
                if DEBUG: print("evento eixos", event )

                ## eixo inferior
                if event.axis == 1 and event.value >= 1.0:
                    abaixar = True
                    t_rex = [ t_rex_4, t_rex_4, t_rex_5, t_rex_5, t_rex_5 ]
                    pos_rex = get_pos_rex( display ) #+25
                    pos_rex = (pos_rex[0], pos_rex[1]+25)
                    print('Abaixa-se!')

                ## volta a posicao normal
                if event.axis == 1 and event.value == 0.0 and abaixar :
                    abaixar = False
                    t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]
                    pos_rex = get_pos_rex( display )
                    print('Levanta-se!')

                ## eixo superior
                if event.axis == 1 and event.value < -1.0:
                    if andar:
                        pular = ~pular
                    andar = True
                    act_terr = True

                    if perdeu:
                        act_pipr = False
                        act_visa = False
                        act_arv = False
                        perdeu = False
                        balas = 2
                        vel_jogo = 10
                        pos_pipira = get_pos_pipira( display )
                        pos_visa = get_pos_visagem( display )
                        n_nuvens = iniciar_nuvens( display )
                        t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]


                ## eixo esquerda
                if event.axis == 0 and event.value < -1.0:
                    t_rex = [ t_rex_0_180, t_rex_1_180, t_rex_0_180, t_rex_2_180, t_rex_3_180 ]
                    left_motion = False

                ## eixo direita
                if event.axis == 0 and event.value >= 1.0:
                    t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]
                    left_motion = True

            ## nao utilizado
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

            ## acoes do teclado
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    abaixar = False
                    t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]
                    pos_rex = get_pos_rex( display )
                    print('Levanta-se!')


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    f = open( 'points_max.txt', 'w' )
                    f.write(str(pontos_max))
                    f.close()
                    pygame.quit(); sys.exit();

                ## atirar a arma
                if event.key == pygame.K_a:
                    print('Fogo')
                    if not disparo and balas >= 1 : # evitar duplo balas
                        disparo = True
                        balas -=1 # contagem de balas utilizados
                        pos_fogo = ( pos_fogo[0], pos_rex[1]+8 ) # para atualizar a posicao atual do rex na vertical

                ## pulo e inicar o jogo
                if event.key == pygame.K_SPACE:
                    if not andar:
                        andar = True
                        act_terr = True

                    if andar and not abaixar:
                        pular = ~pular

                    if perdeu:
                        act_pipr = False
                        act_visa = False
                        act_arv = False
                        perdeu = False
                        balas = 2
                        vel_jogo = 10
                        pos_arv = get_pos_arv( display )
                        pos_pipira = get_pos_pipira( display )
                        pos_visa = get_pos_visagem( display )
                        n_nuvens = iniciar_nuvens( display )
                        t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]


                if event.key == pygame.K_LEFT:
                    t_rex = [ t_rex_0_180, t_rex_1_180, t_rex_0_180, t_rex_2_180, t_rex_3_180 ]
                    left_motion = False

                if event.key == pygame.K_RIGHT:
                    t_rex = [ t_rex_0, t_rex_1, t_rex_0, t_rex_2, t_rex_3 ]
                    left_motion = True
                    #left_motion = operator.not_( left_motion )

                ## visualizar teclas pressionadas
                print(pygame.key.name(event.key))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if play_game:
                abaixar = True
                t_rex = [ t_rex_4, t_rex_4, t_rex_5, t_rex_5, t_rex_5 ]
                pos_rex = get_pos_rex( display ) #+25
                pos_rex = ( pos_rex[0], pos_rex[1]+25 )

                if DEBUG: print('Abaixa-se!')

        # cor de fundo
        cenario.fill( (255,255,255) )


        ## adicao de particulas
        if andar:
            partc_x, partc_y, cor_part = update_particulas( cenario, 'chuva', partc_x, partc_y, cor_part )
            if cor_part[1] > 252:
                partc_x, partc_y = create_particulas( 100, display )
                cor_part = (10,10,10)

        update_terreno( cenario, display, vel_jogo, act_terr, perdeu, left_motion )
        pos_arv, act_arv, arv_type = update_arvore( cenario, display, pos_arv, vel_jogo, act_arv, arv_type, andar, left_motion )

        # add nuvens
        if andar:
            for n, item in enumerate(n_nuvens):
                if DEBUG: print( 'Nuvens:', n_nuvens[n][0], '\t pos x', n_nuvens[n][1][0], '\t pos y', n_nuvens[n][1][1])
                aux_x = n_nuvens[n][1][0]
                aux_y = n_nuvens[n][1][1]
                if aux_x < -50.0:
                    aux_x, aux_y = get_pos_nuvem( display )
                n_nuvens[n][1] = ( aux_x-vel_nuvem, aux_y + np.random.randint( -1, 2 ) )

                # renderizar nuvens que fazem parte do cenario
                if item[1][0] < display[0]:
                    cenario.blit( nuvens[ item[0] ], ( (item[1][0], item[1][1] ) ) )

        if pular:
            cont += 1
            pos_rex =  ( pos_rex[0], pos_rex[1]-(direcao) )
            cenario.blit( t_rex[0], ( (pos_rex[0] , pos_rex[1]) ) )
            if cont >= 7:
                direcao = -12
                #cont += direcao*2   # considerar a fisica de descida
            if cont >= 14 :
                pular = False
                direcao = 15
                pos_rex = get_pos_rex( display )
                cont = 0
        else:
            if andar:
                if DEBUG: print( 'Ande meu filho!' )
                idx_rex +=1
                if idx_rex > 3: idx_rex = 0
            else: idx_rex = 0

            if perdeu:
                cenario.blit( t_rex[4], ( (pos_rex[0], pos_rex[1]) ) )
            else:
                cenario.blit( t_rex[idx_rex], ( (pos_rex[0], pos_rex[1]) ) )
            pygame.time.delay( 10 ) # dificuldade extra


        # ativar o act_pipr da pipira
        if np.random.randint(0,10) > 8:
            if not act_pipr and andar and not act_visa:
                act_pipr = ~act_pipr
                if DEBUG: print( 'Voa pipira!' )
        if act_pipr:
            cenario.blit( pipira[idx_pip], ( (pos_pipira[0], pos_pipira[1]) ) )
            if not perdeu: # atualiza quando estiver ativo o jogo
                if left_motion == True:
                    pos_pipira = ( int(pos_pipira[0])-vel_pip, pos_pipira[1] )
                else:
                    pos_pipira = ( int(pos_pipira[0])-vel_pip+6, pos_pipira[1] )
            # parar o act_pipr apos alguma posicao que tenha saido completamente do cenario
            if pos_pipira[0] < -100.0 :
                act_pipr = False
                pos_pipira = get_pos_pipira( display )

            idx_pip += 1
            if idx_pip > 4: idx_pip = 0

        # ativar act_visagem
        if np.random.randint(0,20) > 18:
            if not act_pipr and andar and not act_visa:
                act_visa = ~act_visa
                if DEBUG: print( 'act_visagem papai!!!' )
        if act_visa:
            cenario.blit( visagem[idx_visa], ( (pos_visa[0], pos_visa[1]) ) )
            if not perdeu:
                if left_motion == True:
                    pos_visa = ( int(pos_visa[0])-vel_visa, pos_visa[1]+np.random.randint(-1,2) )
                else:
                    pos_visa = ( int(pos_visa[0])-vel_visa+10, pos_visa[1]+np.random.randint(-1,2) )
            # parar o act_pipr apos alguma posicao que tenha saido completamente do cenario
            if pos_visa[0] < -50.0 :
                act_visa = False
                pos_visa = get_pos_visagem( display )

            idx_visa += 1
            if idx_visa > 3: idx_visa = 0

        ## disparo ativado
        if disparo:
            if balas >= 0:
                cont_disparo +=1        # controla a dimensao do disparo
                if cont_disparo == 7 :
                    fogo_view = fogo[1]
                if cont_disparo == 12 :
                    fogo_view = fogo[2]
                if cont_disparo == 35 :
                    fogo_view = fogo[1]
                if cont_disparo == 40 :
                    fogo_view = fogo[0]

                cenario.blit( fogo_view[idx_fogo], ( (pos_fogo[0], pos_fogo[1]) ) )
                pos_fogo = ( int(pos_fogo[0])+vel_fogo, pos_fogo[1]+np.random.randint(-1,2) )

                idx_fogo += 1
                if idx_fogo > 3: idx_fogo = 0

            ### colisao do disparo
                # ao final da janela
                if pos_fogo[0] > display[0] + 10:
                    pos_fogo = get_pos_fogo( display )
                    disparo = False
                    if DEBUG: print( 'fogo', pos_fogo, 'disp', display[0] )
                    cont_disparo = 0
                    fogo_view = fogo[0]

                # quando encontra adversarios
                if act_pipr:
                    dst = np.sqrt( np.power( pos_fogo[1]- pos_pipira[1], 2 )  + np.power( pos_fogo[0]-pos_pipira[0], 2) ) + 0.01

                    if dst < 20.0 :
                        if DEBUG: print( 'Arma alcancou passaro!' )
                        pontos += 5
                        act_pipr = False
                        disparo = False
                        cont_disparo = 0
                        fogo_view = fogo[0]
                        pos_pipira = get_pos_pipira( display )
                        pos_fogo = get_pos_fogo( display )

                if act_visa:
                    dst = np.sqrt( np.power( pos_fogo[1]- pos_visa[1], 2 )  + np.power( pos_fogo[0]-pos_visa[0], 2) ) + 0.01
                    ## a act_visagem eh um objeto maior, precisa de maior precisao pois varia de posicionamento na vertical
                    if dst < 30.0 :
                        if DEBUG: print( 'Alcancou act_visagem!' )
                        pontos += 7
                        act_visa = False
                        disparo = False
                        pos_visa = get_pos_visagem( display )
                        pos_fogo = get_pos_fogo( display )
                        fogo_view = fogo[0]
                        cont_disparo = 0
                        if DEBUG: print( 'fogo', pos_fogo, display[0] )

        pos_helc, act_helc, idx_helc, pos_disp, act_helc_disp, idx_disp = update_helic( cenario, display, act_helc, pos_helc, idx_helc, act_helc_disp, pos_disp, idx_disp )

        pygame.time.delay( 1000%vel_jogo )

        i += up_color

        ## colisoes com a pipira
        dst = np.sqrt( np.power( pos_pipira[1]- pos_rex[1], 2 )  + np.power( pos_pipira[0]-pos_rex[0], 2) ) + 0.01
        if DEBUG: print( pos_pipira[1], pos_rex[1], pos_pipira[0], pos_rex[0], dst )

        ## distancia de colisao
        if dst < 40.0 :
            if DEBUG: print( 'Colidiram!' )
            pontos = 0
            andar = False
            perdeu = True

        ## colisoes com a act_visagem
        dst = np.sqrt( np.power( pos_visa[1]- pos_rex[1], 2 )  + np.power( pos_visa[0]-pos_rex[0], 2) ) + 0.01

        if DEBUG: print( pos_visa[1], pos_rex[1], pos_visa[0], pos_rex[0], dst )

        if dst < 40.0 :
            if DEBUG: print( 'Colidiram!' )
            pontos = 0
            andar = False
            perdeu = True

        ## colisoes com o disparo do helicop
        dst = np.sqrt( np.power( pos_disp[1]- pos_rex[1], 2 )  + np.power( pos_disp[0]-pos_rex[0], 2) ) + 0.01
        if DEBUG: print( pos_disp[1], pos_rex[1], pos_disp[0], pos_rex[0], dst )

        ## distancia de colisao
        if dst < 20.0 :
            if DEBUG: print( 'Colidiram-se!' )
            pontos = 0
            andar = False
            perdeu = True

        ## colisoes com o arvore
        dst = np.sqrt( np.power( pos_arv[1]- pos_rex[1], 2 )  + np.power( pos_arv[0]-pos_rex[0], 2) )
        if DEBUG: print( pos_arv[1], pos_rex[1], pos_arv[0], pos_rex[0], dst )

        ## distancia de colisao
        if dst < 20.0 :
            if DEBUG: print( 'Colidiram-se!' )
            pontos = 0
            andar = False
            perdeu = True

        ## pontuacao
        if andar:
            pontos +=1
            if disparo:
                color_font = (250,20,20)
                pontos -= 2
            else: color_font = (50,50,50)

        ## show pontuacao
        if DEBUG: print( pontos, balas )

        text = font.render( str(pontos), True, color_font )
        cenario.blit( text, (70, 20) )

        if pontos > pontos_max:
            pontos_max = pontos
        text = font.render( str(pontos_max), True, (180,180,180) )
        cenario.blit( text, (125, 20) )

        ## informativo das armas disponiveis
        pos = 25
        if balas == 2:
            cenario.blit( ajuda[idx_ajuda], ( 25, 16 ) )
            cenario.blit( ajuda[idx_ajuda], ( 40, 16 ) )
        else:
            if balas == 1:
                cenario.blit( ajuda[idx_ajuda], ( 25, 16 ) )
                cenario.blit( ajuda[3], ( 40, 16 ) )
            else:
                cenario.blit( ajuda[3], ( 25, 16 ) )
                cenario.blit( ajuda[3], ( 40, 16 ) )
                recarregar_balas +=1
                if recarregar_balas > 200:
                    balas = 2
                    recarregar_balas = 0

        idx_ajuda += 1
        if idx_ajuda > 2 : idx_ajuda = 0

        #pos_musica = float(pygame.mixer.music.get_pos())
        #print( pos_musica, 'jjjjjjjj')
        #act_music = mix_music( pos_musica, act_music, perdeu, andar, pular, disparo, act_helc, act_helc_disp, act_pipr, act_visa  )
        #if pos_musica > 1280 or pos_musica == -1:
        #    pygame.mixer.music.play( )
        ## controle de audios
        #if perdeu:
        #    pygame.mixer.Channel(1).stop()

    #    pygame.display.flip()
#        pygame.display.update()
        if pontos % 100 == 0 and vel_jogo < 50 and andar :
            vel_jogo +=1
            if DEBUG: print( vel_jogo )


    else:
        act_pipr = True
        act_visa = True
        act_helc = True
        act_helc_disp = True
#        print( "Nao iniciado" )

        cenario.fill( (255,255,255) )
        pos_pipira, active, idx_pip = update_pipira( cenario, play_game, display, act_visa, pos_pipira, idx_pip, vel_pip )
        pos_visa, act_visa, idx_visa = update_visa( cenario, play_game, display, act_visa, pos_visa, idx_visa )
        pos_helc, act_helc, idx_helc, pos_disp, act_helc_disp, idx_disp = update_helic( cenario, display, act_helc, pos_helc, idx_helc, act_helc_disp, pos_disp, idx_disp )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();

            # analisa a movimentacao do mouse para determinado local do bt start
            pos2 = pygame.mouse.get_pos()

            if pos2[0] >=330 and pos2[0] <=480 and pos2[1] >=90 and pos2[1] <=150:
                id_play = 1
            else:
                id_play = 0

            # pressiona o bt do mouse
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print( 'Mouse pos:', pos )
                if pos2[0] >=330 and pos2[0] <=480 and pos2[1] >=90 and pos2[1] <=150:
                    if DEBUG: print( 'Press bt play' )
                    id_play = 2
                    ## chama o jogo
                    play_game = True
                    andar = True
                    pos_pipira = get_pos_pipira( display ) # pos inicial
                    pos_visa = get_pos_visagem( display )
                    # inicial o terreno e depois ativa a atualizacao
                    update_terreno( cenario, display, vel_jogo, act_terr, perdeu, left_motion )
                    act_terr = True
                else:
                    id_play = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit();


        cenario.blit( play[id_play], ( pos_bt_play ) )

    pygame.display.update()
    clock.tick( vel_jogo )
