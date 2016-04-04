#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import sys

#変数SCREEN_SIZE を定義
SCREEN_SIZE = (640,480)

#pygame の初期化
pygame.init()
#ウィンドウの作成
#surface のインスタンスscreen 作成
screen = pygame.display.set_mode(SCREEN_SIZE)
#ウィンドウのキャプション付け
pygame.display.set_caption(u"マウスイベント".encode('utf-8'))

#pygame.image.load(画像イメージ)：イメージをロードしてsurface を返す
#convert():ウィンドウ用の画像に
#convert_alpha():アルファ値(透過度を考える)
backImg = pygame.image.load("moriyama.jpg").convert()
pythonImg = pygame.image.load("python.png").convert_alpha()

#シーケンスについて説明
#オブジェクトをシーケンシャルに処理するためのデータ構造がシーケンス
#タプル：リストど同様だが、()で囲む
#list と違い、中身は不変である事を前提にしているため、書き換えるメソッドがない
cur_pos = (0,0)    #絵の位置を指定
#リスト(list):種類を問わずに格納かのうな配列
#例：list = [1,2,3,"a","b","c"]
pythons_pos = []   #コピーした蛇の位置を格納するリスト

while True:
    #森の画像を転送
    screen.blit(backImg, (0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        #マウスクリックで蛇をコピー
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            x -= pythonImg.get_width()/2
            y -= pythonImg.get_height()/2
            pythons_pos.append((x,y))  #蛇の位置を追加
        #マウス移動で蛇を移動
        if event.type == MOUSEMOTION:
            x,y = event.pos
            x -= pythonImg.get_width() /2
            y -= pythonImg.get_height() /2
            #値を書き込むことは可能
            cur_pos = (x,y)

    #蛇を表示
    screen.blit(pythonImg, cur_pos)
    for i, j in pythons_pos:
        screen.blit(pythonImg, (i,j))

    pygame.display.update()
