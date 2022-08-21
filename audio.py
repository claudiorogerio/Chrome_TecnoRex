
import pygame

pygame.mixer.init()
musica_cenario = pygame.mixer.music.load( './audio/cenario.ogg' )

#musica_cenario = pygame.mixer.Sound( './audio/086_loose-playa-groove.wav' )
#musica_cenario = pygame.mixer.music.load('./audio/cenario.wav')
#musica_cenario = pygame.mixer.Sound( './audio/086_loose-playa-groove.wav' )
musica_trex = pygame.mixer.Sound( './audio/trex.wav' )
musica_trex_pulo = pygame.mixer.Sound( './audio/trex_pulo.ogg' )
musica_helc = pygame.mixer.Sound( './audio/helc.wav' )
musica_arma = pygame.mixer.Sound( './audio/arma.wav' )

## variaveis locais de controle dos audios
#act_music = False
act_mus_pulo = False

def mix_music( pos_musica, act_music, perdeu, act_andar, act_pulo, act_arma, act_helc, act_helc_arma, act_pipr, act_visa):
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
