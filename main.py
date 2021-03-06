import sys

import pygame
from tools import load_image, win
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

pygame.mixer.music.load('FortyThr33 - Bay Breeze FREE DOWNLOAD.mp3')
pygame.mixer.music.set_volume(0.5)


def terminate():
    pygame.quit()
    sys.exit()


def hover(pos, click=True):
    pygame.mixer.music.play(-1)
    x, y = pos[0], pos[1]
    p1, p2 = 0, 0
    if x in range(180, 400) and y in range(60, 250):
        if click:
            return start_bg_kub
        else:
            ping = run_ping()
            cat = start_cat()
            car = run_car()
            p1 = p1 + ping[0] + cat[0] + car[0]
            p2 = p2 + ping[1] + cat[1] + car[1]
            win(p1, p2)

    elif x in range(500, 720) and y in range(60, 250):
        if click:
            return start_bg_ping
        else:
            p = run_ping()
            win(p[0], p[1])
    elif x in range(180, 400) and y in range(300, 500):
        if click:
            return start_bg_pow
        else:
            p = start_cat()
            win(p[0], p[1])
    elif x in range(500, 720) and y in range(300, 500):
        if click:
            return start_bg_car
        else:
            p = run_car()
            win(p[0], p[1])
    return start_bg


def start_screen():
    clock = pygame.time.Clock()

    while True:
        screen.blit(hover(pygame.mouse.get_pos()), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                hover(pygame.mouse.get_pos(), click=False)
        try:
            pygame.display.flip()
            clock.tick(FPS)
        except pygame.error:
            terminate()


if __name__ == '__main__':
    pygame.init()
    start_screen()
