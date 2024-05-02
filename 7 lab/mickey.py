import pygame
from datetime import datetime
import math

clock = pygame.time.Clock()
w = 245
h = 250
r = h - 90
r_list={
'sec':r-10, 'min':r-40
}

pygame.init()
screen = pygame.display.set_mode((497, 502))
pygame.display.set_caption("clock")
bg = pygame.image.load('images/zzzz.png').convert_alpha()
music_playing=False
bg_m = 0
font = pygame.font.SysFont('big', 40)
def get_clock_pos(clock_dict, clock_hand, key):
    x = w + r_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = h + r_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

breaker = True  
while breaker:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breaker = False
            
    screen.blit(bg, (bg_m, 0))
    t = datetime.now()
    
    time_render = font.render(f'{t:%M:%S}', True, 'Red', 'Green')
    screen.blit(time_render, (25, 25))
    
    clock12 = dict(zip(range(12), range(0, 360, 30)))
    clock60 = dict(zip(range(60), range(0, 360, 6)))
    
    minute, second = t.minute, t.second
    
    pygame.draw.line(screen, pygame.Color('magenta'), (w, h), get_clock_pos(clock60, second,'sec'), 4)
    pygame.draw.line(screen, pygame.Color('Orange'), (w, h), get_clock_pos(clock60, minute,'min'), 7)
    
    pygame.display.flip()
    
    clock.tick(20)

