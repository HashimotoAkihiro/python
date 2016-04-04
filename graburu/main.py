#!/usr/bin/env python
#coding: utf-8
import pdb
import pygame
from pygame.locals import *
import sys
#pygameでボタン操作をする場合に使用
import pygbutton

7def main():
    #変数SCREEN_SIZE を定義
    SCREEN_SIZE = (400,800)
    #pygameの初期化
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    #ウィンドウのキャプション付け
    pygame.display.set_caption(u"グランブルーファンタジー".encode('utf-8'))

    #タイトルの位置を指定
    turn_pos = (0,0)
    #フォントの作成,(デフォで、ゴシック、, 文字サイズ)
    sysfont = pygame.font.SysFont(None, 40)
    #テキストのレンダリング
    #(描画したいテキスト、アンチエイリアシングを使うか、文字色、背景の色
    title = sysfont.render("~~Battle 1/3~~",True, (0,0,0), (255,255,255))
    #
    button_attack_x = 400-100
    button_attack_y = title.get_height() + 450 -50
    button_attack = pygbutton.PygButton((button_attack_x,button_attack_y,100,50), 'Attack')

    #キャラの描写
    #convert()を実行することで、ディスプレイと同じイメージにする。
    EnemyImg = pygame.image.load("binya.png").convert()
    EnemyImg1 = pygame.transform.rotozoom(EnemyImg, -40,0.8)
    #元の画像のどれを透明にするか指定する
    #colorkey = EnemyImg.get_at((0,0))
    colorkey = (255,255,255)
    #第2引数はわかりません。
    EnemyImg1.set_colorkey(colorkey, RLEACCEL)
    MasterImg = pygame.image.load("uta_master.png").convert()
    SlaveImg01 = pygame.image.load("uta_master.png").convert()
    SlaveImg02 = pygame.image.load("uta_master.png").convert()
    SlaveImg03 = pygame.image.load("uta_master.png").convert()
    

    while True:
        screen.fill((0,255,255))
        #surfaceへテキストを設置
        x = 200-title.get_width()/2
        screen.blit(title,(x,0))
        #きゃら位置は、とりあえず四角形で表現(座標、サイズ)
        pygame.draw.rect(screen, (255,255,0), (0,title.get_height(),400,450))
        screen.blit(EnemyImg1,(30 ,title.get_height()+30))

        button_attack.draw(screen)
        
        #(surface, 角度、スケール)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if 'click' in button_attack.handleEvent(event):
                print("Button Pushed")
                #battle()
                #
                sys.exit()
        

#main文の呼び出し、らしい
if __name__ =="__main__":
    main()
