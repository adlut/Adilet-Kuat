import pygame
import random

pygame.init()

# Define constants
RES = 600
SIZE = 50
LEVEL_SIZE = RES - 50  # Initial level size
screen = pygame.display.set_mode((RES, RES))

# Function to generate random positions
def random_position():
    return random.randrange(0, LEVEL_SIZE, SIZE)

x, y = random_position(), random_position()
apple = random_position(), random_position()
baff = random_position(), random_position()
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 6
shrink = 50
done = True
color = (0, 153, 230)
bg = pygame.image.load('images/qas.png')
black = (0, 0, 0)
stop = True

while done:
    screen.fill("black")
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True}
            elif event.key == pygame.K_a and dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False}
            elif event.key == pygame.K_s and dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True}
            elif event.key == pygame.K_d and dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True}

    if stop:
        [(pygame.draw.rect(screen, "green", (i, j, SIZE, SIZE))) for i, j in snake]
        pygame.draw.rect(screen, "red", (*apple, SIZE, SIZE))
        x = x + dx * SIZE
        y = y + dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

        if length % 3 == 0:
            pygame.draw.rect(screen, "Yellow", (*baff, SIZE, SIZE))
            if snake[-1] == baff:
                length = length + 2
                fps = fps - 2
                baff = random_position(), random_position()

        if snake[-1] == apple:
            apple = random_position(), random_position()
            length = length + 1
            fps = fps + 1
            # Shrink the level size every time the snake eats an apple
            LEVEL_SIZE -= shrink

    # Check if the snake hits the boundary of the level
    if x < 0 or x > LEVEL_SIZE - SIZE or y < 0 or y > LEVEL_SIZE - SIZE:
        stop = False
        screen.blit(bg, (40, 0))

    # Check if the snake collides with itself
    if len(snake) != len(set(snake)):
        stop = False
        screen.blit(bg, (0, 0))

    pygame.display.update()
    clock.tick(fps)
