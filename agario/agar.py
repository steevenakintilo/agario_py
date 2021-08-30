#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## s
## File description:
## s
##

import pygame
from random import randint
import sys
from os import system
import pygame.freetype 

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

def write_id(path,x):  
    f = open(path, "a")
    f.write(str(x))    
    f.close            

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()
def split(word):
    return [char for char in word]

def char_nbr(path):
    file = open(path, "r")
    data = file.read()
    num = len(data)
    return(num)

def count_the_line(path):
    strs = print_file(path)
    line = 0
    for i in range(len(strs)):
        if strs[i] == "\n":
            line = line + 1
    return(line)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280

class Car(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Car, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect()

class Block(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Block, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect()

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 255, 255))
        self.rect = self.surf.get_rect()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

def big_list():
    c = []
    q = 5
    for i in range(100):
        write_id("pos.txt",str(q) + "\n")
        q = q + 5

def display_all(screen,x,y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

def display_allg(screen,x,y,a,b,c,size):
    bsize = randint(1,size)
    pygame.draw.circle(screen, (a, b, c), (x, y), bsize)

def get_listpos(list,nbr):
    for i in range(len(list)):
        if list[i] == nbr:
            return (i)
            break

def menu_loop():
    system("clear")
    #SCREEN_WIDTH = 800
    #SCREEN_HEIGHT = 600

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font.ttf", 44)
    GAME_FONT2 = pygame.freetype.Font("font.ttf", 94)
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.ogg'),999)
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('boom.ogg'))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    white = (0,0,0)
    color = (217,225,229)
    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('1')]:
            name_loop(1)
        if pressed_keys[ord('2')]:
            name_loop(2)
        screen.fill(color)
        
        GAME_FONT2.render_to(screen, (800, 30), "AGARIO", (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 230), "PRESS 1 TO PLAY 500 POINTS MODE", (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 430), "PRESS 2 TO PLAY BATTLE ROYAL MODE", (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 330), "PRESS B TO PLAY VS", (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 430), "PRESS C TO SEE IA VS IA", (255, 255, 255))
        
        pygame.display.flip()
        clock.tick(30)

def end_loop(text):
    system("clear")
    #SCREEN_WIDTH = 800
    #SCREEN_HEIGHT = 600

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font.ttf", 44)
    GAME_FONT2 = pygame.freetype.Font("font.ttf", 94)
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.ogg'),999)
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('boom.ogg'))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    color = (217,225,229)
    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('m')]:
            menu_loop()
        screen.fill(color)
        
        GAME_FONT2.render_to(screen, (800, 30), text, (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 230), "PRESS M TO GO TO THE MENU", (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 330), "PRESS B TO PLAY VS", (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 430), "PRESS C TO SEE IA VS IA", (255, 255, 255))
        
        pygame.display.flip()
        clock.tick(30)
