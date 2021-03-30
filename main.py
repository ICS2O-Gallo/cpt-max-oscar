# Oscar Sun's Menu
import pygame

pygame.font.init()
# for fonts: https://coderslegacy.com/python/pygame-font/ 
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
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
opacity = 255
opacity_2 = 255
opacity_3 = 255
opacity_4 = 255
opacity_5 = 255
opacity_6 = 255
opacity_7 = 255
font = pygame.font.SysFont('verdana', 20)

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

start_ticks = pygame.time.get_ticks()
image = pygame.image.load("background (1).jpg").convert()
image_2 = pygame.image.load("among_us_background.jpg").convert()

room = 0
# ---------------------------
while room == 0:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
        elif event.type == QUIT:
            pygame.quit()
    window.blit(image_2, [0, 0])
    font_1 = pygame.font.SysFont("verdana", 50, True, True)
    instruction_1 = font_1.render("Welcome to Among One !!", True, WHITE)
    font_2 = pygame.font.SysFont("verdana", 25, True, True)
    font_3 = pygame.font.SysFont("verdana", 100, True, True)
    game_title = font_3.render("Among", True, RED)
    window.blit(game_title, [830, 190])
    game_title_2 = font_3.render("One", True, RED)
    window.blit(game_title_2, [860, 290])
    instruction_2 = font_2.render("Unfortunately, you are trapped in a spaceship by yourself,", True, WHITE)
    instruction_3 = font_2.render(
        "and from the sound of the alarm, there is something seriously wrong with the engine.", True, WHITE)
    instruction_4 = font_2.render("More unfortunately, you need three keys to unlock the engine room to fix the engine",
                                  True, WHITE)
    instruction_5 = font_2.render("and the keys are distributed in three different rooms.", True, WHITE)
    instruction_6 = font_2.render(
        "To fix the engine, you would need to complete the tasks in three different rooms and gather the keys.", True,
        WHITE)
    instruction_7 = font_2.render("Time is urgent, quickly start by going into the first room !", True, WHITE)
    instruction_1.set_alpha(opacity)
    window.blit(instruction_1, [10, 10])
    if opacity != 0:
        opacity -= 5
    if opacity == 0:
        instruction_2.set_alpha(opacity_2)
        window.blit(instruction_2, [10, 10])
        if opacity_2 != 0:
            opacity_2 -= 1
        if opacity_2 == 0:
            instruction_3.set_alpha(opacity_3)
            window.blit(instruction_3, [10, 10])
            if opacity_3 != 0:
                opacity_3 -= 1
            if opacity_3 == 0:
                instruction_4.set_alpha(opacity_4)
                window.blit(instruction_4, [10, 10])
                if opacity_4 != 0:
                    opacity_4 -= 1
                if opacity_4 == 0:
                    instruction_5.set_alpha(opacity_5)
                    window.blit(instruction_5, [10, 10])
                    if opacity_5 != 0:
                        opacity_5 -= 1
                    if opacity_5 == 0:
                        instruction_6.set_alpha(opacity_6)
                        window.blit(instruction_6, [10, 10])
                        if opacity_6 != 0:
                            opacity_6 -= 1
                        if opacity_6 == 0:
                            instruction_7.set_alpha(opacity_7)
                            window.blit(instruction_7, [10, 10])
                            opacity_7 -= 1
                            print(opacity_7)
                            if opacity_7 == 0:
                                room = 1

    pygame.display.flip()
    clock.tick(30)

# Emily Cheng's Room

import pygame
from pygame.locals import MOUSEBUTTONDOWN
import random

# colours
BLACK = (0, 0, 0)
GRAY = (100, 94, 94)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BUTTONRED = (184, 70, 71)
OFFRED = (103, 50, 43)
# wire colours
YELLOW = (189, 157, 43)
BLUE = (47, 80, 156)
PINK = (163, 31, 159)
RED = (163, 31, 24)

pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Among one")

# images
pointer = pygame.image.load("pointer.png").convert_alpha()
firstbackground = pygame.image.load("background1.png").convert()
secondbackground = pygame.image.load("background2.png").convert()
character = pygame.image.load("character1.png").convert_alpha()
thirdbackground = pygame.image.load("background3.png").convert()
character_i = pygame.image.load("character2.png").convert_alpha()
thirdbackground_i = pygame.image.load("background3.5.png").convert()
fourthbackground = pygame.image.load("background4.png").convert()
lastbackground = pygame.image.load("background5.png").convert()

