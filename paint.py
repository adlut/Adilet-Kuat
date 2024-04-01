import pygame 
clock=pygame.time.Clock()

pygame.init()
w=414
h=312
screen=pygame.display.set_mode((w, h))
pygame.display.set_caption("paint")
az=pygame.image.load('images/qqa.jpg').convert()

run = True
while run:
    screen.blit(az, (0, 0))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(15)