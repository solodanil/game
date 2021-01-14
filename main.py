import sys

import pygame
from tools import load_image
from cat import start_cat
from play2 import run_ping
from play1 import run_car

FPS = 50
size = WIDTH, HEIGHT = 900, 600

screen = pygame.display.set_mode(size)

start_bg = load_image('start_bg.png')
start_bg_car = load_image('start_bg_car.png')
start_bg_kub = load_image('start_bg_kub.png')
start_bg_ping = load_image('start_bg_ping.png')
start_bg_pow = load_image('start_bg_pow.png')


def terminate():
    pygame.quit()
    sys.exit()


def hover(pos, click=True):
    x, y = pos[0], pos[1]
    # 180, 60
    if x in range(180, 400) and y in range(60, 250):
        if click:
            return start_bg_kub
        else:
            pass
    elif x in range(500, 720) and y in range(60, 250):
        if click:
            return start_bg_ping
        else:
            run_ping()
    elif x in range(180, 400) and y in range(300, 500):
        if click:
            return start_bg_pow
        else:
            start_cat()
    elif x in range(500, 720) and y in range(300, 500):
        if click:
            return start_bg_car
        else:
            run_car()
    return start_bg


def start_screen():

    clock = pygame.time.Clock()

    while True:
        print(pygame.mouse.get_pos())
        screen.blit(hover(pygame.mouse.get_pos()), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                hover(pygame.mouse.get_pos(), click=False)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    start_screen()
