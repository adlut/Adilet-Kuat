import pygame
import random
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((280, 309))
pygame.display.set_caption("racer")
bg = pygame.image.load('images/t1.jpg').convert()
bg1 = pygame.image.load('images/t2.jpg').convert()
bg2 = pygame.image.load('images/t3.jpg').convert()
bg3 = pygame.image.load('images/tr.jpg').convert()
bg_move = 0
car_x = 100
car_y = 200
car_m = 10
coin_x=random.randint(30, 260)
coin=pygame.image.load('images/coin.png').convert_alpha()
coin_list = [pygame.Rect(coin_x, -10, coin.get_width(), coin.get_height())]
car = pygame.image.load('images/red.png').convert_alpha()
end = pygame.image.load('images/end.jpg').convert()
score=0
font = pygame.font.Font(None, 36)
enemy=pygame.image.load('images/bl.png').convert_alpha()
enemy_interval=random.randint(2000, 3000)
enemy_x=random.randint(50, 100)
enemy_y=-30
enemy_list= [pygame.Rect(enemy_x, -30, enemy.get_width(), enemy.get_height())]
enemy_speed=10
enemy_timer = pygame.USEREVENT + 1

coin_timer = pygame.USEREVENT + 1
coin_interval = random.randint(2000, 5000)
pygame.time.set_timer(coin_timer, coin_interval)
gameplay=True
run = True
while run:
    if bg_move <= 2400:
        screen.blit(bg, (0, bg_move))
        screen.blit(bg1, (0, bg_move - 309))
        screen.blit(bg1, (0, bg_move - 309 * 2))
        screen.blit(bg1, (0, bg_move - 309 * 3))
        screen.blit(bg2, (0, bg_move - 309 * 4))
        screen.blit(bg2, (0, bg_move - 309 * 5))
        screen.blit(bg2, (0, bg_move - 309 * 6))
        screen.blit(bg3, (0, bg_move - 309 * 7))
        screen.blit(bg2, (0, bg_move - 309 * 8))

        screen.blit(car, (car_x, car_y))
        player_barrier= car.get_rect(topleft=(car_x, car_y))


        if gameplay:
            for el in coin_list:
                screen.blit(coin, el)
                el.y += 10
                if el.y > 310:
                    coin_list.remove(el)
                if player_barrier.colliderect(el):
                    score += 1         
                    enemy_speed+=5           
                    coin_list.remove(el)
        if gameplay:
            for el in enemy_list:
                screen.blit(enemy, el)
                el.y += enemy_speed
                if el.y > 310:
                    enemy_list.remove(el)
                if player_barrier.colliderect(el):                  
                    run=False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and car_y >= 20:
            car_y -= 10
            bg_move += 10
        if keys[pygame.K_d] and car_x < 200:
            car_x += 10
        if keys[pygame.K_a] and car_x > 0:
            car_x -= 10
        if keys[pygame.K_s] and car_y < 220:
            car_y += 20
        bg_move += 10
        if bg_move >= 2400:
            bg_move += 10
        score_text = font.render(f"Score: {score}", True, (252, 136, 3))
        screen.blit(score_text, (170, 10))
    else:
        screen.blit(end, (-10, -10))
        score_text = font.render(f" your score: {score}", True, (252, 136, 3))
        screen.blit(score_text, (100, 280))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == coin_timer:
            coin_x = random.randint(30, 220)  # Update coin's x position
            coin_list.append(pygame.Rect(coin_x, -10, coin.get_width(), coin.get_height()))
            coin_interval = random.randint(2000, 5000)
            pygame.time.set_timer(coin_timer, coin_interval)
            
        if event.type == enemy_timer:
            enemy_x = random.randint(10, 100)  # Update enemy's x position
            enemy_list.append(pygame.Rect(enemy_x, -30, enemy.get_width(), enemy.get_height()))
            enemy_interval = random.randint(1000, 3000)
            pygame.time.set_timer(enemy_timer, enemy_interval)
    clock.tick(20)
