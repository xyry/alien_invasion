#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/8 16:00
# @Author  : YPL
# @FileName: settings.py
# @Software: PyCharm

# 文件settings.py包含Settings类，这个类只包含方法__init__()，它初始化控制游戏外观和飞
# 船速度的属性。
class Settings():
    def __init__(self):

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color=(230,230,230)
        #ship configuration
        self.ship_speed_factor=1.5
        self.ship_limit=3
        # bullet configuration
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        # alien configuration
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed=100
        # fleet_direction 为1 表示向右移动，为-1表示向左移动
        self.fleet_direction = 1