import pygame
import sys

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ERASER = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

drawing = False
last_pos = None
color = BLACK
radius = 5

def draw_circle(pos):
    pygame.draw.circle(screen, color, pos, radius)

def draw_rectangle(start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, 2)

def draw_square(start, size):
    pygame.draw.rect(screen, color, (start[0], start[1], size, size), 2)

def draw_right_triangle(start, size):
    points = [start, (start[0] + size, start[1]), (start[0], start[1] + size)]
    pygame.draw.polygon(screen, color, points, 2)

def draw_equilateral_triangle(start, size):
    points = [start, (start[0] + size, start[1]), (start[0] + size // 2, start[1] - size)]
    pygame.draw.polygon(screen, color, points, 2)

def draw_rhombus(start, width, height):
    points = [
        (start[0], start[1] - height // 2),
        (start[0] + width // 2, start[1]),
        (start[0], start[1] + height // 2),
        (start[0] - width // 2, start[1])
    ]
    pygame.draw.polygon(screen, color, points, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_e:
                color = ERASER
            if event.key == pygame.K_s:  # Draw square
                draw_square((100, 100), 50)
            if event.key == pygame.K_t:  # Draw right triangle
                draw_right_triangle((200, 100), 50)
            if event.key == pygame.K_y:  # Draw equilateral triangle
                draw_equilateral_triangle((300, 150), 50)
            if event.key == pygame.K_h:  # Draw rhombus
                draw_rhombus((400, 150), 60, 80)
    
    if drawing:
        draw_circle(pygame.mouse.get_pos())
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
