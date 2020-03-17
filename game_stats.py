#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/10 14:25
# @Author  : YPL
# @FileName: game_stats.py
# @Software: PyCharm

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.game_active=False

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left=self.ai_settings.ship_limit