loading_i = pygame.image.load("loading.png").convert()
loading_ii = pygame.image.load("loading1.png").convert()
loading_iii = pygame.image.load("loading2.png").convert()
loading_iv = pygame.image.load("loading3.png").convert()


# door
def door():
    pygame.draw.rect(screen, GRAY, [570, 220 - door_animation, 80, 140])
    pygame.draw.rect(screen, GRAY, [570, 360 + door_animation, 80, 140])
    pygame.draw.rect(screen, BLACK, [570, 0, 80, 220])
    pygame.draw.rect(screen, BLACK, [570, 500, 80, 220])


door_animation = 0

# door button
button = pygame.Rect(650, 530, 30, 100)
# electrical button
electric_button = pygame.Rect(99, 256, 285, 145)
# yellow wire
yellow_wire = pygame.Rect(63, 76, 100, 70)
yellow_end = pygame.Rect(569, 542, 100, 70)
# blue wire
blue_wire = pygame.Rect(63, 226, 100, 70)
blue_end = pygame.Rect(569, 79, 100, 70)
# pink wire
pink_wire = pygame.Rect(63, 391, 100, 70)
pink_end = pygame.Rect(569, 390, 100, 70)
# red wire
red_wire = pygame.Rect(63, 531, 100, 70)
red_end = pygame.Rect(569, 229, 100, 70)


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


def thirdstage_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Now click the button to", True, BLACK)
    screen.blit(text, [667, 210])
    text = font.render("access the electrical.", True, BLACK)
    screen.blit(text, [667, 250])


def fourthstage_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Drag and drop the wires to", True, BLACK)
    screen.blit(text, [839, 300])
    text = font.render("fix the electricity.", True, BLACK)
    screen.blit(text, [839, 340])


def final_words():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Woohoo! We fixed the", True, BLACK)
    screen.blit(text, [839, 300])
    text = font.render("electricity!", True, BLACK)
    screen.blit(text, [839, 340])
    font = pygame.font.SysFont("Comic Sans", 23, False, False)
    text = font.render("Click anywhere to continue.", True, BLACK)
    screen.blit(text, [839, 380])


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

first_stage = 1
start_instruction = 1
second_stage = 0
door_instruction = 1
third_stage = 0
loading = True
timeloading = 0
fourthstage = 0
finish = 0

wire_draggingy = False
wire_draggingb = False
wire_draggingp = False
wire_draggingr = False
wire_complete = False

yellow_x = 107
yellow_y = 105

blue_x = 107
blue_y = 250

pink_x = 107
pink_y = 435

red_x = 107
red_y = 576

yellow = False
blue = False
pink = False
red = False

clock = pygame.time.Clock()

level_complete = False

