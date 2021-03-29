# Emily C's room
import pygame
from pygame.locals import MOUSEBUTTONDOWN, K_LEFT, K_RIGHT
import random

# Define some colors
BLACK = (0, 0, 0)
GRAY = (100, 94, 94)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BUTTONRED = (184, 70, 71)
OFFRED = (103, 50, 43)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Emily's level")

# images
pointer = pygame.image.load("pointer.png").convert_alpha()
firstbackground = pygame.image.load("background1.png").convert()
secondbackground = pygame.image.load("background2.png").convert()
character = pygame.image.load("character1.png").convert_alpha()
thirdbackground = pygame.image.load("background3.png").convert()
# animation
character_i = pygame.image.load("character2.png").convert_alpha()

# door
def door():
    pygame.draw.rect(screen, BLACK, [570, 0, 80, 220])
    pygame.draw.rect(screen, BLACK, [570, 500, 80, 220])
    pygame.draw.rect(screen, GRAY, [570, 220 - door_animation, 80, 140])
    pygame.draw.rect(screen, GRAY, [570, 360 + door_animation, 80, 140])
door_animation = 0
# door button
button = pygame.Rect(650, 530, 30, 100)

# speech bubble
def bubble():
    pygame.draw.rect(screen, WHITE, [bubble_x, bubble_y, 305, 170])

def instruction_one():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("There seems to be something", True, BLACK)
    screen.blit(text, [867, 165])
    text = font.render("wrong with the electricity.", True, BLACK)
    screen.blit(text, [867, 195])
    font = pygame.font.SysFont("Comic Sans", 23, False, False)
    text = font.render("Click anywhere to continue.", True, BLACK)
    screen.blit(text, [867, 239])

def instruction_two():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Click the red button to open", True, BLACK)
    screen.blit(text, [867, 180])
    text = font.render("the electricity room door", True, BLACK)
    screen.blit(text, [867, 205])

def firstdoor_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Uh oh! This door is locked!", True, BLACK)
    screen.blit(text, [895, 325])
    text = font.render("Looks like you will have to", True, BLACK)
    screen.blit(text, [895, 385])
    text = font.render("flip the switches to unlock it!", True, BLACK)
    screen.blit(text, [895, 415])
def seconddoor_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Nice! Door unlocked!", True, BLACK)
    screen.blit(text, [867, 150])

switch_i = 1
switch_ii = 2
switch_iii = 3
switch_iv = 4
switch_v = 5
switch_vi = 6

openswitch = [switch_i, switch_ii, switch_iii, switch_iv, switch_v, switch_vi]
choice_i = random.choice(openswitch)
openswitch.remove(choice_i)
choice_ii = random.choice(openswitch)
openswitch.remove(choice_ii)
choice_iii = random.choice(openswitch)

buttonoff_i = False
buttonoff_ii = False
buttonoff_iii = False
open_door = False
character_animation = True
character_animatio = False

done = False

