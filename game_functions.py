#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/8 16:53
# @Author  : YPL
# @FileName: game_functions.py
# @Software: PyCharm

import sys
import pygame

def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)

        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def updata_screen(ai_settings,screen,ship):
    # 每次循环重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
