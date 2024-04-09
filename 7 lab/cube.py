import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_r = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_r)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, HEIGHT - ball_r)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_r)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, WIDTH - ball_r)

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_r)
    pygame.display.flip()
pygame.quit()
sys.exit()