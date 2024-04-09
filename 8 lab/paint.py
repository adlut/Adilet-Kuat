import pygame

pygame.init()
pygame.font.init()


h=500
w=600
screen=pygame.display.set_mode((w, h))
white=(255, 255, 255)
black= (0, 0, 0)
red=(255, 0, 0)
blue=(0, 255, 0)
green=(0, 0, 255)
bg=pygame.image.load('images/zz.jpg').convert()

FPS=60

rows=cols=50
toolbar=w-h
pixel_size=w//cols
draw_grid_lines=False

run = True
while run:

    screen.blit(bg, (-10, -10))


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False