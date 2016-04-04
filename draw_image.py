#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import sys

#Python で、UTF-８を使えるように
#u'文字' とコードを書くとUSC2 の文字列を扱うらしい
#変数SCREEN_SIZEを定義
SCREEN_SIZE = (640, 480)

#pygame の初期化
pygame.init()
#ウィンドウの作成
#surface クラスのインスタンス作成
screen = pygame.display.set_mode(SCREEN_SIZE)
#ウィンドウのキャプション付け
pygame.display.set_caption(u"イメージの描画".encode('utf-8'))

#イメージをロード
#Pygame は，BMP, GIF, JPG, PNG, PCX, TGA, TIF, LBM, PBM, XPMをサポート
#画像イメージファイルのロードには、"pygame.image.load("画像ファイル名")"を使う
#戻り値はイメージが描画されたsurface
backImg = pygame.image.load("moriyama.jpg").convert()        #背景用の画像をロード
#surface.convert():ロードした画像イメージをディスプレイ用に変換し，オリジナルの画像イメージに透過度が指定されていないときに使用
#surface.convert_alpha():convert()と同様、オリジナルの画像イメージに透過度が指定されている時に使用
pythonImg = pygame.image.load("python.png").convert_alpha()  #蛇
#pythonImg = pygame.image.load("python.png").convert()  #蛇

while True:
    #Surface のインスタンスscreen(main となる画像)へ
    #backImg, pythonImg を描画する
    #surface.blit():画像ファイルの描画(ファイル転送というイメージらしい)
    screen.blit(backImg,(0,0))     #背景を描画
    screen.blit(pythonImg,(320,400))#蛇を描画
    #screen に色々設定したら，下の.display.update()を実行しないと
    #ウィンドウに表示されない
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
              sys.exit()
#簡単に
#screen は白紙のようなもの
#そこに，backImg, pythonImgを描いていく(screen.blit("screen のインスタンス",(座標)))