# -------- Main Program Loop -----------
while room == 1:
    pygame.mouse.set_visible(0)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:

            if first_stage == 1 and loading is False:
                start_instruction += 1

            if second_stage == 1:
                door_instruction += 1
            x, y = event.pos
            print(x, y)

            if button.collidepoint(x, y) and start_instruction > 2:
                second_stage = 1

            if button.collidepoint(x, y) and open_door is True:
                if third_stage == 0:
                    door_animation += 20
                    print(door_animation)

            if electric_button.collidepoint(x, y) and third_stage == 1 and loading is False:
                loading = True
                third_stage = 0
                fourthstage = 1

            if wire_complete is True:
                fourthstage = 0
                finish = 1

            if fourthstage == 1 and loading is False and event.button == 1:

                if yellow is False:
                    if yellow_wire.collidepoint(x,
                                                y) and wire_draggingp is False and wire_draggingb is False and wire_draggingr is False:
                        wire_draggingy = True
                    if yellow_end.collidepoint(yellow_x, yellow_y):
                        wire_draggingy = False
                        yellow = True

                if blue is False:
                    if blue_wire.collidepoint(x,
                                              y) and wire_draggingp is False and wire_draggingy is False and wire_draggingr is False:
                        wire_draggingb = True
                    if blue_end.collidepoint(blue_x, blue_y):
                        wire_draggingb = False
                        blue = True

                if pink is False:
                    if pink_wire.collidepoint(x,
                                              y) and wire_draggingy is False and wire_draggingb is False and wire_draggingr is False:
                        wire_draggingp = True
                    if pink_end.collidepoint(pink_x, pink_y):
                        wire_draggingp = False
                        pink = True

                if red is False:
                    if red_wire.collidepoint(x,
                                             y) and wire_draggingp is False and wire_draggingb is False and wire_draggingy is False:
                        wire_draggingr = True
                    if red_end.collidepoint(red_x, red_y):
                        wire_draggingr = False
                        red = True

    # game logic

    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    if wire_draggingy is True:
        yellow_x = pygame.mouse.get_pos()[0]
        yellow_y = pygame.mouse.get_pos()[1]
    elif wire_draggingb is True:
        blue_x = pygame.mouse.get_pos()[0]
        blue_y = pygame.mouse.get_pos()[1]
    elif wire_draggingp is True:
        pink_x = pygame.mouse.get_pos()[0]
        pink_y = pygame.mouse.get_pos()[1]
    elif wire_draggingr is True:
        red_x = pygame.mouse.get_pos()[0]
        red_y = pygame.mouse.get_pos()[1]

    # --- Screen-clearing code goes here

    screen.fill(WHITE)

    if loading is True:
        timeloading += 1
        screen.blit(loading_i, [0, 0])
        if timeloading > 10:
            screen.blit(loading_ii, [0, 0])
        if timeloading > 30:
            screen.blit(loading_iii, [0, 0])
        if timeloading > 50:
            screen.blit(loading_iv, [0, 0])
        if timeloading > 70:
            timeloading = 0
            loading = False

    if first_stage == 1 and loading is False:
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
            if open_door is True:
                seconddoor_instruction()

    if second_stage == 1 and open_door is False:
        first_stage = 0
        screen.blit(secondbackground, [0, 0])
        bubble_x = 885
        bubble_y = 300
        bubble()
        if open_door is False and door_instruction >= 1:
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
            timeloading += 1
            if timeloading == 20:
                open_door = True
                first_stage = 1
                timeloading = 0

    if door_animation == 140:
        second_stage = 0
        first_stage = 0
        third_stage = 1
        loading = True
        door_animation = 0

    # second part
    if third_stage == 1 and loading is False:
        screen.blit(thirdbackground, [0, 0])
        if 99 < pygame.mouse.get_pos()[0] < 370 and 256 < pygame.mouse.get_pos()[1] < 387:
            screen.blit(thirdbackground_i, [0, 0])
        bubble_x = 650
        bubble_y = 150
        bubble()
        thirdstage_instruction()
        screen.blit(character_i, [300, 250])

    if fourthstage == 1 and loading is False:
        screen.blit(fourthbackground, [0, 0])
        if wire_complete is True:
            screen.blit(lastbackground, [0, 0])
        bubble_x = 821
        bubble_y = 253
        bubble()
        if wire_complete is False:
            fourthstage_instruction()
        else:
            final_words()

        pygame.draw.line(screen, OFFRED, (643, 393), (643, 469), 20)
        pygame.draw.line(screen, OFFRED, (643, 229), (643, 304), 20)
        pygame.draw.line(screen, OFFRED, (643, 77), (643, 151), 20)

        if yellow is True:
            pygame.draw.line(screen, YELLOW, (107, 105), (601, 570), 45)
            pygame.draw.line(screen, GREEN, (643, 541), (643, 609), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 541), (643, 609), 20)
        if wire_draggingy is True:
            pygame.draw.line(screen, YELLOW, (107, 105), (yellow_x, yellow_y), 45)

        if blue is True:
            pygame.draw.line(screen, BLUE, (107, 265), (601, 109), 45)
            pygame.draw.line(screen, GREEN, (643, 77), (643, 151), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 77), (643, 151), 20)
        if wire_draggingb is True:
            pygame.draw.line(screen, BLUE, (107, 265), (blue_x, blue_y), 45)

        if pink is True:
            pygame.draw.line(screen, PINK, (107, 430), (601, 431), 45)
            pygame.draw.line(screen, GREEN, (643, 392), (643, 468), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 393), (643, 469), 20)
        if wire_draggingp is True:
            pygame.draw.line(screen, PINK, (107, 430), (pink_x, pink_y), 45)

        if red is True:
            pygame.draw.line(screen, RED, (107, 576), (601, 270), 45)
            pygame.draw.line(screen, GREEN, (643, 229), (643, 304), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 229), (643, 304), 20)
        if wire_draggingr is True:
            pygame.draw.line(screen, RED, (107, 576), (red_x, red_y), 45)

        if red is True and blue is True and pink is True and yellow is True:
            timeloading += 1
            if timeloading == 20:
                wire_complete = True

    if finish == 1:
        room = 2

    screen.blit(pointer, [mouse_x - 26, mouse_y - 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)


#
#
#
# Oscar Sun's Room
import pygame

pygame.font.init()
# for fonts: https://coderslegacy.com/python/pygame-font/ 
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
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
instruction_part = False
camera_part = False
key_part = False
frame = 0
time = 0

first_time = 0
start_radius = 0
font = pygame.font.SysFont('verdana', 20)


def draw_battery(screen, x, y, length, width):
    pygame.draw.rect(screen, GREY, [x, y, length, width])
    pygame.draw.polygon(screen, ORANGE,
                        [[x, y], [x + 2 / 5 * length, y], [x + 3 / 5 * length, y + width], [x, y + width]])
    pygame.draw.rect(screen, GREY, [x + length, y + 1 / 5 * width, 0.1 * length, 0.6 * width])


def draw_lightbulb(screen, x, y, opacity):
    pygame.draw.rect(screen, LIGHT_YELLOW, [x, y, 200, 100])
    for i in range(x, x + 100, 20):
        pygame.draw.line(screen, BLACK, [x, y + i - x], [x + 200, y + i - x], 10)
    draw_rect_alpha(screen, (153, 208, 255, opacity), [x, y + 100, 200, 150])
    draw_circle_alpha(screen, (153, 208, 255, opacity), [x + 100, y + 362], 150)
    pygame.draw.line(screen, bulb_color, [x + 100, y + 250], [x + 30, y + 350], 7)
    pygame.draw.line(screen, bulb_color, [x + 170, y + 400], [x + 30, y + 350], 7)
    pygame.draw.line(screen, bulb_color, [x + 170, y + 400], [x + 50, y + 430], 7)
    pygame.draw.line(screen, bulb_color, [x + 150, y + 470], [x + 50, y + 430], 7)
    pygame.draw.line(screen, bulb_color, [x + 150, y + 470], [x + 70, y + 490], 7)


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
    pygame.draw.line(screen, list[1], [x + 100, y + 350], [x + 50, y + 350], 5)
    pygame.draw.line(screen, list[1], [x + 50, y + 350], [x + 50, y + 50], 5)
    pygame.draw.line(screen, list[2], [x + 50, y + 50], [x + 150, y + 50], 5)
    pygame.draw.line(screen, list[3], [x + 150, y + 50], [x + 150, y + 250], 5)
    pygame.draw.line(screen, list[4], [x + 250, y + 250], [x + 150, y + 250], 5)
    pygame.draw.line(screen, list[5], [x + 250, y + 250], [x + 250, y + 70], 5)
    pygame.draw.line(screen, list[6], [x + 300, y + 70], [x + 250, y + 70], 5)
    pygame.draw.line(screen, list[7], [x + 300, y + 70], [x + 300, y + 200], 5)
    pygame.draw.line(screen, list[8], [x + 350, y + 200], [x + 300, y + 200], 5)
    pygame.draw.line(screen, list[9], [x + 350, y + 200], [x + 350, y + 100], 5)
    pygame.draw.line(screen, list[10], [x + 175, y + 100], [x + 350, y + 100], 5)
    pygame.draw.line(screen, list[11], [x + 175, y + 100], [x + 175, y + 30], 5)
    pygame.draw.line(screen, list[12], [x + 400, y + 30], [x + 175, y + 30], 5)
    pygame.draw.line(screen, list[13], [x + 400, y + 30], [x + 400, 260], 5)
    pygame.draw.line(screen, list[14], [800, 260], [x + 400, 260], 5)
    pygame.draw.line(screen, list[15], [800, 260], [1100, 260], 5)
    pygame.draw.line(screen, list[16], [1100, 260], [1100, 150], 5)
    pygame.draw.line(screen, list[17], [570, 150], [1100, 150], 5)
    pygame.draw.line(screen, list[18], [570, 150], [570, y + 350], 5)
    pygame.draw.line(screen, list[18], [x + 350, y + 350], [570, y + 350], 5)
    draw_battery(screen, x + 100, y + 300, 250, 100)


def draw_camera(screen, x, y, radius):
    pygame.draw.rect(screen, WHITE, [x, y, 1000, 500])
    pygame.draw.rect(screen, CAMERA_GREEN, [x, y + 50, 1000, 400])
    pygame.draw.rect(screen, CAMERA_GREEN, [x + 30, y - 50, 150, 50])
    pygame.draw.polygon(screen, CAMERA_GREEN, [[x + 300, y], [x + 700, y], [x + 600, y - 50], [x + 400, y - 50]])
    pygame.draw.rect(screen, CAMERA_GREEN, [x + 820, y - 50, 150, 50])
    pygame.draw.rect(screen, WHITE, [x + 450, y - 40, 100, 30])
    pygame.draw.rect(screen, WHITE, [x + 800, y + 150, 150, 50])
    pygame.draw.circle(screen, CAMERA_YELLOW, [x + 500, y + 250], 230)
    pygame.draw.circle(screen, BLACK, [x + 500, y + 250], radius)
    pygame.draw.circle(screen, BLUE, [x + 890, y + 340], 80)
    instruction = font.render("CLICK HERE", True, WHITE)
    screen.blit(instruction, [x + 830, y + 340])


def draw_key(screen, x, y, color):
    pygame.draw.circle(screen, color, [x, y], 100)
    pygame.draw.rect(screen, color, [x + 90, y - 20, 180, 40])
    pygame.draw.rect(screen, color, [x + 140, y + 20, 20, 30])
    pygame.draw.rect(screen, color, [x + 200, y + 20, 20, 30])


def distance(x, y):
    center_x = x + 135 / 2
    center_y = y + 75 / 2
    distance = math.sqrt((640 - center_x) ** 2 + (335 - center_y) ** 2)
    return distance


WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
button_click = 0
button = pygame.Rect(1030, 350, 200, 200)
click = 0
position = [-100, 0]
rect_x = 0
rect_y = 0
points = 0
ufo_list = []
room = 2

image = pygame.image.load("among_us.png").convert_alpha()
ufo_2 = pygame.image.load("ufos (2).jpg").convert()
ufo_2.set_colorkey(BLACK)
pygame.display.set_caption("Oscar's room")

start_ticks = pygame.time.get_ticks()
pygame.mouse.set_visible(255)

# ---------------------------
while room == 2:
    if light_bulb_part:
        seconds = round(pygame.time.get_ticks() - start_ticks / 1000)
        wire_color = [GREY] * 20
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = math.sqrt((mouse_x - 1130) ** 2 + (mouse_y - 450) ** 2)
                if distance <= 100:
                    click = 1
                else:
                    click = 0
                    button_click = 0
            elif event.type == MOUSEBUTTONUP:
                click = 0

        button_click += click
        for i in range(0, 20):
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
            draw_circle_alpha(window, (242, 238, 208, opacity_2), [800, 372], 150 + radius)
            radius += 10
            if opacity_2 >= 10:
                opacity_2 -= 5
            else:
                radius = 1
                opacity_2 = 200
            if radius >= 150:
                draw_circle_alpha(window, (242, 238, 208, opacity_2), [800, 372], 20 + radius)
        draw_lightbulb(window, 700, 10, opacity)
        draw_circuit(window, 20, 20, wire_color)
        pygame.draw.circle(window, RED, [1130, 450], 100)

        font_1 = pygame.font.SysFont("verdana", 20, True, True)
        instruction_1 = font_1.render("The light bulb in this room is disconnected from electricity.", True, WHITE)
        window.blit(instruction_1, [10, 500])
        instruction_2 = font_1.render("You need to reconnect electricity and make it shine", True, WHITE)
        window.blit(instruction_2, [10, 530])
        instruction_4 = font_1.render("before you see what's inside this room.", True, WHITE)
        window.blit(instruction_4, [10, 560])
        instruction_3 = font_1.render("CLICK HERE", True, BLACK)
        window.blit(instruction_3, [1070, 450])

        if wire_color[19] == WHITE:
            light_bulb_part = False
            instruction_part = True

    if instruction_part:
        time += 1
        window.fill(LIGHT_YELLOW)
        font_1 = pygame.font.SysFont("verdana", 30, False, True)
        instruction_1 = font_1.render("Congratulations, you've turned on the light bulb!", True, BLACK)
        instruction_2 = font_1.render("Now see what's inside this room", True, BLACK)
        instruction_3 = font_1.render("You need to use the camera to capture UFO and get 150 points", True, BLACK)
        instruction_4 = font_1.render("Once you've done the task, collect one key leading to the final room", True,
                                      BLACK)
        window.blit(instruction_1, [300, 200])
        window.blit(instruction_2, [300, 250])
        window.blit(instruction_3, [300, 300])
        window.blit(instruction_4, [300, 350])
        window.blit(image, position)
        if time == 300:
            instruction_part = False
            camera_part = True
            time = 0

    if camera_part:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = math.sqrt((mouse_x - 1030) ** 2 + (mouse_y - 425) ** 2)
                center_x = rect_x + 135 / 2
                center_y = rect_y + 75 / 2
                ufo_camera = math.sqrt((640 - center_x) ** 2 + (335 - center_y) ** 2)
                if frame % 100 > 50 and frame % 100 <= 99:
                    points -= 5
                elif distance <= 80 and ufo_camera <= 100 + start_radius:
                    points += 10
                elif distance <= 80 and ufo_camera > 100 + start_radius:
                    points -= 5

        window.fill(BLACK)
        amount = 0
        frame += 1
        if start_radius <= 100:
            start_radius += 0.5
        if start_radius > 100:
            start_radius = 20
            start_radius -= 0.5
        draw_camera(window, WIDTH / 2 - 1000 / 2, HEIGHT / 2 - 550 / 2, 100 + start_radius)
        camera_button = pygame.Rect(WIDTH / 2 - 1000 / 2, HEIGHT / 2 - 550 / 2, 80, 80)
        if frame % 100 == 0:
            y_coor = random.randrange(335 - 100 - round(start_radius), 335 + 100 + round(start_radius))
            if ((start_radius + 100) ** 2 - (y_coor - 335) ** 2 > 0):
                x_min = -1 * math.sqrt((start_radius + 100) ** 2 - (y_coor - 335) ** 2) + 640
                x_max = math.sqrt((start_radius + 100) ** 2 - (y_coor - 335) ** 2) + 640
                x_coor = random.randrange(round(x_min + 1), round(x_max - 1))
                ufo_list.append([x_coor, y_coor])
        if len(ufo_list) != 0:
            if frame % 100 > 0 and frame % 100 < 50:
                window.blit(ufo_2, ufo_list[len(ufo_list) - 1])
                rect_x, rect_y = ufo_list[len(ufo_list) - 1]

        points_print = font_1.render(f"Your point right now is {points}", True, WHITE)
        window.blit(points_print, [10, 5])

        if points > 150:
            camera_part = False
            key_part = True

    if key_part:
        time += 1
        window.fill(BLACK)
        font_1 = pygame.font.SysFont("verdana", 30, False, True)
        congrat = font_1.render("Congratulations, you've completed the task in this room", True, WHITE)
        key_award = font_1.render("And you are awarded with one key!", True, WHITE)
        window.blit(congrat, [300, 200])
        window.blit(key_award, [300, 230])
        draw_key(window, 500, 400, LIGHT_YELLOW)
        window.blit(image, [-100, 10])
        print(time)
        if time == 300:
            room = 3
            print("lmao")

    pygame.display.flip()
    clock.tick(30)

# Max's room

import pygame
import random

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 51, 51)
LIGHTGREY = (181, 181, 181)
GREEN = (0, 255, 0)
DARKGREEN = (63, 166, 31)
DARKGREY = (64, 64, 64)
YELLOW = (255, 242, 0)
LIGHTYELLOW = (226, 227, 166)
LIGHTRED = (207, 146, 136)
DARKRED = (255, 0, 0)
BROWN = (133, 98, 68)
DARKBROWN = (94, 66, 42)
BLUE = (115, 195, 209)

