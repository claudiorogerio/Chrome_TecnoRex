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
# @author Claudio Rogerio 02.07.2022


import pygame

pygame.mixer.set_num_channels(20)
pygame.mixer.init()

##musica_cenario = pygame.mixer.Sound( './audio/086_loose-playa-groove.wav' )
##musica_cenario = pygame.mixer.music.load('./audio/cenario.wav')
##musica_cenario = pygame.mixer.Sound( './audio/086_loose-playa-groove.wav' )
#musica_trex = pygame.mixer.Sound( './audio/trex.wav' )
#musica_trex_pulo = pygame.mixer.Sound( './audio/trex_pulo.ogg' )
#musica_helc = pygame.mixer.Sound( './audio/helc.wav' )
#musica_arma = pygame.mixer.Sound( './audio/arma.wav' )
mus_intro = pygame.mixer.Sound( './audio/intro.ogg' )

mus_base_groove = pygame.mixer.Sound( './audio/bassdrum.ogg' )
mus_base_hhat_close = pygame.mixer.Sound( './audio/hihat_closed.ogg' )
mus_base_hhat_open = pygame.mixer.Sound( './audio/hihat_opened.ogg' )
mus_base_snare = pygame.mixer.Sound( './audio/snare.ogg' )

mus_perdeu = pygame.mixer.Sound( './audio/lose.wav' )

mus_visagem = pygame.mixer.Sound( './audio/visagem.ogg' )
mus_pipira = pygame.mixer.Sound( './audio/pipira.ogg' )
mus_helc = pygame.mixer.Sound( './audio/clap.ogg' )
mus_helc_disparo = pygame.mixer.Sound( './audio/shaker.ogg' )


## variaveis locais de controle dos audios
#act_music = False
act_mus_pulo = False

# on/off music base on game
def mix_music( mus_base, mus_stop, version = 1 ):

    if version == 1 and mus_base == False :
        print('[mix music] Play base music', mus_base, mus_stop)
        pygame.mixer.Channel(0).play( mus_base_groove, loops = -1 )
        pygame.mixer.Channel(1).play( mus_base_hhat_close, loops = -1 )
        pygame.mixer.Channel(2).play( mus_base_hhat_open, loops = -1 )
        pygame.mixer.Channel(3).play( mus_base_snare, loops = -1 )
        mus_base = True

    #
    if mus_stop == True :
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(1).stop()
        pygame.mixer.Channel(2).stop()
        pygame.mixer.Channel(3).stop()
        pygame.mixer.Channel(0).play( mus_perdeu )
        print( '[mix music] Stop base music' )
        mus_stop = False

    print( '[mix music]', mus_base, mus_stop )

    return mus_base

'''
# acoes musicais de personagens e adversarios
##
'''
def mix_persona( pipira_on, mus_pip_on,
                visagem_on, mus_visa_on,
                arvore_on, mus_arv_on,
                helic_on, mus_helc_on,
                helic_disp_on, mus_helc_disp_on,
                trex_arma_on, mus_trex_disp_on ):

    #### pipira ativada
    if pipira_on :
        if not mus_pip_on :
            pygame.mixer.Channel(4).play( mus_pipira, loops = -1 )
            mus_pip_on = True
    else:
        pygame.mixer.Channel(4).stop()

    #### visagem ativada
    if visagem_on :
        if not mus_visa_on :
            pygame.mixer.Channel(5).play( mus_visagem, loops = -1 )
            mus_visa_on = True
    else:
        pygame.mixer.Channel(5).stop()

    #### helicoptero ativado
    if helic_on :
        if not mus_helc_on :
            pygame.mixer.Channel(6).play( mus_helc, loops = -1 )
            mus_helc_on = True
    else:
        pygame.mixer.Channel(6).stop()


    #### disparo do helicoptero
    if helic_disp_on :
        if not mus_helc_disp_on :
            pygame.mixer.Channel(7).play( mus_helc_disparo, loops = -1 )
            mus_helc_disp_on = True
    else:
        pygame.mixer.Channel(7).stop()

    return mus_pip_on, mus_visa_on, mus_arv_on, mus_helc_on, mus_helc_disp_on, mus_trex_disp_on


## nao utilizado
def mix_music2( pos_musica, act_music, perdeu, act_andar, act_pulo, act_arma, act_helc, act_helc_arma, act_pipr, act_visa):
    """
    Sincroniza todos os audios de cada personagem
    """
    global act_mus_pulo
    #pos_musica = pygame.mixer.music.get_pos()
    if pos_musica > 1280 :
        pygame.mixer.music.set_pos(0)
#    print( 'a####################qui')
    #    pygame.mixer.music.play( )

    #if not perdeu and not act_andar:

        #print( pygame.mixer.music.get_pos() , 'music')

    #    print( 'aqui cenario' )

    if not perdeu and act_andar :
        #pygame.mixer.play()
        #pygame.mixer.Channel(0).stop()
        #pygame.mixer.Channel(0).play( musica_cenario )
        if not act_music:
            #if pygame.mixer.music.get_pos() % 2 == 0:
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.Channel(1).play( musica_trex, loops = -1 )
                act_music = True

        if act_music and act_pulo and not act_mus_pulo:
            #if pygame.mixer.music.get_pos() % 2 == 0:
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.Channel(2).play( musica_trex_pulo )
                #act_music = True
            act_mus_pulo = True

    return act_music
