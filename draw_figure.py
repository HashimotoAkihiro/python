#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import sys

#Python で、UTF-８を使えるように
#u'文字' とコードを書くとUSC2 の文字列を扱うらしい
 
#変数SCREEN_SIZEを定義
SCREEN_SIZE = (640, 480)
#ウィンドウの作成
screen = pygame.display.set_mode(SCREEN_SIZE)
#ウィンドウのキャプション
pygame.display.set_caption(u"図形の描画".encode('utf-8'))
 
#while(1)のように、無限ループ
while True:
    screen.fill((0,0,0))    #黒一色のウィンドウ
 
    #図形を描画
    #黄色の矩形(四角形)を作成
    #引数：(表示するウィンドウ名,図形の色, (左上の座標(x, y), 横，縦))
#   pygame.draw.rect(screen, (255,255,0), Rect(10, 10, 300, 200))
    #線の太さを指定
#   pygame.draw.rect(screen, (255,255,0), Rect(10, 10, 300, 200), 2)
    screen.fill((255,255,0), Rect(10,10,300,200))
    #赤の円
    pygame.draw.circle(screen, (255,0,0), (320,240), 100)
    #紫の楕円
    pygame.draw.ellipse(screen, (255,0,255), (400, 300, 200, 100))
    #白い線
    pygame.draw.line(screen, (255, 255, 255), (0,0), (640, 480))
 
    #Surface(画像)をウィンドウに出力
    pygame.display.update()
 
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