passcode_menu = False
passcode_check = False
have_key = False
screen_menu = False
vault_menu = False
cabinet_menu = False

speed_x = 0
speed_y = 0

speed_x2 = 0
speed_y2 = 0

x = 300
y = 600

count = 0
ship_screen = 0

timer = 0
passcode = ""
passcode_length = 0

character = pygame.Rect(x, y, 80, 80)
passcode_area = pygame.Rect(600, 0, 100, 100)
key_area = pygame.Rect(575, 550, 75, 50)
screen_one_area = pygame.Rect(1190, 175, 20, 100)
screen_two_area = pygame.Rect(1190, 365, 20, 100)
screen_three_area = pygame.Rect(1190, 550, 20, 100)
vault_area = pygame.Rect(300, 30, 100, 75)
cabinet_area = pygame.Rect(75, 175, 50, 20)

pygame.init()

size = [1280, 720]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Segoe UI', 16, False, False)
font_two = pygame.font.SysFont('MV Boli', 69, False, False)
font_three = pygame.font.SysFont('Segoe UI', 375, False, False)
font_four = pygame.font.SysFont('Bahnschrift', 25, False, False)

# lists
instructions = ["WASD to move",
                "F to interact with items (a prompt will show up if you are close enough)",
                "ESC to close menu's",
                "You are trying to get to the next room",
                "Click anywhere to begin"]
