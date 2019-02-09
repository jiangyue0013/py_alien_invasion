import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien

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

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.upadate()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens, ship)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens,)

run_game()