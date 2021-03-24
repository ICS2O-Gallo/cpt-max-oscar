# Oscar Sun's Room
import pygame
pygame.font.init()
# for fonts: https://coderslegacy.com/python/pygame-font/ 
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
import math
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)
GREY = (146, 160, 173)
ORANGE = (206, 120, 11)
LIGHT_YELLOW = (242, 238, 208)
PI = math.pi

def draw_battery(x, y, length, width):
    pygame.draw.rect(screen, GREY, [x, y, length, width])
    pygame.draw.polygon(screen, ORANGE, [[x,y], [x+2/5*length,y], [x+3/5*length,y+width], [x,y+width]])
    pygame.draw.rect(screen, GREY, [x+length,y+1/5*width,0.1*length,0.6*width])

def draw_lightbulb(screen, x, y):
    position = [x, y]
    light_bulb = pygame.image.load("light bulb 2.png").convert()
    screen.blit(light_bulb, position)

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

pygame.display.set_caption("Oscar's room")
font = pygame.font.SysFont('verdana', 20)

start_ticks=pygame.time.get_ticks()

running = True

# ---------------------------
while running:
    seconds = round(pygame.time.get_ticks() - start_ticks / 1000)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    screen.fill(BLACK)
    draw_lightbulb(screen, 100, 100)

    font_1 = pygame.font.SysFont("verdana", 20, True, True)
    instruction_1 = font_1.render("The light bulb in this room is disconnected from electricity.", True, WHITE)
    screen.blit(instruction_1, [10, 500])
    instruction_2 = font_1.render("You need to reconnect electricity and make it shine", True, WHITE)
    screen.blit(instruction_2, [10, 530])
    instruction_2 = font_1.render("before you see what's inside this room.", True, WHITE)
    screen.blit(instruction_2, [10, 560])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