prompts = ["F to pick up",
           "F to search",
           "Locked",
           "F to interact",
           "F to unlock",
           "F to inspect"]

endgame_credits = [
    "Developers: Oscar, Max, Emily",
    "Thanks for playing!",
    "As more unexpected events awaits, you continue on what seems like an endless journey through space...",
    "After getting past the 3 rooms, you made it to the fourth and managed fixed the engine."
]


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


def draw_character(screen, x, y):
    character.x = x
    character.y = y
    pygame.draw.rect(screen, RED, [x, y, 80, 70])
    pygame.draw.circle(screen, RED, [x + 40, y], 40)
    pygame.draw.rect(screen, RED, [x, y + 70, 30, 10])
    pygame.draw.rect(screen, RED, [x + 50, y + 70, 30, 10])
    pygame.draw.rect(screen, BLUE, [x + 30, y - 5, 20, 30])
    pygame.draw.circle(screen, BLUE, [x + 30, y + 10], 15)
    pygame.draw.circle(screen, BLUE, [x + 50, y + 10], 15)
    pygame.draw.circle(screen, WHITE, [x + 30, y + 5], 5)


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


def draw_vault():
    pygame.draw.rect(screen, LIGHTGREY, vault_area)
    pygame.draw.rect(screen, BLACK, vault_area, 2)
    # key hole
    pygame.draw.circle(screen, BLACK, [385, 60], 5)
    pygame.draw.polygon(screen, BLACK, ([385, 60], [390, 75], [380, 75]))


