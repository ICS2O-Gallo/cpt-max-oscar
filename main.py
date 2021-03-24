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

def draw_battery(screen, x, y, length, width):
    pygame.draw.rect(screen, GREY, [x, y, length, width])
    pygame.draw.polygon(screen, ORANGE, [[x,y], [x+2/5*length,y], [x+3/5*length,y+width], [x,y+width]])
    pygame.draw.rect(screen, GREY, [x+length,y+1/5*width,0.1*length,0.6*width])
    

def draw_lightbulb(screen, x, y, opacity):
    pygame.draw.rect(screen, LIGHT_YELLOW, [x, y, 200, 100])
    for i in range (x, x+100, 20):
        pygame.draw.line(screen, BLACK, [x,y+i-x], [x+200,y+i-x],10)
    draw_rect_alpha(screen, (250, 250, 250, opacity), [x,y+100,200,150])
    draw_circle_alpha(screen, (250,250,250,opacity),[x+100,y+423],200)
    pygame.draw.line(screen, BLACK, [x+100, y+250],[x+30,y+350],7)
    pygame.draw.line(screen, BLACK, [x+170, y+400],[x+30,y+350],7)
    pygame.draw.line(screen, BLACK, [x+170, y+400],[x+50,y+430],7)
    pygame.draw.line(screen, BLACK, [x+150, y+470],[x+50,y+430],7)
    pygame.draw.line(screen, BLACK, [x+150, y+470],[x+70,y+490],7)
    pygame.draw.line(screen, BLACK, [x+120, y+510],[x+70,y+490],7)

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)

def draw_circuit(screen, x, y, list):
    pygame.draw.rect(screen, WHITE, [x, y, 450, 450], 10)
    pygame.draw.line(screen, list[1], [x+100,y+350],[x+50,y+350],5)
    pygame.draw.line(screen, list[1], [x+50,y+350],[x+50,y+50],5)
    pygame.draw.line(screen, list[2], [x+50,y+50],[x+150,y+50],5)
    pygame.draw.line(screen, list[3], [x+150,y+50],[x+150,y+250],5)
    pygame.draw.line(screen, list[4], [x+250,y+250],[x+150,y+250],5)
    pygame.draw.line(screen, list[5], [x+250,y+250],[x+250,y+70],5)
    pygame.draw.line(screen, list[6], [x+300,y+70],[x+250,y+70],5)
    pygame.draw.line(screen, list[7], [x+300,y+70],[x+300,y+200],5)
    pygame.draw.line(screen, list[8], [x+350,y+200],[x+300,y+200],5)
    pygame.draw.line(screen, list[9], [x+350,y+200],[x+350,y+100],5)
    pygame.draw.line(screen, list[10], [x+175,y+100],[x+350,y+100],5)
    pygame.draw.line(screen, list[11], [x+175,y+100],[x+175,y+30],5)
    pygame.draw.line(screen, list[12], [x+400,y+30],[x+175,y+30],5)
    pygame.draw.line(screen, list[13], [x+400,y+30],[x+400,260],5)
    pygame.draw.line(screen, list[14], [800,260],[x+400,260],5)
    pygame.draw.line(screen, list[15], [800,260],[1100,260],5)
    pygame.draw.line(screen, list[16], [1100,260],[1100,150],5)
    pygame.draw.line(screen, list[17], [570,150],[1100,150],5)
    pygame.draw.line(screen, list[18], [570,150],[570,y+350],5)
    pygame.draw.line(screen, list[19], [x+350,y+350],[570,y+350],5)
    draw_battery(screen,x+100,y+300,250,100)
    
    
WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
button_click = 0
button = pygame.Rect(1030,350,200,200)
click = 0

pygame.display.set_caption("Oscar's room")
font = pygame.font.SysFont('verdana', 20)

start_ticks=pygame.time.get_ticks()

running = True

# ---------------------------
while running:
    seconds = round(pygame.time.get_ticks() - start_ticks / 1000)
    wire_color = [GREY] * 20
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = math.sqrt((mouse_x-1130) ** 2 + (mouse_y-450) ** 2)
            if distance <= 100:
                click = 1
            else:
                click = 0
                button_click = 0
    
    button_click += click
    for i in range (0, 20):
        if button_click > 50 * i:
            for j in range(0, i):
                wire_color[i] = WHITE
    print(wire_color[0])
    
    
    window.fill(BLACK)
    draw_lightbulb(window, 700, 10, 200)
    draw_circuit(window, 20, 20, wire_color)
    pygame.draw.circle(window, RED, [1130, 450],100)

    font_1 = pygame.font.SysFont("verdana", 20, True, True)
    instruction_1 = font_1.render("The light bulb in this room is disconnected from electricity.", True, WHITE)
    window.blit(instruction_1, [10, 500])
    instruction_2 = font_1.render("You need to reconnect electricity and make it shine", True, WHITE)
    window.blit(instruction_2, [10, 530])
    instruction_2 = font_1.render("before you see what's inside this room.", True, WHITE)
    window.blit(instruction_2, [10, 560])
    instruction_3 = font_1.render("CLICK HERE", True, BLACK)
    window.blit(instruction_3, [1070,450])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
