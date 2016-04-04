#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

#変数SCREEN_SIZEを定義
SCREEN_SIZE = (640, 480)

#pygame の初期化
pygame.init()
#ウィンドウの作成
#surface クラスのインスタンス作成
screen = pygame.display.set_mode(SCREEN_SIZE)
#ウィンドウのキャプション付け
#str型.encode('utf-8')で、utf-8 でエンコーディング
pygame.display.set_caption(u"透明色の指定".encode('utf-8'))

#画像イメージをロードしてsurfaceのインスタンスを作成
#.convert()で作成したsurface のインスタンスをウィンドウに適したようにコンバート
planeImg = pygame.image.load("plane.png").convert()

# 透明色を指定したイメージを作成
planeImg2 = pygame.image.load("plane.png").convert()
colorkey = planeImg2.get_at((0,0))  # 左上の色を透明色に
planeImg2.set_colorkey(colorkey, RLEACCEL)

while True:
    #screen を黒一色に
    screen.fill((0,0,0))
    screen.blit(planeImg, (100,100))
    screen.blit(planeImg2, (200,100))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
