#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/8 15:46
# @Author  : YPL
# @FileName: alien_invasion.py
# @Software: PyCharm
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship=Ship(ai_settings,screen)
    while True:
        #监听鼠标和键盘事件
        gf.check_events(ship)
        ship.update()
        gf.updata_screen(ai_settings,screen,ship)

run_game()

# pdf 220页