first_stage = 1
start_instruction = 1
second_stage = 0
door_instruction = 1
third_stage = 0
fourthstage = 0

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            start_instruction += 1
            if second_stage == 1:
                door_instruction += 1
            x, y = event.pos
            print(x, y)

            if button.collidepoint(x, y) and start_instruction > 2:
                second_stage = 1

            if button.collidepoint(x, y) and open_door is True:
                door_animation += 5
                print(door_animation)


    # --- Game logic should go here

    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    # --- Screen-clearing code goes here

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    if first_stage == True:
        screen.blit(firstbackground, [0, 0])
        screen.blit(character, [700, 300])
        door()
        pygame.draw.rect(screen, BUTTONRED, [650, 530, 30, 100])
        bubble_x = 857
        bubble_y = 120
        bubble()

        if start_instruction == 1:
            instruction_one()
        if start_instruction >= 2:
            instruction_two()
            if open_door == True:
                seconddoor_instruction()

    if second_stage == True and open_door == False:
        first_stage = False
        screen.blit(secondbackground, [0, 0])
        bubble_x = 885
        bubble_y = 300
        bubble()
        if open_door == False and door_instruction >= 1:
            firstdoor_instruction()

        if choice_i == 1:
            button_i = pygame.draw.rect(screen, BUTTONRED, [404, 132, 50, 99])
        elif choice_i == 2:
            button_i = pygame.draw.rect(screen, BUTTONRED, [404, 313, 50, 99])
        elif choice_i == 3:
            button_i = pygame.draw.rect(screen, BUTTONRED, [404, 493, 50, 99])
        elif choice_i == 4:
            button_i = pygame.draw.rect(screen, BUTTONRED, [669, 131, 50, 99])
        elif choice_i == 5:
            button_i = pygame.draw.rect(screen, BUTTONRED, [669, 313, 50, 99])
        elif choice_i == 6:
            button_i = pygame.draw.rect(screen, BUTTONRED, [669, 493, 50, 99])

        if choice_ii == 1:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [404, 132, 50, 99])
        elif choice_ii == 2:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [404, 313, 50, 99])
        elif choice_ii == 3:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [404, 493, 50, 99])
        elif choice_ii == 4:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [669, 131, 50, 99])
        elif choice_ii == 5:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [669, 313, 50, 99])
        elif choice_ii == 6:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [669, 493, 50, 99])

        if choice_iii == 1:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [404, 132, 50, 99])
        elif choice_iii == 2:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [404, 313, 50, 99])
        elif choice_iii == 3:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [404, 493, 50, 99])
        elif choice_iii == 4:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [669, 131, 50, 99])
        elif choice_iii == 5:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [669, 313, 50, 99])
        elif choice_iii == 6:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [669, 493, 50, 99])

        if button_iii.collidepoint(x, y) and door_instruction > 1:
            choice_iii = 0
        if button_ii.collidepoint(x, y):
            choice_ii = 0
        if button_i.collidepoint(x, y):
            choice_i = 0

        if choice_i != 1 and choice_ii != 1 and choice_iii != 1:
            pygame.draw.rect(screen, OFFRED, [302, 132, 50, 99])
        if choice_i != 2 and choice_ii != 2 and choice_iii != 2:
            pygame.draw.rect(screen, OFFRED, [302, 313, 50, 99])
        if choice_i != 3 and choice_ii != 3 and choice_iii != 3:
            pygame.draw.rect(screen, OFFRED, [302, 493, 50, 99])
        if choice_i != 4 and choice_ii != 4 and choice_iii != 4:
            pygame.draw.rect(screen, OFFRED, [567, 131, 50, 99])
        if choice_i != 5 and choice_ii != 5 and choice_iii != 5:
            pygame.draw.rect(screen, OFFRED, [567, 313, 50, 99])
        if choice_i != 6 and choice_ii != 6 and choice_iii != 6:
            pygame.draw.rect(screen, OFFRED, [567, 493, 50, 99])

        if choice_i == 0 and choice_ii == 0 and choice_iii == 0:
            open_door = True
            first_stage = True

    if door_animation == 100:
        second_stage = False
        first_stage = False
        third_stage = 1

    # second part
    if third_stage == 1:
        screen.blit(thirdbackground, [0, 0])
        screen.blit(character_i, [300, 250])




    screen.blit(pointer, [mouse_x - 26, mouse_y - 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


#
#
#
# Oscar Sun's Room
import pygame
pygame.font.init()
# for fonts: https://coderslegacy.com/python/pygame-font/ 
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
import math
import random
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)
GREY = (146, 160, 173)
ORANGE = (206, 120, 11)
LIGHT_YELLOW = (242, 238, 208)
CAMERA_GREEN = (0, 255, 187)
CAMERA_YELLOW = (255, 217, 0)
SPACE_BLUE = (44, 3, 252)
PURPLE = (149, 0, 255)
PI = math.pi
bulb_color = BLACK
opacity = 50
opacity_2 = 200
radius = 1
light_bulb_part = True
camera_part = False
frame = 0
first_time = 0
start_radius = 0
# for convenience
test_thing = False
font = pygame.font.SysFont('verdana', 20)

def draw_battery(screen, x, y, length, width):
    pygame.draw.rect(screen, GREY, [x, y, length, width])
    pygame.draw.polygon(screen, ORANGE, [[x,y], [x+2/5*length,y], [x+3/5*length,y+width], [x,y+width]])
    pygame.draw.rect(screen, GREY, [x+length,y+1/5*width,0.1*length,0.6*width])
    

def draw_lightbulb(screen, x, y, opacity):
    pygame.draw.rect(screen, LIGHT_YELLOW, [x, y, 200, 100])
    for i in range (x, x+100, 20):
        pygame.draw.line(screen, BLACK, [x,y+i-x], [x+200,y+i-x],10)
    draw_rect_alpha(screen, (153, 208, 255, opacity), [x,y+100,200,150])
    draw_circle_alpha(screen, (153,208,255,opacity),[x+100,y+362],150)
    pygame.draw.line(screen, bulb_color, [x+100, y+250],[x+30,y+350],7)
    pygame.draw.line(screen, bulb_color, [x+170, y+400],[x+30,y+350],7)
    pygame.draw.line(screen, bulb_color, [x+170, y+400],[x+50,y+430],7)
    pygame.draw.line(screen, bulb_color, [x+150, y+470],[x+50,y+430],7)
    pygame.draw.line(screen, bulb_color, [x+150, y+470],[x+70,y+490],7)

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
    pygame.draw.line(screen, list[18], [x+350,y+350],[570,y+350],5)
    draw_battery(screen,x+100,y+300,250,100)
    
def draw_camera(screen, x, y, radius):
    pygame.draw.rect(screen, WHITE, [x,y,1000,500])
    pygame.draw.rect(screen, CAMERA_GREEN, [x,y+50,1000,400])
    pygame.draw.rect(screen, CAMERA_GREEN, [x+30,y-50,150,50])
    pygame.draw.polygon(screen, CAMERA_GREEN, [[x+300,y],[x+700,y],[x+600,y-50],[x+400,y-50]])
    pygame.draw.rect(screen, CAMERA_GREEN, [x+820,y-50,150,50])
    pygame.draw.rect(screen, WHITE, [x+450,y-40,100,30])
    pygame.draw.rect(screen, WHITE, [x+800,y+150,150,50])
    pygame.draw.circle(screen, CAMERA_YELLOW, [x+500,y+250], 230)
    pygame.draw.circle(screen, BLACK, [x+500,y+250], radius)
    pygame.draw.circle(screen, BLUE, [x+890,y+340], 80)
    instruction = font.render("CLICK HERE", True, WHITE)
    screen.blit(instruction, [x+830, y+340])

def distance(x, y):
    center_x = x + 135/2
    center_y = y + 75/2
    distance = math.sqrt((640-center_x)**2 + (335-center_y)**2)
    return round(distance)
    
WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
button_click = 0
button = pygame.Rect(1030,350,200,200)
click = 0
position = [0, 0]
rect_x = 0
rect_y = 0
points = 0

image = pygame.image.load("among_us.png").convert_alpha()
ufo = pygame.image.load("ufos (2).jpg").convert()
ufo.set_colorkey(BLACK)
ufo_2 = pygame.image.load("ufos (3).jpg").convert()
ufo_2.set_colorkey(BLACK)
pygame.display.set_caption("Oscar's room")

start_ticks=pygame.time.get_ticks()

running = True

# ---------------------------
while running:
    # for convenience
    if light_bulb_part and test_thing:
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
                if i == 14:
                    bulb_color = WHITE


        if click == 0:
            bulb_color = BLACK
            opacity = 50
        
        
        window.fill(BLACK)

        if bulb_color == WHITE:
            if opacity < 250:
                opacity += 1
            draw_circle_alpha(window, (242, 238, 208, opacity_2), [800,372], 150+radius)
            radius += 10
            if opacity_2 >= 10:
                opacity_2 -= 5
            else:
                radius = 1
                opacity_2 = 200
            if radius >= 150:
                draw_circle_alpha(window, (242, 238, 208, opacity_2), [800,372], 20+radius)
        draw_lightbulb(window, 700, 10, opacity)
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

        if wire_color[19] == WHITE:
            light_bulb_part = False
            camera_part = True


    # for convenience
    camera_part = True
    if camera_part:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = math.sqrt((mouse_x-1030) ** 2 + (mouse_y-425) ** 2)
                print(distance(rect_x, rect_y))
                ufo_camera = 0
                if distance <= 80 and ufo_camera <= 100+start_radius:
                    points += 10
                elif distance <= 80 and ufo_camera > 100+start_radius:
                    points -= 5



        first_time += 1
        print(first_time)
        if first_time == 1:
            window.fill(LIGHT_YELLOW)
            font_1 = pygame.font.SysFont("verdana", 30, False, True)
            instruction_1 = font_1.render("Congratulations, you've turned on the light bulb!", True, BLACK)
            instruction_2 = font_1.render("Now see what's inside this room", True, BLACK)
            instruction_3 = font_1.render("You need to use the camera to capture UFO and get 150 points", True, BLACK)
            instruction_4 = font_1.render("Once you've done the task, collect one key leading to the final room", True, BLACK)
            window.blit(instruction_1, [200, 200])
            window.blit(instruction_2, [200, 250])
            window.blit(instruction_3, [200, 300])
            window.blit(instruction_4, [200, 350])
            window.blit(image, position)
            time.sleep(10)
        else:
            window.fill(BLACK)
            frame += 1
            if frame // 100 == 0 and start_radius<=100:
                start_radius += 0.5
            elif start_radius >100:
                start_radius -= 0.5
            draw_camera(window, WIDTH/2-1000/2, HEIGHT/2-550/2, 100+start_radius)
            camera_button = pygame.Rect(WIDTH/2-1000/2,HEIGHT/2-550/2,80,80)
            if frame // 10000 == 0:
                y_coor = random.randrange(335-100-round(start_radius - 1), 335+100+round(start_radius - 1))
                if (start_radius+100)**2 - (y_coor-335) **2 < 0:
                    print((y_coor-335) **2)
                    print((start_radius+100)**2)
                    print(start_radius+100)
                    print(y_coor-335)
                    print((start_radius+100)**2 - (y_coor-335) **2)
                x_min = -1 * math.sqrt((start_radius+100)**2 - (y_coor-335) **2) + 640
                x_max = math.sqrt((start_radius+100)**2 - (y_coor-335) **2) + 640
                plus_what = 0
            
            if x_min+plus_what < x_max:
                window.blit(ufo_2, [x_min+plus_what, y_coor])
                rect_x = x_min + plus_what
                rect_y = y_coor
                plus_what += 1




    pygame.display.flip()
    clock.tick(30)

pygame.quit()

#Max's room

import pygame
import random

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
LIGHTGREY = (181, 181, 181)
GREEN = (0, 255, 0)
DARKGREEN = (63, 166, 31)
DARKGREY = (64, 64, 64)
YELLOW = (255, 242, 0)
RED = (207, 146, 136)
DARKRED = (255, 0, 0)

passcode_menu = False
passcode_check = False
have_key = False
screen_menu = False

speed_x = 0
speed_y = 0

speed_x2 = 0
speed_y2 = 0

y = 100
x = 100

count = 0
ship_screen = 0

timer = 0
passcode = ""
passcode_length = 0

passcode_area = pygame.Rect(600, 0, 100, 100)
creeper = pygame.Rect(x, y, 80, 80)
key_area = pygame.Rect(575, 550, 75, 50)
screen_one_area = pygame.Rect(1190, 175, 20, 100)
screen_two_area = pygame.Rect(1190, 365, 20, 100)
screen_three_area = pygame.Rect(1190, 550, 20, 100)

pygame.init()

size = [1280, 720]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Segoe UI', 16, False, False)
font_two = pygame.font.SysFont('MV Boli', 69, False, False)
font_three = pygame.font.SysFont('Segoe UI', 375, False, False)

def collision(obj_one, obj_two):
    if obj_one.colliderect(obj_two): 
        return True
    
def draw_key():
    pygame.draw.rect(screen, YELLOW, [600, 570, 35, 5])
    pygame.draw.circle(screen, YELLOW, [600, 572], 10)
    pygame.draw.rect(screen, YELLOW, [615, 570, 5, 10])
    pygame.draw.rect(screen, YELLOW, [625, 570, 5, 10])
    
def draw_door():
    pygame.draw.rect(screen, DARKGREY, [750, 0, 200, 150])
    pygame.draw.line(screen, BLACK, [850, 0], [850, 150])
    for x in range(760, 861, 100):
        for y in range(10, 81, 70):
            pygame.draw.rect(screen, LIGHTGREY, [x, y, 80, 60])
            
def draw_creeperface(screen, x, y):
    creeper.x = x 
    creeper.y = y
    pygame.draw.rect(screen, GREEN, creeper)
    pygame.draw.rect(screen, BLACK, [x + 10, y + 20, 20, 20])
    pygame.draw.rect(screen, BLACK, [x + 50, y + 20, 20, 20])
    pygame.draw.rect(screen, BLACK, [x + 30, y + 40, 20, 20])
    pygame.draw.rect(screen, BLACK, [x + 20, y + 50, 20, 20])
    pygame.draw.rect(screen, BLACK, [x + 40, y + 50, 20, 20])
    pygame.draw.rect(screen, BLACK, [x + 50, y + 70, 10, 10])
    pygame.draw.rect(screen, BLACK, [x + 20, y + 70, 10, 10])

def draw_lock():
    pygame.draw.rect(screen, LIGHTGREY, [350, 10, 500, 700])
    pygame.draw.rect(screen, WHITE, [370, 30, 460, 100])
    for x in range(410, 691, 140):
        for y in range(170, 451, 140):
            pygame.draw.rect(screen, BLACK, [x, y, 100, 100])
    pygame.draw.rect(screen, BLACK, [550, 585, 100, 100])

def draw_table():
    pygame.draw.rect(screen, (179, 126, 118), [410, 400, 480, 275])
    pygame.draw.rect(screen, GREY, [400, 400, 500, 200])
    pygame.draw.rect(screen, DARKGREEN, [450, 450, 400, 100])
    pygame.draw.rect(screen, LIGHTGREY, [400, 600, 500, 25])
    pygame.draw.rect(screen, DARKGREY, [500, 625, 300, 20])
    clue_one = font.render("h _ _ _", True, BLACK)
    screen.blit(clue_one, [455, 525])
    for i in range(50):
        x = random.randrange(455, 846)
        y = random.randrange(455, 546)
        pygame.draw.circle(screen, WHITE, [x, y], 1)
    
def draw_background():
    pygame.draw.rect(screen, GREY, [0, 0, 1280, 150])
    pygame.draw.rect(screen, GREY, [0, 0, 75, 720])
    pygame.draw.rect(screen, GREY, [1205, 0, 75, 720])
    pygame.draw.line(screen, BLACK, [0,0], [75, 150], 2)
    pygame.draw.line(screen, BLACK, [1280, 0], [1205, 150], 2)
    pygame.draw.line(screen, BLACK, [75, 150], [1205, 150], 2)
    pygame.draw.line(screen, BLACK, [75, 150], [75, 720], 2)
    pygame.draw.line(screen, BLACK, [1205, 150], [1205, 720], 2)
    #lock
    pygame.draw.rect(screen, LIGHTGREY, [625, 30, 50, 70])
    pygame.draw.rect(screen, WHITE, [635, 40, 30, 10])
    for x in range(635, 656, 20):
        for y in range(60, 81, 20):
            pygame.draw.rect(screen, BLACK, [x, y, 10, 10])
    #vent
    pygame.draw.rect(screen, (194, 207, 205), [100, 200, 100, 100])
    for y in range(215, 276, 20):
        pygame.draw.rect(screen, DARKGREY, [125, y, 50, 10])
    #screens
    pygame.draw.polygon(screen, DARKGREEN, ([1260, 75], [1225, 150], [1225, 300], [1260, 250]))
    pygame.draw.polygon(screen, DARKGREEN, ([1260, 290], [1225, 340], [1225, 475], [1260, 525]))
    pygame.draw.polygon(screen, DARKGREEN, ([1260, 565], [1225, 510], [1225, 675], [1260, 750]))
    #chairs
    y = 0
    for i in range(3):
        pygame.draw.rect(screen, (200, 88, 72), [1075, 175 + y, 100, 100])
        pygame.draw.rect(screen, (171, 64, 50), [1075, 150 + y, 50, 100])
        pygame.draw.rect(screen, (217, 88, 72), [1075, 250 + y, 100, 40])
        pygame.draw.circle(screen, (171, 64, 50), [1100, 150 + y], 25)
        y += 200
    
def not_offscreen(x, y, a, b, c, d):
    if x < a:
        x = a
    elif x > b:
        x = b
    
    if y < c:
        y = c
    elif y > d:
        y = d
        
    return x, y

def table_collision(x, y):
    if x > 320 and x < 326 and y > 320 and y < 565:
        x = 320
    elif x < 900 and x > 894 and y > 320 and y < 565:
        x = 900
    
    if y > 320 and y < 326 and x > 320 and x < 900:
        y = 320
    elif y < 565 and y > 549 and x > 320 and x < 900:
        y = 565
        
    return x, y

room_3 = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not room_3:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            room_3 = True
            
        elif event.type == pygame.KEYDOWN:
            
            if count == 0:
                if event.key == pygame.K_w:
                    speed_y = -5
                elif event.key == pygame.K_a:
                    speed_x = -5
                elif event.key == pygame.K_s:
                    speed_y2 = 5
                elif event.key == pygame.K_d:
                    speed_x2 = 5
                
                elif event.key == pygame.K_f:
                    if collision(creeper, passcode_area) == True:
                        count = 1
                        passcode_menu = True
                    elif collision(creeper, key_area) ==  True:
                        have_key = True
                    elif collision(creeper, screen_one_area) == True:
                        count = -1
                        screen_menu = True
                    elif collision(creeper, screen_two_area) == True:
                        count = -1
                        screen_menu = True
                    elif collision(creeper, screen_three_area) == True:
                        count = -1
                        screen_menu = True
                        
            elif count == 1:
                passcode += event.unicode
                passcode_length += 1
                if passcode_length >= 4:
                    count = 2
                    
            elif count == 2:
                if event.key == pygame.K_RETURN:
                    passcode_check = True
                    
            if event.key == pygame.K_ESCAPE:
                passcode_menu = False
                screen_menu = False
                count = 0
                passcode = ""
                passcode_length = 0
                ship_screen = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed_y = 0
            elif event.key == pygame.K_s:
                speed_y2 = 0
            elif event.key == pygame.K_a:
                speed_x = 0
            elif event.key == pygame.K_d:
                speed_x2 = 0  
                
    # --- Game Logic
    x += speed_x + speed_x2
    y += speed_y + speed_y2
    
    x, y = not_offscreen(x, y, 75, 1125, 70, 640)
    x, y = table_collision(x, y)
    # --- Drawing Code

    screen.fill(RED)
    
    draw_background()
    draw_table()
    draw_door()
    
    #Key
    if have_key == False:
        draw_key()
        if collision(creeper, key_area) == True:
            message = font.render("F to pick up", True, BLACK)
            screen.blit(message, [575, 544])
        
    draw_creeperface(screen, x, y)
    
    #screens
    if collision(creeper, screen_one_area) == True:
        message = font.render("F to inspect", True, BLACK)
        screen.blit(message, [1196, 175])
        ship_screen = 1
    elif collision(creeper, screen_two_area) == True:
        message = font.render("F to inspect", True, BLACK)
        screen.blit(message, [1196, 375])
        ship_screen = 2
    elif collision(creeper, screen_three_area) == True:
        message = font.render("F to inspect", True, BLACK)
        screen.blit(message, [1196, 575])
        ship_screen = 3
        
    if screen_menu == True:
        pygame.draw.rect(screen, DARKGREEN, [125, 75, 1024, 576])
        clue_two = font_three.render("_ _ 5 _", True, BLACK)
        screen.blit(clue_two, [150, 75])
        if ship_screen == 1:
            pygame.draw.rect(screen, DARKGREEN, [125, 75, 1024, 250])
            pygame.draw.rect(screen, DARKGREEN, [125, 450, 1024, 192])
        elif ship_screen == 2:
            pygame.draw.rect(screen, DARKGREEN, [125, 325, 1024, 250])
            pygame.draw.rect(screen, DARKGREEN, [125, 450, 1024, 192])
        elif ship_screen == 3:
            pygame.draw.rect(screen, DARKGREEN, [125, 75, 1024, 250])
            pygame.draw.rect(screen, DARKGREEN, [125, 267, 1024, 192])
            
            
    
    #Passcode lock
    if collision(creeper, passcode_area) == True:
        message = font.render("F to interact", True, BLACK)
        screen.blit(message, [610, 0])
    
    if passcode_menu == True:
        draw_lock()
        passcode_text = font_two.render(passcode, True, BLACK)
        screen.blit(passcode_text, [520, 30])
        
    if passcode_check == True:
        if passcode == "h254":
            pygame.draw.rect(screen, WHITE, [370, 30, 460, 100])
            correct = font_two.render("Correct", True, GREEN)
            screen.blit(correct, [475, 30])
            timer += 1
            if timer == 60:
                timer = 0
                room_3 = True
        else:
            passcode = ""
            passcode_length = 0
            incorrect = font_two.render("Incorrect", True, DARKRED)
            screen.blit(incorrect, [450, 30])
            timer += 1
            if timer == 60:
                timer = 0
                count = 1
                passcode_check = False 
        
    pygame.display.flip()
 
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
