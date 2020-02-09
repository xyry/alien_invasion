#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/9 16:24
# @Author  : YPL
# @FileName: bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''对飞船发射的子弹进行管理'''
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                              ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #存储用小数表示子弹位置
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor