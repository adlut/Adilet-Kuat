import pygame

pygame.init()

width , height = 680, 420

surface = pygame.display.set_mode((width, height))
name_pro = pygame.display.set_caption("Music player")

background = pygame.image.load('images/io.jpg')
stop_icon = pygame.image.load('images/pause.png')
next_icon = pygame.image.load('images/next.png')
previous_icon = pygame.image.load('images/previous.png')
play_icon = pygame.image.load('images/play.png')


pygame.mixer.music.load('music/attack.wav')
pygame.mixer.music.load('music/duvet.wav')
pygame.mixer.music.load('music/feet.wav')

playlist = {
    1: 'music/attack.wav',
    2: 'music/duvet.wav',
    3: 'music/feet.wav'
}

count_track = 1
run = True
FPS = 60
is_playing = False
tickrate = pygame.time.Clock()
paused_time = 0

while run:

    surface.blit(background, (0, 0))
    surface.blit(previous_icon, (100,155))
    
    if is_playing == False:
        surface.blit(play_icon,(262,155))
    else:
        surface.blit(stop_icon, (262,155))
        
    surface.blit(next_icon, (424,155))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_F7) and is_playing == False:
                # pause need for didn`t replay music
                if paused_time != 0:
                    pygame.mixer.music.unpause()
                    is_playing = True
                else:
                    pygame.mixer.music.load(playlist[count_track])
                    pygame.mixer.music.play()
                    is_playing = True
            elif event.key == pygame.K_F5 or event.key == pygame.K_LEFT:
                if count_track == 1:
                    count_track = 3
                else:
                    count_track -= 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
            elif event.key == pygame.K_F6 or event.key == pygame.K_RIGHT:
                if count_track == 3:
                    count_track = 1
                else:
                    count_track += 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
            elif (event.key == pygame.K_SPACE or event.key == pygame.K_F7) and is_playing == True:
                pygame.mixer.music.pause()
                is_playing = False
                paused_time = pygame.mixer.music.get_pos()

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    tickrate.tick(FPS)
        


        