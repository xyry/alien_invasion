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
from pygame.sprite import Group
from alien import Alien
from button import Button
from game_stats import GameStats
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #  创建play 按钮
    play_button = Button(ai_settings,screen,'Play')
    # 创建 一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens=Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)


    while True:
        #监听鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active==True:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)
        # print(stats.game_active)


run_game()

# pdf 220页