def name_loop(choice):
    system("clear")
    #SCREEN_WIDTH = 800
    #SCREEN_HEIGHT = 600

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("font.ttf", 44)
    GAME_FONT2 = pygame.freetype.Font("font.ttf", 64)
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.ogg'),999)
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('boom.ogg'))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    color = (217,225,229)
    # Main loop
    name = []
    l = []
    d = 430
    pos = []
    for i in range(100):
        pos.append(d)
        d = d + 100
    letter = 97
    for i in range(26):
        l.append(chr(letter))
        letter = letter + 1
    while running:
        #print(l)
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if choice == 1:
                    if event.key == pygame.K_RETURN:
                        name.append(" ")
                        main_loop(name)
                if choice == 2:
                    if event.key == pygame.K_RETURN:
                        name.append(" ")
                        battle_loop(name)
            elif event.type == QUIT:
                quit()
            for i in range(26):
                if pressed_keys[ord(l[i])]:
                    name.append(l[i])
                    print(name)
        screen.fill(color)
        GAME_FONT2.render_to(screen, (550, 30), "WRITE YOUR NAME THEN PRESS ENTER", (255, 255, 255))
        if len(name) > 0:
            for i in range(len(name)):
                GAME_FONT2.render_to(screen, (pos[i], 430), name[i], (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 230), "PRESS A TO PLAY 500 POINTS MODE", (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 330), "PRESS B TO PLAY VS", (255, 255, 255))
        #GAME_FONT.render_to(screen, (120, 430), "PRESS C TO SEE IA VS IA", (255, 255, 255))
        
        pygame.display.flip()
        clock.tick(30)
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def battle_loop(my_namee):
    my_name = listToString(my_namee)
    my_name = my_name.replace(" ","")
    my_name = my_name.upper()

    brown = (150,75,0)
    green = (0,128,0)
    black =  (255,255,255)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    GAME_FONT = pygame.freetype.Font("font.ttf", 24)
    #car = Car("car.png")
    X = SCREEN_WIDTH/2
    Y = SCREEN_HEIGHT/2
    player = Player()
    player2 = Player2()
    boss = Boss()
    running = True
    i = 0
    j = 0
    px = 950
    py = 500
    move1 = 0
    move2 = 0
    nove1 = 0
    nove2 = 0
    pove1 = 0
    pove2 = 0
    qove1 = 0
    qove2 = 0
    rove1 = 0
    rove2 = 0
    bx = 0
    gx = 0
    d = 0
    y = []
    wlow = 0
    pos_x = []
    pos_y = []
    color1 = []
    color2 = []
    color3 = []
    f = 0
    size = 20
    iasize = 20
    iasize2 = 20
    iasize3 = 20
    iasize4 = 20
    restart = 0
    iarestart = 0
    iarestart2 = 0
    iarestart3 = 0
    iarestart4 = 0
    score = [1,1,1,1,1]
    name = [my_name ,"Ia ","Ia2 ","Ia3 ","Ia4"]
    iax = randint(100,1820)
    iay = randint(100,1180)
    iax2 = randint(100,1820)
    iay2 = randint(100,1180)
    iax3 = randint(100,1820)
    iay3 = randint(100,1180)
    iax4 = randint(100,1820)
    iay4 = randint(100,1180)
    for i in range(200):
        y.append(d)
        pos_x.append(randint(100,1800))
        pos_y.append(randint(100,1180))
        color1.append(randint(0,255))
        color2.append(randint(0,255))
        color3.append(randint(0,255))
        d = d + 100
    color = (217,225,229)
    textsize = 14
    textsize2 = 14
    textsize3 = 14
    textsize4 = 14
    textsize5 = 14
    iaspeed = randint(1,20)
    iaspeed = iaspeed/10
    #iaspeed = 0.3
    while running:
        i = i + 1
        if i % 10 ==0:
            j = j + 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        
        pos = pygame.mouse.get_pos()
        #print(950+move1,500+move2)
        pressed_keys = pygame.key.get_pressed()
        psx = px + move1
        psy = py + move2
        piax = iax + nove1
        piay = iay + nove2
        piax2 = iax2 + pove1
        piay2 = iay2 + pove2
        piax3 = iax3 + qove1
        piay3 = iay3 + qove2
        piax4 = iax4 + rove1
        piay4 = iay4 + rove2
        s = size - 20
        ais = iasize - 20
        slow = size/500
        wlow = 0
        score[0] = size
        score[1] = iasize
        score[2] = iasize2
        score[3] = iasize3
        score[4] = iasize4
        score.sort()
        font = pygame.font.Font("font.ttf", textsize)
        text = font.render(my_name, True, black)
        textRect = text.get_rect()       
        textRect.center = (psx, psy)
        
        iafont = pygame.font.Font("font.ttf", iasize)
        iatext = iafont.render("IA1", True, black)
        iatextRect = iatext.get_rect()       
        iatextRect.center = (piax, piay)
        
        iafont2 = pygame.font.Font("font.ttf", iasize2)
        iatext2 = iafont2.render("IA2", True, black)
        iatext2Rect = iatext2.get_rect()       
        iatext2Rect.center = (piax2, piay2)
       

        iafont3 = pygame.font.Font("font.ttf", iasize3)
        iatext3 = iafont3.render("IA3", True, black)
        iatext3Rect = iatext3.get_rect()       
        iatext3Rect.center = (piax3, piay3)
       

        iafont4 = pygame.font.Font("font.ttf", iasize4)
        iatext4 = iafont4.render("IA4", True, black)
        iatext4Rect = iatext4.get_rect()       
        iatext4Rect.center = (piax4, piay4)
       
        #print(int(iax+nove1),int(iay+nove2),pos_x[0],pos_y[0])
        if pressed_keys[ord("z")] and py+move2-s > 24:
            move2 = move2 - 1 + slow
        if pressed_keys[ord("q")] and px+move1-s > 20:
            move1 = move1 - 1 + slow
        if pressed_keys[ord("s")] and py+move2+s < 978:
            move2 = move2 + 1 - slow
        if pressed_keys[ord("d")] and px+move1+s < 1895:
            move1 = move1 + 1 - slow
        screen.fill((241, 249, 249))
        if iax+nove1 > 1895:
            nove1 = nove1 - 1 - wlow
        if iax+nove1 < 20:
            nove1 = nove1 + 1 + wlow
        if iay+nove2 > 24:
            nove2 = nove2 - 1 - wlow
        if iay+nove2 < 978:
            nove2 = nove2 + 1 + wlow
        
        if iax2+pove1 > 1895:
            pove1 = pove1 - 1
        if iax2+pove1 < 20:
            pove1 = pove1 + 1
        if iay2+pove2 > 24:
            pove2 = pove2 - 1
        if iay2+pove2 < 978:
            pove2 = pove2 + 1
        
        if iax3+qove1 > 1895:
            qove1 = qove1 - 1
        if iax3+qove1 < 20:
            qove1 = qove1 + 1
        if iay3+qove2 > 24:
            qove2 = qove2 - 1
        if iay3+qove2 < 978:
            qove2 = qove2 + 1
        

        if iax4+rove1 > 1895:
            rove1 = rove1 - 1
        if iax4+rove1 < 20:
            rove1 = rove1 + 1
        if iay4+rove2 > 24:
            rove2 = rove2 - 1
        if iay4+qove2 < 978:
            rove2 = rove2 + 1
        
        #pygame.draw.rect(screen, color, pygame.Rect(0, 0, 10000, 10000))
        if size >= 490:
            system("clear")
            end_loop("You win")
        if iasize >= 490:
            system("clear")
            end_loop("IA1 win")
        if iasize2 >= 490:
            system("clear")
            end_loop("IA2 win")
        if iasize3 >= 490:
            system("clear")
            end_loop("IA3 win")
        if iasize4 >= 490:
            system("clear")
            end_loop("IA4 win")
        
        name[get_listpos(score,size)] = my_name + " "
        name[get_listpos(score,iasize)] = "AI  "
        name[get_listpos(score,iasize2)] = "AI2  "
        name[get_listpos(score,iasize3)] = "AI3  "
        name[get_listpos(score,iasize4)] = "AI4  "
        if iasize < 490:
            if iasize <= size or size == 0:
                if int(iax+nove1) < int(pos_x[randint(0,0)]):
                    nove1 = nove1 + 1 + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax+nove1) > int(pos_x[randint(0,0)]):
                    nove1 = nove1 - 1 + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay+nove2) < int(pos_y[randint(0,0)]):
                    nove2 = nove2 + 1 + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) > int(pos_y[randint(0,0)]):
                    nove2 = nove2 - 1 + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) == int(pos_y[randint(0,0)]):
                    pos_x[0] = randint(50,1250)
                if int(iax+nove1) == int(pos_x[randint(0,0)]):
                    pos_y[0] = randint(50,1870)
            if iasize >= size and size != 0:
                if int(iax+nove1) < int(psx):
                    nove1 = nove1 + iaspeed + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax+nove1) > int(psx):
                    nove1 = nove1 - iaspeed + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay+nove2) < int(psy):
                    nove2 = nove2 + iaspeed + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) > int(psy):
                    nove2 = nove2 - iaspeed + wlow
        
        if iasize2 < 490:
            if iasize2 <= iasize or iasize == 0:
                if int(iax2+pove1) < int(pos_x[randint(1,1)]):
                    pove1 = pove1 + 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax2+pove1) > int(pos_x[randint(1,1)]):
                    pove1 = pove1 - 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay2+pove2) < int(pos_y[randint(1,1)]):
                    pove2 = pove2 + 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) > int(pos_y[randint(1,1)]):
                    pove2 = pove2 - 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) == int(pos_y[randint(1,1)]):
                    pos_x[1] = randint(50,1250)
                if int(iax2+pove1) == int(pos_x[randint(1,1)]):
                    pos_y[1] = randint(50,1870)
            if iasize2 >= iasize and iasize != 0:
                if int(iax2+pove1) < int(piax):
                    pove1 = pove1 + iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax2+pove1) > int(piax):
                    pove1 = pove1 - iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay2+pove2) < int(piay):
                    pove2 = pove2 + iaspeed
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) > int(piay):
                    pove2 = pove2 - iaspeed
        
        if iasize3 < 490:
            if iasize3 <= iasize2 or iasize2 == 0:
                if int(iax3+qove2) < int(pos_x[randint(2,2)]):
                    qove1 = qove1 + 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax3+qove1) > int(pos_x[randint(2,2)]):
                    qove1 = qove1 - 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay3+qove2) < int(pos_y[randint(2,2)]):
                    qove2 = qove2 + 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay3+qove2) > int(pos_y[randint(2,2)]):
                    qove2 = qove2 - 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay3+qove2) == int(pos_y[randint(2,2)]):
                    pos_x[2] = randint(50,1250)
                if int(iax3+qove1) == int(pos_x[randint(2,2)]):
                    pos_y[2] = randint(50,1870)
            if iasize3 >= iasize2 and iasize2 != 0:
                if int(iax3+qove1) < int(piax2):
                    qove1 = qove1 + iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax3+qove1) > int(piax2):
                    qove1 = qove1 - iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay3+qove2) < int(piay2):
                    qove2 = qove2 + iaspeed
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay3+qove2) > int(piay2):
                    qove2 = qove2 - iaspeed
        
        if iasize4 < 490:
            if iasize4 <= iasize3 or iasize3 == 0:
                if int(iax4+rove1) < int(pos_x[randint(3,3)]):
                    rove1 = rove1 + 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax4+rove1) > int(pos_x[randint(3,3)]):
                    rove1 = rove1 - 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay4+rove2) < int(pos_y[randint(3,3)]):
                    rove2 = rove2 + 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay4+rove2) > int(pos_y[randint(3,3)]):
                    rove2 = rove2 - 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay4+rove2) == int(pos_y[randint(3,3)]):
                    pos_x[3] = randint(50,1250)
                if int(iax4+rove1) == int(pos_x[randint(3,3)]):
                    pos_y[3] = randint(50,1870)
            if iasize4 >= iasize3 and iasize3 != 0:
                if int(iax4+rove1) < int(piax3):
                    rove1 = rove1 + iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax4+rove1) > int(piax3):
                    rove1 = rove1 - iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay4+rove2) < int(piay3):
                    rove2 = rove2 + iaspeed
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay4+rove2) > int(piay3):
                    rove2 =rove2 - iaspeed
        if psx - size <= piax and psx + size >= piax and psy - size <= piay and psy + size >= piay and size > iasize:
            size = size + iasize
            textsize = textsize + iasize
            iarestart = 0
            if iarestart == 0:
                iax = 9999999
                iay = 9999999
                iarestart = 1
            iasize = 0
            textsize2 = 14
        if psx - size <= piax2 and psx + size >= piax2 and psy - size <= piay2 and psy + size >= piay2 and size > iasize2:
            size = size + iasize2
            textsize = textsize + iasize2
            restart = 0
            if restart == 0:
                iax2 = 8999999
                iay2 = 8999999
                restart = 1
            iasize2 = 0
            textsize3 = 14
        if psx - size <= piax3 and psx + size >= piax3 and psy - size <= piay3 and psy + size >= piay3 and size > iasize3:
            size = size + iasize3
            textsize = textsize + iasize3
            restart = 0
            if restart == 0:
                iax3 = 7999999
                iay3 = 7999999
                restart = 1
            iasize3 = 0
            textsize4 = 14
        if psx - size <= piax4 and psx + size >= piax4 and psy - size <= piay4 and psy + size >= piay4 and size > iasize4:
            size = size + iasize4
            textsize = textsize + iasize4
            restart = 0
            if restart == 0:
                iax4 = 6999999
                iay4 = 6999999
                restart = 1
            iasize4 = 0
            textsize5 = 14
        if psx - size <= piax and psx + size >= piax and psy - size <= piay and psy + size >= piay and size < iasize:
            iasize = iasize + size
            textsize2 = textsize2 + size
            restart = 0
            if restart == 0:
                px = 5999999
                py = 5999999
                restart = 1
            size = 0
            textsize = 14
        if psx - size <= piax2 and psx + size >= piax2 and psy - size <= piay2 and psy + size >= piay2 and size < iasize2:
            iasize2 = iasize2 + size
            textsize3 = textsize3 + size
            restart = 0
            if restart == 0:
                px = 4999999
                py = 4999999
                restart = 1
            size = 0
            textsize = 14
        if psx - size <= piax3 and psx + size >= piax3 and psy - size <= piay3 and psy + size >= piay3 and size < iasize3:
            iasize3 = iasize3 + size
            textsize4 = textsize4 + iasize
            restart = 0
            if restart == 0:
                px = 3999999
                py = 3999999
                restart = 1
            size = 0
            textsize = 14
        if psx - size <= piax4 and psx + size >= piax4 and psy - size <= piay4 and psy + size >= piay4 and size < iasize4:
            iasize4 = iasize4 + size
            textsize5 = textsize5 + size
            restart = 0
            if restart == 0:
                px = 2999999
                py = 2999999
                restart = 1
            size = 0
            textsize = 14
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize2 > iasize:
            iasize2 = iasize2 + iasize
            textsize3 = textsize3 + iasize
            iarestart2 = 0
            if iarestart2 == 0:
                iax = 1999999
                iay = 1999999
                iarestart2 = 1
            iasize = 0
            textsize2 = 14
        if piax - iasize <= piax3 and piax + iasize >= piax3 and piay - iasize <= piay3 and piay + iasize >= piay3 and iasize3 > iasize:
            iasize3 = iasize3 + iasize
            textsize3 = textsize3 + iasize
            iarestart3 = 0
            if iarestart3 == 0:
                iax = -9999999
                iay = -9999999
                iarestart3 = 1
            iasize = 0
            textsize2 = 14
        

        if piax2 - iasize2 <= piax3 and piax2 + iasize2 >= piax3 and piay2 - iasize2 <= piay3 and piay2 + iasize2 >= piay3 and iasize3 > iasize2:
            iasize3 = iasize3 + iasize2
            textsize3 = textsize3 + iasize2
            iarestart2 = 0
            if iarestart2 == 0:
                iax2 = -8999999
                iay2 = -8999999
                iarestart2 = 1
            iasize2 = 0
            textsize3 = 14
        
        if piax2 - iasize2 <= piax3 and piax2 + iasize2 >= piax3 and piay2 - iasize2 <= piay3 and piay2 + iasize2 >= piay3 and iasize3 < iasize2:
            iasize2 = iasize2 + iasize3
            textsize2 = textsize2 + iasize3
            iarestart3 = 0
            if iarestart3 == 0:
                iax3 = -7999999
                iay3 = -7999999
                iarestart3 = 1
            iasize3 = 0
            textsize4 = 14
        

        if piax2 - iasize2 <= piax4 and piax2 + iasize2 >= piax4 and piay2 - iasize2 <= piay4 and piay2 + iasize2 >= piay4 and iasize4 > iasize2:
            iasize4 = iasize4 + iasize2
            textsize4 = textsize4 + iasize2
            iarestart2 = 0
            if iarestart2 == 0:
                iax2 = -6999999
                iay2 = -6999999
                iarestart2 = 1
            iasize2 = 0
            textsize3 = 14
        
        if piax2 - iasize2 <= piax4 and piax2 + iasize2 >= piax4 and piay2 - iasize2 <= piay4 and piay2 + iasize2 >= piay4 and iasize4 < iasize2:
            iasize2 = iasize2 + iasize4
            textsize2 = textsize2 + iasize4
            iarestart4 = 0
            if iarestart4 == 0:
                iax4 = -5999999
                iay4 = -5999999
                iarestart4 = 1
            iasize4 = 0
            textsize5 = 14
        
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize > iasize2:
            iasize = iasize + iasize2
            iarestart2 = 0
            textsize2 = textsize2 + iasize2
            if iarestart2 == 0:
                iax2 = -4999999
                iay2 = -4999999
                iarestart2 = 1
            iasize2 = 0
            textsize3 = 14
        
        if piax - iasize <= piax3 and piax + iasize >= piax3 and piay - iasize <= piay3 and piay + iasize >= piay3 and iasize3 < iasize:
            iasize = iasize + iasize3
            textsize2 = textsize2 + iasize3
            iarestart3 = 0
            if iarestart3 == 0:
                iax3 = -3999999
                iay3 = -3999999
                iarestart3 = 1
            iasize3 = 0
            textsize4 = 14
        
        if piax - iasize <= piax4 and piax + iasize >= piax4 and piay - iasize <= piay4 and piay + iasize >= piay4 and iasize4 < iasize:
            iasize = iasize + iasize4
            textsize2 = textsize2 + iasize4
            iarestart4 = 0
            if iarestart4 == 0:
                iax4 = -2999999
                iay4 = -2999999
                iarestart4 = 1
            iasize4 = 0
            textsize5 = 14
        
        if piax - iasize <= piax4 and piax + iasize >= piax4 and piay - iasize <= piay4 and piay + iasize >= piay4 and iasize4 > iasize:
            iasize4 = iasize4 + iasize
            textsize4 = textsize4 + iasize
            iarestart = 0
            if iarestart == 0:
                iax = -1999999
                iay = -1999999
                iarestart = 1
            iasize = 0
            textsize2 = 14
        
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize < iasize2:
            iasize2 = iasize2 + iasize
            textsize3 = textsize3 + iasize
            iarestart = 0
            if iarestart == 0:
                iax = -8999999
                iay = -4999999
                iarestart = 1
            iasize = 0
            textsize2 = 14
        
        if piax3 - iasize3 <= piax4 and piax3 + iasize3 >= piax4 and piay3 - iasize3 <= piay4 and piay3 + iasize3 >= piay4 and iasize4 > iasize3:
            iasize4 = iasize4 + iasize3
            textsize4 = textsize4 + iasize3
            iarestart3 = 0
            if iarestart3 == 0:
                iax3 = -4999999
                iay3 = -8999999
                iarestart3 = 1
            iasize3 = 0
            textsize4 = 14
        
        if piax3 - iasize3 <= piax4 and piax3 + iasize3 >= piax4 and piay3 - iasize3 <= piay4 and piay3 + iasize3 >= piay4 and iasize4 < iasize3:
            iasize3 = iasize3 + iasize4
            textsize3 = textsize3 + iasize4
            iarestart4 = 0
            if iarestart4 == 0:
                iax4 = -9999999
                iay4 = 9999999
                iarestart4 = 1
            iasize4 = 0
            textsize5 = 14
        
        
        for i in range(200):
            if psx - size <= int(pos_x[i]) and psx + size >= int(pos_x[i]) and psy - size <= int(pos_y[i]) and psy + size >= int(pos_y[i]) and size < 490:
                size = size + 1
                textsize = textsize + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax - iasize <= int(pos_x[i]) and piax + iasize >= int(pos_x[i]) and piay - iasize <= int(pos_y[i]) and piay + iasize >= int(pos_y[i]) and iasize < 490:
                iasize = iasize + 1
                textsize2 = textsize2 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax2 - iasize2 <= int(pos_x[i]) and piax2 + iasize2 >= int(pos_x[i]) and piay2 - iasize2 <= int(pos_y[i]) and piay2 + iasize2 >= int(pos_y[i]) and iasize2 < 490:
                iasize2 = iasize2 + 1
                textsize3 = textsize3 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax3 - iasize3 <= int(pos_x[i]) and piax3 + iasize3 >= int(pos_x[i]) and piay3 - iasize3 <= int(pos_y[i]) and piay3 + iasize3 >= int(pos_y[i]) and iasize3 < 490:
                iasize3 = iasize3 + 1
                textsize4 = textsize4 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax4 - iasize4 <= int(pos_x[i]) and piax4 + iasize4 >= int(pos_x[i]) and piay4 - iasize4 <= int(pos_y[i]) and piay4 + iasize4 >= int(pos_y[i]) and iasize4 < 490:
                iasize4 = iasize4 + 1
                textsize5 = textsize5 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            
            pygame.draw.rect(screen, color, pygame.Rect(0, y[i], 12000, 2))
            pygame.draw.rect(screen, color, pygame.Rect(y[i], 0, 2, 12000))
            pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (pos_x[i], pos_y[i]), 10)
        #print(piax2-10-textsize3/3,piax2-10-textsize3/3,piay2-10-textsize3/5)
        pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (px+ move1, py + move2), size)
        #NAME_FONT.render_to(screen, (int(psx-10-textsize/3), int(psy-10-textsize/5)), str(my_name), (255,255,255))
        screen.blit(text, textRect)
        pygame.draw.circle(screen, (color1[10], color2[20], color3[30]), (iax + nove1, iay + nove2), iasize)
        #NAME_FONT2.render_to(screen, (int(piax-10-textsize2/3), int(piay-10-textsize2/5)), "IA1", (255,255,255))
        screen.blit(iatext, iatextRect)
        pygame.draw.circle(screen, (color1[11], color2[21], color3[31]), (iax2 + pove1, iay2 + pove2), iasize2)
        #NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        screen.blit(iatext2, iatext2Rect)
        pygame.draw.circle(screen, (color1[12], color2[22], color3[32]), (iax3 + qove1, iay3 + qove2), iasize3)
        #NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        screen.blit(iatext3, iatext3Rect)
        pygame.draw.circle(screen, (color1[13], color2[23], color3[33]), (iax4 + rove1, iay4 + rove2), iasize4)
        #NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        screen.blit(iatext4, iatext4Rect)
        
        GAME_FONT.render_to(screen, (20, 25), "Classement: ",(0,0,0))
        GAME_FONT.render_to(screen, (20, 45), " 1 " + name[4] + str(score[4]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 65), " 2 " + name[3] + str(score[3]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 85), "3 " + name[2] + str(score[2]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 105), "4 " + name[1] + str(score[1]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 125), "5 " + name[0] + str(score[0]), (0,0,0))
        pygame.display.flip()