def draw_background():
    pygame.draw.rect(screen, GREY, [0, 0, 1280, 150])
    pygame.draw.rect(screen, GREY, [0, 0, 75, 720])
    pygame.draw.rect(screen, GREY, [1205, 0, 75, 720])
    pygame.draw.line(screen, BLACK, [0, 0], [75, 150], 2)
    pygame.draw.line(screen, BLACK, [1280, 0], [1205, 150], 2)
    pygame.draw.line(screen, BLACK, [75, 150], [1205, 150], 2)
    pygame.draw.line(screen, BLACK, [75, 150], [75, 720], 2)
    pygame.draw.line(screen, BLACK, [1205, 150], [1205, 720], 2)
    # cabinet
    pygame.draw.rect(screen, BROWN, [35, 70, 100, 75])
    pygame.draw.polygon(screen, DARKBROWN, ([35, 145], [75, 232], [134, 232], [134, 145]))
    pygame.draw.polygon(screen, BROWN, ([45, 150], [57, 177], [129, 177], [129, 150]))
    pygame.draw.polygon(screen, BROWN, ([59, 183], [71, 210], [129, 210], [129, 183]))
    pygame.draw.polygon(screen, BROWN, ([73, 216], [79, 228], [129, 228], [129, 216]))
    pygame.draw.circle(screen, BLACK, [90, 165], 5)
    pygame.draw.circle(screen, BLACK, [97, 197], 5)
    pygame.draw.circle(screen, BLACK, [102, 223], 5)
    pygame.draw.rect(screen, (179, 126, 118), [77, 233, 58, 100])

    # lock
    pygame.draw.rect(screen, LIGHTGREY, [625, 30, 50, 70])
    pygame.draw.rect(screen, WHITE, [635, 40, 30, 10])
    for x in range(635, 656, 20):
        for y in range(60, 81, 20):
            pygame.draw.rect(screen, BLACK, [x, y, 10, 10])
    # vent
    pygame.draw.rect(screen, (194, 207, 205), [100, 600, 100, 100])
    for y in range(615, 676, 20):
        pygame.draw.rect(screen, DARKGREY, [125, y, 50, 10])
    # screens
    pygame.draw.polygon(screen, DARKGREEN, ([1260, 75], [1225, 150], [1225, 300], [1260, 250]))
    pygame.draw.polygon(screen, DARKGREEN, ([1260, 290], [1225, 340], [1225, 475], [1260, 525]))
    pygame.draw.polygon(screen, DARKGREEN, ([1260, 565], [1225, 510], [1225, 675], [1260, 750]))
    # chairs
    y = 0
    for i in range(3):
        pygame.draw.rect(screen, (171, 64, 50), [1075, 150 + y, 50, 100])
        pygame.draw.rect(screen, (217, 88, 72), [1075, 250 + y, 100, 40])
        pygame.draw.rect(screen, (200, 88, 72), [1125, 175 + y, 50, 85])
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
    elif y > 320 and y < 326 and x > 320 and x < 900:
        y = 320
    elif y < 565 and y > 549 and x > 320 and x < 900:
        y = 565

    return x, y


