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
def main_loop():
    brown = (150,75,0)
    green = (0,128,0)
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
    restart = 0
    iarestart = 0
    iarestart2 = 0
    score = [1,1,1]
    name = ["Moi ","Ia ","Ia2 "]
    iax = randint(100,1820)
    iay = randint(100,1180)
    iax2 = randint(100,1820)
    iay2 = randint(100,1180)
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
        s = size - 20
        ais = iasize - 20
        slow = size/500
        wlow = 0
        score[0] = size
        score[1] = iasize
        score[2] = iasize2
        score.sort()
        
        NAME_FONT = pygame.freetype.Font("font.ttf", textsize)
        NAME_FONT2 = pygame.freetype.Font("font.ttf", textsize2)
        NAME_FONT3 = pygame.freetype.Font("font.ttf", textsize3)
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
        #pygame.draw.rect(screen, color, pygame.Rect(0, 0, 10000, 10000))
        if size >= 490:
            system("clear")
            print("You win")
            quit()
        if iasize >= 490:
            system("clear")
            print("Ia1 win")
            quit()
        if iasize2 >= 490:
            system("clear")
            print("Ia2 win")
            quit()
        name[get_listpos(score,size)] = "Moi  "
        name[get_listpos(score,iasize)] = "Ai  "
        name[get_listpos(score,iasize2)] = "Ai2  "
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
                    nove1 = nove1 + 0.3 + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax+nove1) > int(psx):
                    nove1 = nove1 - 0.3 + wlow
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay+nove2) < int(psy):
                    nove2 = nove2 + 0.3 + wlow
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay+nove2) > int(psy):
                    nove2 = nove2 - 0.3 + wlow
        
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
                    pove1 = pove1 + 0.3
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iax2+pove1) > int(piax):
                    pove1 = pove1 - 0.3
                    #nove1 = int(pos_x[randint(0,2)]) - iax
                if int(iay2+pove2) < int(piay):
                    pove2 = pove2 + 0.3
                    #nove2 = int(pos_y[randint(0,2)]) - iay
                if int(iay2+pove2) > int(piay):
                    pove2 = pove2 - 0.3
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
        
        if piax - iasize <= piax2 and piax + iasize >= piax2 and piay - iasize <= piay2 and piay + iasize >= piay2 and iasize < iasize2:
            iasize2 = iasize2 + iasize
            iarestart = 0
            if iarestart == 0:
                iax = randint(100,1800)
                iay = randint(100,1180)
                iarestart = 1
            iasize = 20
            textsize2 = 14
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
            pygame.draw.rect(screen, color, pygame.Rect(0, y[i], 12000, 2))
            pygame.draw.rect(screen, color, pygame.Rect(y[i], 0, 2, 12000))
            pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (pos_x[i], pos_y[i]), 10)
        print(psx,piax,piax2)
        pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (px+ move1, py + move2), size)
        NAME_FONT.render_to(screen, (int(psx-10-textsize/3), int(psy-10-textsize/5)), "Moi", (255,255,255))
        pygame.draw.circle(screen, (color1[10], color2[20], color3[30]), (iax + nove1, iay + nove2), iasize)
        NAME_FONT2.render_to(screen, (int(piax-10-textsize2/3), int(piay-10-textsize2/5)), "IA1", (255,255,255))
        pygame.draw.circle(screen, (color1[11], color2[21], color3[31]), (iax2 + pove1, iay2 + pove2), iasize2)
        NAME_FONT3.render_to(screen, (int(piax2-10-textsize3/3), int(piay2-10-textsize3/5)), "IA2", (255,255,255))
        GAME_FONT.render_to(screen, (20, 25), "Classement: ",(0,0,0))
        GAME_FONT.render_to(screen, (20, 45), " 1 " + name[2] + str(score[2]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 65), "2 " + name[1] + str(score[1]), (0,0,0))
        GAME_FONT.render_to(screen, (20, 85), "3 " + name[0] + str(score[0]), (0,0,0))
        pygame.display.flip()
        
system("clear")
main_loop()
