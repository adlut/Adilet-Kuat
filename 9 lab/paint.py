import pygame
import math

def calculate_rectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return (x, y, width, height)

def draw_square(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    return (x, y, side_length, side_length)

def draw_right_triangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    base = abs(x2 - x1)
    height = abs(y2 - y1)
    return [(x, y), (x, y + height), (x + base, y + height)]

def draw_equilateral_triangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    height = math.sqrt(3) * side_length / 2
    return [(x, y + height), ((x + x2) / 2, y), (x2, y + height)]

def draw_rhombus(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return [(x + width / 2, y), (x, y + height / 2), (x + width / 2, y + height), (x + width, y + height / 2)]

pygame.init()
screen = pygame.display.set_mode((800, 600))
second_screen = pygame.Surface((800, 600))

done = False
clock = pygame.time.Clock()
fps = 8
x_start = 10
y_start = 10
x_end = 10
y_end = 10
index_color = 0
index_tool = 0
mouse_moving = False

screen.fill((0, 0, 0))

colors = ["Red", "Blue", "White", "Green", "Yellow", "Pink", "Purple"]  # list of colors
tools = ["Rectangle", "Circle", "Eraser", "Square", "Right Triangle", "Equilateral Triangle", "Rhombus"]  # list of functions

font = pygame.font.Font(None, 30)  # Using default font with size 30
text_color = str("Color: " + str(colors[index_color]))
text_tool = str("Function: " + str(tools[index_tool]))
text_color_surface = font.render(text_color, True, (255, 255, 255))
text_tool_surface = font.render(text_tool, True, (255, 255, 255))

# Main game loop
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Handle mouse button presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fps = 60
                # Start drawing or erasing based on the selected tool
                if index_tool in [0, 1, 3, 4, 5, 6]:
                    x_start = event.pos[0]
                    y_start = event.pos[1]
                if index_tool == 2:
                    x_start = event.pos[0]
                    y_start = event.pos[1]
                    x_end = x_start
                    y_end = y_start
                mouse_moving = True

        # Handle mouse button releases
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                fps = 60
                # Copy the current screen to the second screen to preserve drawn figures
                second_screen.blit(screen, (0, 0))
                mouse_moving = False

        # Handle mouse motion
        if event.type == pygame.MOUSEMOTION:
            if mouse_moving:
                fps = 60
                # Update drawing or erasing based on mouse motion
                if index_tool in [0, 1, 3, 4, 5, 6]:
                    x_end = event.pos[0]
                    y_end = event.pos[1]
                    screen.blit(second_screen, (0, 0))
                    if index_tool == 0:
                        pygame.draw.rect(screen, colors[index_color], pygame.Rect(calculate_rectangle(x_start, y_start, x_end, y_end)), 1)
                    elif index_tool == 1:
                        pygame.draw.ellipse(screen, colors[index_color], pygame.Rect(calculate_rectangle(x_start, y_start, x_end, y_end)), 1)
                    elif index_tool == 3:
                        square_coords = draw_square(x_start, y_start, x_end, y_end)
                        pygame.draw.rect(screen, colors[index_color], pygame.Rect(square_coords), 1)
                    elif index_tool == 4:
                        right_triangle_coords = draw_right_triangle(x_start, y_start, x_end, y_end)
                        pygame.draw.polygon(screen, colors[index_color], right_triangle_coords, 1)
                    elif index_tool == 5:
                        equilateral_triangle_coords = draw_equilateral_triangle(x_start, y_start, x_end, y_end)
                        pygame.draw.polygon(screen, colors[index_color], equilateral_triangle_coords, 1)
                    elif index_tool == 6:
                        rhombus_coords = draw_rhombus(x_start, y_start, x_end, y_end)
                        pygame.draw.polygon(screen, colors[index_color], rhombus_coords, 1)
                if index_tool == 2:
                    x_start = x_end
                    y_start = y_end
                    x_end = event.pos[0]
                    y_end = event.pos[1]
                    pygame.draw.line(screen, "Black", (x_start, y_start), (x_end, y_end), 7)

    # Handle key presses for changing color and tool
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        fps = 7
        index_color += 1
        if index_color == len(colors):
            index_color = 0
        text_color = str("Color: " + str(colors[index_color]))
        text_color_surface = font.render(text_color, True, (255, 255, 255))

    if pressed[pygame.K_LEFT]:
        fps = 7
        index_color -= 1
        if index_color == -1:
            index_color = len(colors) - 1
        text_color = str("Color: " + str(colors[index_color]))
        text_color_surface = font.render(text_color, True, (255, 255, 255))

    if pressed[pygame.K_UP]:
        fps = 7
        index_tool += 1
        if index_tool == len(tools):
            index_tool = 0
        text_tool = str("Function: " + str(tools[index_tool]))
        text_tool_surface = font.render(text_tool, True, (255, 255, 255))

    if pressed[pygame.K_DOWN]:
        fps = 7
        index_tool -= 1
        if index_tool == -1:
            index_tool = len(tools) - 1
        text_tool = str("Function: " + str(tools[index_tool]))
        text_tool_surface = font.render(text_tool, True, (255, 255, 255))

    # Render menu surface with color and function information
    menu_surface = pygame.Surface((800, 30))
    menu_surface.fill((0, 0, 0))  # Black background for menu
    menu_surface.blit(text_color_surface, (1, 1))
    menu_surface.blit(text_tool_surface, (201, 1))

    # Draw menu on top of the screen
    screen.blit(menu_surface, (0, 0))

    # Update display and control FPS
    pygame.display.flip()
    clock.tick(fps)