def desk_collision(x, y):
    if y < 153 and x < 130:
        y = 153
    if x < 135 and y < 153:
        x = 135

    return x, y


room = 3
screen_ = 0

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while room == 3:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen_ == 0:
                screen_ = 1

        elif event.type == pygame.KEYDOWN:
            if screen_ == 1:
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
                        if collision(character, passcode_area):
                            count = 1
                            passcode_menu = True
                        elif collision(character, key_area):
                            have_key = True
                        elif collision(character, screen_one_area):
                            count = -1
                            screen_menu = True
                        elif collision(character, screen_two_area):
                            count = -1
                            screen_menu = True
                        elif collision(character, screen_three_area):
                            count = -1
                            screen_menu = True
                        elif collision(character, vault_area):
                            if have_key == True:
                                count = -1
                                vault_menu = True
                        elif collision(character, cabinet_area):
                            count = -1
                            cabinet_menu = True

                elif count == 1:
                    passcode += event.unicode
                    passcode_length += 1
                    if passcode_length == 4:
                        count = 2

                elif count == 2:
                    if event.key == pygame.K_RETURN:
                        passcode_check = True

                if event.key == pygame.K_ESCAPE:
                    passcode_menu = False
                    passcode_check = False
                    screen_menu = False
                    vault_menu = False
                    cabinet_menu = False
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
    x, y = desk_collision(x, y)

    # --- Drawing Code
    screen.fill(LIGHTRED)
    if screen_ == 0:
        # instructions page

        y_instruction = 0
        for i in range(4):
            message = font_four.render(instructions[i], True, BLACK)
            screen.blit(message, [200, 200 + y_instruction])
            y_instruction += 50

        message = font_four.render(instructions[4], True, BLACK)
        screen.blit(message, [200, 600])

    elif screen_ == 1:
        draw_background()
        draw_table()
        draw_door()
        draw_vault()

        # Key
        if not have_key:
            draw_key()
            if collision(character, key_area):
                message = font.render(prompts[0], True, BLACK)
                screen.blit(message, [575, 544])

        draw_character(screen, x, y)

        # cabinet
        if collision(character, cabinet_area):
            message = font.render(prompts[1], True, BLACK)
            screen.blit(message, [50, 120])

        if cabinet_menu:
            pygame.draw.rect(screen, WHITE, [125, 75, 1024, 576])
            clue_four = font_three.render("_ _ _ t", True, BLACK)
            screen.blit(clue_four, [150, 75])

        # vault
        if collision(character, vault_area):
            if have_key:
                message = font.render(prompts[4], True, BLACK)
                screen.blit(message, [315, 5])
            else:
                message = font.render(prompts[2], True, BLACK)
                screen.blit(message, [325, 5])

        if vault_menu:
            pygame.draw.rect(screen, LIGHTYELLOW, [125, 75, 1024, 576])
            clue_three = font_three.render("_ 3 _ _", True, BLACK)
            screen.blit(clue_three, [150, 75])

        # screens
        message = font.render(prompts[5], True, BLACK)

        if collision(character, screen_one_area):
            screen.blit(message, [1196, 175])
            ship_screen = 1
        elif collision(character, screen_two_area):
            screen.blit(message, [1196, 375])
            ship_screen = 2
        elif collision(character, screen_three_area):
            screen.blit(message, [1196, 575])
            ship_screen = 3

        if screen_menu:
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

        # Passcode lock
        if collision(character, passcode_area):
            screen.blit(message, [610, 5])

        if passcode_menu:
            draw_lock()
            passcode_text = font_two.render(passcode, True, BLACK)
            screen.blit(passcode_text, [520, 30])

        if passcode_check:
            if passcode == "h35t":
                pygame.draw.rect(screen, WHITE, [370, 30, 460, 100])
                correct = font_two.render("Correct", True, GREEN)
                screen.blit(correct, [475, 30])
                timer += 1
                if timer == 60:
                    timer = 0
                    screen_ = 2
                    a = 0
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
    elif screen_ == 2:
        screen.fill(WHITE)
        a += 1
        message_1 = font_four.render(endgame_credits[0], True, BLACK)
        message_2 = font_four.render(endgame_credits[1], True, BLACK)
        message_3 = font_four.render(endgame_credits[2], True, BLACK)
        message_4 = font_four.render(endgame_credits[3], True, BLACK)
        screen.blit(message_1, [450, -600 + a])
        screen.blit(message_2, [500, -400 + a])
        screen.blit(message_3, [30, -200 + a])
        screen.blit(message_4, [100, -100 + a])
        print(a)
        if a == 1400:
            pygame.quit()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