def main_loop(my_namee):
    my_name = listToString(my_namee)
    my_name = my_name.replace(" ","")
    my_name = my_name.upper()

    brown = (150,75,0)
    green = (0,128,0)
    black =  (255,255,255)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    GAME_FONT = pygame.freetype.Font("font.ttf", 24)
    #car = Car("car.png")
    X = SCREEN_WIDTH/2
    Y = SCREEN_HEIGHT/2
    player = Player()
    player2 = Player2()
    boss = Boss()
    running = True
    i = 0
    j = 0
    px = 950
    py = 500
    move1 = 0
    move2 = 0
    nove1 = 0
    nove2 = 0
    pove1 = 0
    pove2 = 0
    qove1 = 0
    qove2 = 0
    rove1 = 0
    rove2 = 0
    bx = 0
    gx = 0
    d = 0
    y = []
    wlow = 0
    pos_x = []
    pos_y = []
    color1 = []
    color2 = []
    color3 = []
    f = 0
    size = 20
    iasize = 20
    iasize2 = 20
    iasize3 = 20
    iasize4 = 20
    restart = 0
    iarestart = 0
    iarestart2 = 0
    iarestart3 = 0
    iarestart4 = 0
    score = [1,1,1,1,1]
    name = [my_name ,"Ia ","Ia2 ","Ia3 ","Ia4"]
    iax = randint(100,1820)
    iay = randint(100,1180)
    iax2 = randint(100,1820)
    iay2 = randint(100,1180)
    iax3 = randint(100,1820)
    iay3 = randint(100,1180)
    iax4 = randint(100,1820)
    iay4 = randint(100,1180)
    for i in range(200):
        y.append(d)
        pos_x.append(randint(100,1800))
        pos_y.append(randint(100,1180))
        color1.append(randint(0,255))
        color2.append(randint(0,255))
        color3.append(randint(0,255))
        d = d + 100
    color = (217,225,229)
    textsize = 14
    textsize2 = 14
    textsize3 = 14
    textsize4 = 14
    textsize5 = 14
    iaspeed = randint(1,20)
    iaspeed = iaspeed/10
    #iaspeed = 0.3
    while running:
        i = i + 1
        if i % 10 ==0:
            j = j + 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        
        pos = pygame.mouse.get_pos()
        #print(950+move1,500+move2)
        pressed_keys = pygame.key.get_pressed()
        psx = px + move1
        psy = py + move2
        piax = iax + nove1
        piay = iay + nove2
        piax2 = iax2 + pove1
        piay2 = iay2 + pove2
        piax3 = iax3 + qove1
        piay3 = iay3 + qove2
        piax4 = iax4 + rove1
        piay4 = iay4 + rove2
        s = size - 20
        ais = iasize - 20
        slow = size/500
        wlow = 0
        score[0] = size
        score[1] = iasize
        score[2] = iasize2
        score[3] = iasize3
        score[4] = iasize4
        score.sort()
        font = pygame.font.Font("font.ttf", textsize)
        text = font.render(my_name, True, black)
        textRect = text.get_rect()       
        textRect.center = (psx, psy)
        
        iafont = pygame.font.Font("font.ttf", iasize)
        iatext = iafont.render("IA1", True, black)
        iatextRect = iatext.get_rect()       
        iatextRect.center = (piax, piay)
        
        iafont2 = pygame.font.Font("font.ttf", iasize2)
        iatext2 = iafont2.render("IA2", True, black)
        iatext2Rect = iatext2.get_rect()       
        iatext2Rect.center = (piax2, piay2)
       

        iafont3 = pygame.font.Font("font.ttf", iasize3)
        iatext3 = iafont3.render("IA3", True, black)
        iatext3Rect = iatext3.get_rect()       
        iatext3Rect.center = (piax3, piay3)
       

        iafont4 = pygame.font.Font("font.ttf", iasize4)
        iatext4 = iafont4.render("IA4", True, black)
        iatext4Rect = iatext4.get_rect()       
        iatext4Rect.center = (piax4, piay4)
       
        #print(int(iax+nove1),int(iay+nove2),pos_x[0],pos_y[0])
        if pressed_keys[ord("z")] and py+move2-s > 24:
            move2 = move2 - 1 + slow
        if pressed_keys[ord("q")] and px+move1-s > 20:
            move1 = move1 - 1 + slow
        if pressed_keys[ord("s")] and py+move2+s < 978:
            move2 = move2 + 1 - slow
        if pressed_keys[ord("d")] and px+move1+s < 1895:
            move1 = move1 + 1 - slow
        screen.fill((241, 249, 249))
        if iax+nove1 > 1895:
            nove1 = nove1 - 1 - wlow
        if iax+nove1 < 20:
            nove1 = nove1 + 1 + wlow
        if iay+nove2 > 24:
            nove2 = nove2 - 1 - wlow
        if iay+nove2 < 978:
            nove2 = nove2 + 1 + wlow
        
        if iax2+pove1 > 1895:
            pove1 = pove1 - 1
        if iax2+pove1 < 20:
            pove1 = pove1 + 1
        if iay2+pove2 > 24:
            pove2 = pove2 - 1
        if iay2+pove2 < 978:
            pove2 = pove2 + 1
        
        if iax3+qove1 > 1895:
            qove1 = qove1 - 1
        if iax3+qove1 < 20:
            qove1 = qove1 + 1
        if iay3+qove2 > 24:
            qove2 = qove2 - 1
        if iay3+qove2 < 978:
            qove2 = qove2 + 1
        

        if iax4+rove1 > 1895:
            rove1 = rove1 - 1
        if iax4+rove1 < 20:
            rove1 = rove1 + 1
        if iay4+rove2 > 24:
            rove2 = rove2 - 1
        if iay4+qove2 < 978:
            rove2 = rove2 + 1
        
        #pygame.draw.rect(screen, color, pygame.Rect(0, 0, 10000, 10000))
        if size >= 490:
            system("clear")
            end_loop("You win")
        if iasize >= 490:
            system("clear")
            end_loop("IA1 win")
        if iasize2 >= 490:
            system("clear")
            end_loop("IA2 win")
        if iasize3 >= 490:
            system("clear")
            end_loop("IA3 win")
        if iasize4 >= 490:
            system("clear")
            end_loop("IA4 win")
        
        name[get_listpos(score,size)] = my_name + " "
        name[get_listpos(score,iasize)] = "AI  "
        name[get_listpos(score,iasize2)] = "AI2  "
        name[get_listpos(score,iasize3)] = "AI3  "
        name[get_listpos(score,iasize4)] = "AI4  "
        if iasize < 490:
            if iasize <= size:
                if int(iax+nove1) < int(pos_x[randint(0,0)]):
                    nove1 = nove1 + 1 + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax+nove1) > int(pos_x[randint(0,0)]):
                    nove1 = nove1 - 1 + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay+nove2) < int(pos_y[randint(0,0)]):
                    nove2 = nove2 + 1 + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) > int(pos_y[randint(0,0)]):
                    nove2 = nove2 - 1 + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) == int(pos_y[randint(0,0)]):
                    pos_x[0] = randint(50,1250)
                if int(iax+nove1) == int(pos_x[randint(0,0)]):
                    pos_y[0] = randint(50,1870)
            if iasize >= size:
                if int(iax+nove1) < int(psx):
                    nove1 = nove1 + iaspeed + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax+nove1) > int(psx):
                    nove1 = nove1 - iaspeed + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay+nove2) < int(psy):
                    nove2 = nove2 + iaspeed + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) > int(psy):
                    nove2 = nove2 - iaspeed + wlow
        
        if iasize2 < 490:
            if iasize2 <= iasize:
                if int(iax2+pove1) < int(pos_x[randint(1,1)]):
                    pove1 = pove1 + 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax2+pove1) > int(pos_x[randint(1,1)]):
                    pove1 = pove1 - 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay2+pove2) < int(pos_y[randint(1,1)]):
                    pove2 = pove2 + 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) > int(pos_y[randint(1,1)]):
                    pove2 = pove2 - 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) == int(pos_y[randint(1,1)]):
                    pos_x[1] = randint(50,1250)
                if int(iax2+pove1) == int(pos_x[randint(1,1)]):
                    pos_y[1] = randint(50,1870)
            if iasize2 >= iasize:
                if int(iax2+pove1) < int(piax):
                    pove1 = pove1 + iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax2+pove1) > int(piax):
                    pove1 = pove1 - iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay2+pove2) < int(piay):
                    pove2 = pove2 + iaspeed
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) > int(piay):
                    pove2 = pove2 - iaspeed
        
        if iasize3 < 490:
            if iasize3 <= iasize2:
                if int(iax3+qove2) < int(pos_x[randint(2,2)]):
                    qove1 = qove1 + 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax3+qove1) > int(pos_x[randint(2,2)]):
                    qove1 = qove1 - 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay3+qove2) < int(pos_y[randint(2,2)]):
                    qove2 = qove2 + 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay3+qove2) > int(pos_y[randint(2,2)]):
                    qove2 = qove2 - 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay3+qove2) == int(pos_y[randint(2,2)]):
                    pos_x[2] = randint(50,1250)
                if int(iax3+qove1) == int(pos_x[randint(2,2)]):
                    pos_y[2] = randint(50,1870)
            if iasize3 >= iasize2:
                if int(iax3+qove1) < int(piax2):
                    qove1 = qove1 + iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax3+qove1) > int(piax2):
                    qove1 = qove1 - iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay3+qove2) < int(piay2):
                    qove2 = qove2 + iaspeed
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay3+qove2) > int(piay2):
                    qove2 = qove2 - iaspeed
        
        if iasize4 < 490:
            if iasize4 <= iasize3:
                if int(iax4+rove1) < int(pos_x[randint(3,3)]):
                    rove1 = rove1 + 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax4+rove1) > int(pos_x[randint(3,3)]):
                    rove1 = rove1 - 1
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay4+rove2) < int(pos_y[randint(3,3)]):
                    rove2 = rove2 + 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay4+rove2) > int(pos_y[randint(3,3)]):
                    rove2 = rove2 - 1
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay4+rove2) == int(pos_y[randint(3,3)]):
                    pos_x[3] = randint(50,1250)
                if int(iax4+rove1) == int(pos_x[randint(3,3)]):
                    pos_y[3] = randint(50,1870)
            if iasize4 >= iasize3:
                if int(iax4+rove1) < int(piax3):
                    rove1 = rove1 + iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax4+rove1) > int(piax3):
                    rove1 = rove1 - iaspeed
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay4+rove2) < int(piay3):
                    rove2 = rove2 + iaspeed
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay4+rove2) > int(piay3):
                    rove2 =rove2 - iaspeed
        if psx - size <= piax and psx + size >= piax and psy - size <= piay and psy + size >= piay and size > iasize:
            size = size + iasize
            textsize = textsize + iasize
            iarestart = 0
            if iarestart == 0:
                iax = randint(100,1800)
                iay = randint(100,1180)
                iarestart = 1
            iasize = 20
            textsize2 = 14
        if psx - size <= piax2 and psx + size >= piax2 and psy - size <= piay2 and psy + size >= piay2 and size > iasize2:
            size = size + iasize2
            textsize = textsize + iasize2
            restart = 0
            if restart == 0:
                iax2 = randint(100,1800)
                iay2 = randint(100,1180)
                restart = 1
            iasize2 = 20
            textsize3 = 14
        if psx - size <= piax3 and psx + size >= piax3 and psy - size <= piay3 and psy + size >= piay3 and size > iasize3:
            size = size + iasize3
            textsize = textsize + iasize3
            restart = 0
            if restart == 0:
                iax3 = randint(100,1800)
                iay3 = randint(100,1180)
                restart = 1
            iasize3 = 20
            textsize4 = 14
        if psx - size <= piax4 and psx + size >= piax4 and psy - size <= piay4 and psy + size >= piay4 and size > iasize4:
            size = size + iasize4
            textsize = textsize + iasize4
            restart = 0
            if restart == 0:
                iax4 = randint(100,1800)
                iay4 = randint(100,1180)
                restart = 1
            iasize4 = 20
            textsize5 = 14
        if psx - size <= piax and psx + size >= piax and psy - size <= piay and psy + size >= piay and size < iasize:
            iasize = iasize + size
            textsize2 = textsize2 + size
            restart = 0
            if restart == 0:
                px = randint(100,1800)
                py = randint(100,1180)
                restart = 1
            size = 20
            textsize = 14
        if psx - size <= piax2 and psx + size >= piax2 and psy - size <= piay2 and psy + size >= piay2 and size < iasize2:
            iasize2 = iasize2 + size
            textsize3 = textsize3 + size
            restart = 0
            if restart == 0:
                px = randint(100,1800)
                py = randint(100,1180)
                restart = 1
            size = 20
            textsize = 14
        if psx - size <= piax3 and psx + size >= piax3 and psy - size <= piay3 and psy + size >= piay3 and size < iasize3:
            iasize3 = iasize3 + size
            textsize4 = textsize4 + iasize
            restart = 0
            if restart == 0:
                px = randint(100,1800)
                py = randint(100,1180)
                restart = 1
            size = 20
            textsize = 14
        if psx - size <= piax4 and psx + size >= piax4 and psy - size <= piay4 and psy + size >= piay4 and size < iasize4:
            iasize4 = iasize4 + size
            textsize5 = textsize5 + size
            restart = 0
            if restart == 0:
                px = randint(100,1800)
                py = randint(100,1180)
                restart = 1
            size = 20
            textsize = 14
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize2 > iasize:
            iasize2 = iasize2 + iasize
            textsize3 = textsize3 + iasize
            iarestart2 = 0
            if iarestart2 == 0:
                iax = randint(100,1800)
                iay = randint(100,1180)
                iarestart2 = 1
            iasize = 20
            textsize2 = 14
        if piax - iasize <= piax3 and piax + iasize >= piax3 and piay - iasize <= piay3 and piay + iasize >= piay3 and iasize3 > iasize:
            iasize3 = iasize3 + iasize
            textsize3 = textsize3 + iasize
            iarestart3 = 0
            if iarestart3 == 0:
                iax = randint(100,1800)
                iay = randint(100,1180)
                iarestart3 = 1
            iasize = 20
            textsize2 = 14
        

        if piax2 - iasize2 <= piax3 and piax2 + iasize2 >= piax3 and piay2 - iasize2 <= piay3 and piay2 + iasize2 >= piay3 and iasize3 > iasize2:
            iasize3 = iasize3 + iasize2
            textsize3 = textsize3 + iasize2
            iarestart2 = 0
            if iarestart2 == 0:
                iax2 = randint(100,1800)
                iay2 = randint(100,1180)
                iarestart2 = 1
            iasize2 = 20
            textsize3 = 14
        
        if piax2 - iasize2 <= piax3 and piax2 + iasize2 >= piax3 and piay2 - iasize2 <= piay3 and piay2 + iasize2 >= piay3 and iasize3 < iasize2:
            iasize2 = iasize2 + iasize3
            textsize2 = textsize2 + iasize3
            iarestart3 = 0
            if iarestart3 == 0:
                iax3 = randint(100,1800)
                iay3 = randint(100,1180)
                iarestart3 = 1
            iasize3 = 20
            textsize4 = 14
        

        if piax2 - iasize2 <= piax4 and piax2 + iasize2 >= piax4 and piay2 - iasize2 <= piay4 and piay2 + iasize2 >= piay4 and iasize4 > iasize2:
            iasize4 = iasize4 + iasize2
            textsize4 = textsize4 + iasize2
            iarestart2 = 0
            if iarestart2 == 0:
                iax2 = randint(100,1800)
                iay2 = randint(100,1180)
                iarestart2 = 1
            iasize2 = 20
            textsize3 = 14
        
        if piax2 - iasize2 <= piax4 and piax2 + iasize2 >= piax4 and piay2 - iasize2 <= piay4 and piay2 + iasize2 >= piay4 and iasize4 < iasize2:
            iasize2 = iasize2 + iasize4
            textsize2 = textsize2 + iasize4
            iarestart4 = 0
            if iarestart4 == 0:
                iax4 = randint(100,1800)
                iay4 = randint(100,1180)
                iarestart4 = 1
            iasize4 = 20
            textsize5 = 14
        
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize > iasize2:
            iasize = iasize + iasize2
            iarestart2 = 0
            textsize2 = textsize2 + iasize2
            if iarestart2 == 0:
                iax2 = randint(100,1800)
                iay2 = randint(100,1180)
                iarestart2 = 1
            iasize2 = 20
            textsize3 = 14
        
        if piax - iasize <= piax3 and piax + iasize >= piax3 and piay - iasize <= piay3 and piay + iasize >= piay3 and iasize3 < iasize:
            iasize = iasize + iasize3
            textsize2 = textsize2 + iasize3
            iarestart3 = 0
            if iarestart3 == 0:
                iax3 = randint(100,1800)
                iay3 = randint(100,1180)
                iarestart3 = 1
            iasize3 = 20
            textsize4 = 14
        
        if piax - iasize <= piax4 and piax + iasize >= piax4 and piay - iasize <= piay4 and piay + iasize >= piay4 and iasize4 < iasize:
            iasize = iasize + iasize4
            textsize2 = textsize2 + iasize4
            iarestart4 = 0
            if iarestart4 == 0:
                iax4 = randint(100,1800)
                iay4 = randint(100,1180)
                iarestart4 = 1
            iasize4 = 20
            textsize5 = 14
        
        if piax - iasize <= piax4 and piax + iasize >= piax4 and piay - iasize <= piay4 and piay + iasize >= piay4 and iasize4 > iasize:
            iasize4 = iasize4 + iasize
            textsize4 = textsize4 + iasize
            iarestart = 0
            if iarestart == 0:
                iax = randint(100,1800)
                iay = randint(100,1180)
                iarestart = 1
            iasize = 20
            textsize2 = 14
        
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize < iasize2:
            iasize2 = iasize2 + iasize
            textsize3 = textsize3 + iasize
            iarestart = 0
            if iarestart == 0:
                iax = randint(100,1800)
                iay = randint(100,1180)
                iarestart = 1
            iasize = 20
            textsize2 = 14
        
        if piax3 - iasize3 <= piax4 and piax3 + iasize3 >= piax4 and piay3 - iasize3 <= piay4 and piay3 + iasize3 >= piay4 and iasize4 > iasize3:
            iasize4 = iasize4 + iasize3
            textsize4 = textsize4 + iasize3
            iarestart3 = 0
            if iarestart3 == 0:
                iax3 = randint(100,1800)
                iay3 = randint(100,1180)
                iarestart3 = 1
            iasize3 = 20
            textsize4 = 14
        
        if piax3 - iasize3 <= piax4 and piax3 + iasize3 >= piax4 and piay3 - iasize3 <= piay4 and piay3 + iasize3 >= piay4 and iasize4 < iasize3:
            iasize3 = iasize3 + iasize4
            textsize3 = textsize3 + iasize4
            iarestart4 = 0
            if iarestart4 == 0:
                iax4 = randint(100,1800)
                iay4 = randint(100,1180)
                iarestart4 = 1
            iasize4 = 20
            textsize5 = 14
        
        
        for i in range(200):
            if psx - size <= int(pos_x[i]) and psx + size >= int(pos_x[i]) and psy - size <= int(pos_y[i]) and psy + size >= int(pos_y[i]) and size < 490:
                size = size + 1
                textsize = textsize + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax - iasize <= int(pos_x[i]) and piax + iasize >= int(pos_x[i]) and piay - iasize <= int(pos_y[i]) and piay + iasize >= int(pos_y[i]) and iasize < 490:
                iasize = iasize + 1
                textsize2 = textsize2 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax2 - iasize2 <= int(pos_x[i]) and piax2 + iasize2 >= int(pos_x[i]) and piay2 - iasize2 <= int(pos_y[i]) and piay2 + iasize2 >= int(pos_y[i]) and iasize2 < 490:
                iasize2 = iasize2 + 1
                textsize3 = textsize3 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax3 - iasize3 <= int(pos_x[i]) and piax3 + iasize3 >= int(pos_x[i]) and piay3 - iasize3 <= int(pos_y[i]) and piay3 + iasize3 >= int(pos_y[i]) and iasize3 < 490:
                iasize3 = iasize3 + 1
                textsize4 = textsize4 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            if piax4 - iasize4 <= int(pos_x[i]) and piax4 + iasize4 >= int(pos_x[i]) and piay4 - iasize4 <= int(pos_y[i]) and piay4 + iasize4 >= int(pos_y[i]) and iasize4 < 490:
                iasize4 = iasize4 + 1
                textsize5 = textsize5 + 1
                pos_x[i] = randint(100,1800)
                pos_y[i] = randint(100,1180)
            
            pygame.draw.rect(screen, color, pygame.Rect(0, y[i], 12000, 2))
            pygame.draw.rect(screen, color, pygame.Rect(y[i], 0, 2, 12000))
            pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (pos_x[i], pos_y[i]), 10)
        #print(piax2-10-textsize3/3,piax2-10-textsize3/3,piay2-10-textsize3/5)
        pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (px+ move1, py + move2), size)
        #NAME_FONT.render_to(screen, (int(psx-10-textsize/3), int(psy-10-textsize/5)), str(my_name), (255,255,255))
        screen.blit(text, textRect)
        pygame.draw.circle(screen, (color1[10], color2[20], color3[30]), (iax + nove1, iay + nove2), iasize)
        #NAME_FONT2.render_to(screen, (int(piax-10-textsize2/3), int(piay-10-textsize2/5)), "IA1", (255,255,255))
        screen.blit(iatext, iatextRect)
        pygame.draw.circle(screen, (color1[11], color2[21], color3[31]), (iax2 + pove1, iay2 + pove2), iasize2)
        #NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        screen.blit(iatext2, iatext2Rect)
        pygame.draw.circle(screen, (color1[12], color2[22], color3[32]), (iax3 + qove1, iay3 + qove2), iasize3)
        #NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        screen.blit(iatext3, iatext3Rect)
        pygame.draw.circle(screen, (color1[13], color2[23], color3[33]), (iax4 + rove1, iay4 + rove2), iasize4)
        #NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        screen.blit(iatext4, iatext4Rect)
        
        GAME_FONT.render_to(screen, (20, 25), "Classement: ",(0,0,0))
        GAME_FONT.render_to(screen, (20, 45), " 1 " + name[4] + str(score[4]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 65), " 2 " + name[3] + str(score[3]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 85), "3 " + name[2] + str(score[2]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 105), "4 " + name[1] + str(score[1]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 125), "5 " + name[0] + str(score[0]), (0,0,0))
        pygame.display.flip()
        
system("clear")
menu_loop()
#main_loop()
