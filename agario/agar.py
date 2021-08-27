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

def main_loop():
    brown = (150,75,0)
    green = (0,128,0)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #car = Car("car.png")
    X = SCREEN_WIDTH/2
    Y = SCREEN_HEIGHT/2
    player = Player()
    player2 = Player2()
    boss = Boss()
    running = True
    i = 0
    j = 0
    move1 = 0
    move2 = 0
    nove1 = 0
    nove2 = 0
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
    iax = randint(100,1820)
    iay = randint(100,1180)
    for i in range(200):
        y.append(d)
        pos_x.append(randint(50,1870))
        pos_y.append(randint(50,1250))
        color1.append(randint(0,255))
        color2.append(randint(0,255))
        color3.append(randint(0,255))
        d = d + 100
    color = (217,225,229)
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
        psx = 950 + move1
        psy = 500 + move2
        piax = iax + nove1
        piay = iay + nove2
        s = size - 20
        ais = iasize - 20
        slow = size/500
        wlow = iasize/500
        print(int(iax+nove1),int(iay+nove2),pos_x[0],pos_y[0])
        if pressed_keys[ord("z")] and 500+move2-s > 24:
            move2 = move2 - 1 + slow
        if pressed_keys[ord("q")] and 950+move1-s > 20:
            move1 = move1 - 1 + slow
        if pressed_keys[ord("s")] and 500+move2+s < 978:
            move2 = move2 + 1 - slow
        if pressed_keys[ord("d")] and 950+move1+s < 1895:
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
        #pygame.draw.rect(screen, color, pygame.Rect(0, 0, 10000, 10000))
        if iasize < 490:
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
        for i in range(200):
            if psx - size <= int(pos_x[i]) and psx + size >= int(pos_x[i]) and psy - size <= int(pos_y[i]) and psy + size >= int(pos_y[i]) and size < 490:
                size = size + 1
                pos_x[i] = randint(50,1870)
                pos_y[i] = randint(50,1250)
            if piax - iasize <= int(pos_x[i]) and piax + iasize >= int(pos_x[i]) and piay - iasize <= int(pos_y[i]) and piay + iasize >= int(pos_y[i]) and iasize < 490:
                iasize = iasize + 1
                pos_x[i] = randint(50,1870)
                pos_y[i] = randint(50,1250)
            pygame.draw.rect(screen, color, pygame.Rect(0, y[i], 12000, 2))
            pygame.draw.rect(screen, color, pygame.Rect(y[i], 0, 2, 12000))
            pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (pos_x[i], pos_y[i]), 10)
        pygame.draw.circle(screen, (color1[i], color2[i], color3[i]), (950 + move1, 500 + move2), size)
        pygame.draw.circle(screen, (color1[10], color2[20], color3[30]), (iax + nove1, iay + nove2), iasize)
        pygame.display.flip()
        
system("clear")
main_loop()
