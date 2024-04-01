import pygame

clock=pygame.time.Clock()

pygame.init()
w=440
h=500
screen=pygame.display.set_mode((w, h))
pygame.display.set_caption("snake.io")
bg=pygame.image.load('images/bgs.jpg').convert()
color1=(109, 14, 120)
color2=(18, 193, 224)
snake_color=(31, 145, 65)
block=20
count=20
margin=1

def draw_block(color, row, column):
    x = block*count+2*block+margin*count
    y = block * count + 2 * block + margin * count+70
    pygame.draw.rect(screen, color, [(0, 0, block, block)])



snake_block=[[0, 0], [0, 1]]


run = True
while run:
    
    screen.blit(bg, (0, 0))
    for row in range(count):
        for column in range(count):
            if (row+column)%2==0:
                color=color2
            else:
                color=color1
            draw_block(color, row, column)
    draw_block(snake_color, 0, 0)
    for block in snake_block:
         x, y = block
         draw_block(snake_color, x, y)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False