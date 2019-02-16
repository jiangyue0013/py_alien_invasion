import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

import game_functions as gf 

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb)
        if stats.game_active:

            ship.upadate()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb)
        gf.update_screen(
            ai_settings,
            screen,
            ship,
            bullets,
            aliens,
            play_button,
            stats,
            sb,
        )

run_game()