#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def load_image(filename, colorkey=None):
    #例外処理用の記述が,try　条件: except 条件:
    #下の記述だと、pygame.error,messageと書くとその例外がある場合にSystemExitを実行
    try:
        #filename をロードしてsurface を作成
        image = pygame.image.load(filename)
    except pygame.error,message:
        #エラーメッセージを送信するらしい
        raise SystemExit, message
    #ウィンドウ用にコンバート
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))#左上の色を透明にするらしい
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
