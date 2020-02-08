#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/8 15:46
# @Author  : YPL
# @FileName: alien_invasion.py
# @Software: PyCharm
import sys
import pygame

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien Invasion")
    bg_color=(230,230,230)
    while True:
        #监听鼠标和键盘事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #每次循环重新绘制屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()