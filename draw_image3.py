#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
#下のように書くと，load_image.py の関数load_image を使用する
from load_image import load_image
#下の用にかくと，load_image.load_image()とかく
#import load_image

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(u"イメージロード関数".encode('utf-8'))

planeImg, planeRect = load_image("plane.png", colorkey=-1)
#planeImg, planeRect = load_image.load_image("plane.png", colorkey=-1)

while True:
    screen.fill((0,0,0))
    screen.blit(planeImg, (200,100))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
