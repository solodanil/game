import os
import sys
import random

import pygame
from tools import load_image

pygame.init()
size = width, height = 900, 600
screen = pygame.display.set_mode(size)

p1, p2 = 0, 0


def show_points(sc):
    font = pygame.font.Font(None, 60)
    points1 = font.render(str(p1), True, (255, 255, 255))
    p1_x = 273 if len(str(p1)) <= 1 else 265
    p1_y = 32
    sc.blit(points1, (p1_x, p1_y))

    points2 = font.render(str(p2), True, (255, 255, 255))
    p2_x = 585 if len(str(p2)) <= 1 else 577
    print(len(str(p2)), p2_x)
    p2_y = 534
    sc.blit(points2, (p2_x, p2_y))


class Pow(pygame.sprite.Sprite):
    l_image = load_image('Pow1.png')
    r_image = load_image('Pow2.png')
    l_x, l_y = 0, 0
    x_pressed, y_pressed = width // 2 - 100, height // 2 - 100
    r_x, r_y = width - 200, height - 200

    def __init__(self, group, left):
        super().__init__(group)
        self.left = left
        self.pressed = False
        self.timer = 0
        if left:
            self.image = Pow.l_image
            self.rect = self.image.get_rect()
        else:
            self.image = Pow.r_image
            self.rect = self.image.get_rect()
            self.rect.x = Pow.r_x
            self.rect.y = Pow.r_y

    def press(self):
        self.pressed = True
        self.timer = 0
        self.rect.x = Pow.x_pressed
        self.rect.y = Pow.y_pressed

    def unpress(self):
        self.pressed = False
        self.timer = 0
        if self.left:
            self.rect.x = Pow.l_x
            self.rect.y = Pow.l_y
        else:
            self.rect.x = Pow.r_x
            self.rect.y = Pow.r_y

    def update(self):
        if self.pressed:
            self.timer += 1
            if self.timer > 4:
                self.unpress()


class Fish(pygame.sprite.Sprite):
    image = load_image('good_fish.png')
    bomb_image = load_image('bomb_fish.png')

    def __init__(self, group, is_bomb):
        self.timer = 0

        super().__init__(group)
        self.is_bomb = is_bomb
        if is_bomb:
            self.image = Fish.bomb_image
        else:
            self.image = Fish.image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = height

    def show(self):
        self.rect.x = width // 2 - 50
        self.rect.y = height // 2 - 50

    def hide(self):
        self.rect.x = width
        self.rect.y = height

    def update(self):
        pass


class FishGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.timer = 0
        self.bomb = sprites[1]
        self.good = sprites[0]
        self.bomb_flag = False
        self.good_flag = False

    def press(self, left: bool):
        global p1, p2
        if self.good_flag:
            self.good_flag = False
            if left:
                p1 += 1
            else:
                p2 += 1
        elif self.bomb_flag:
            self.bomb_flag = False
            if left:
                p1 -= 2
            else:
                p2 -= 2
        self.good.hide()
        self.bomb.hide()

    def update(self, *args):
        super(FishGroup, self).update()
        print(self.bomb_flag)
        rnd = random.randint(0, 180)
        if self.good_flag or self.bomb_flag:
            self.timer += 1
        if self.timer > 60 and self.bomb_flag:
            self.bomb.hide()
            self.bomb_flag = False
            self.timer = 0
        elif self.timer > 60 and self.good_flag:
            self.good.hide()
            self.good_flag = False
            self.timer = 0
        if rnd == 0 and not self.bomb_flag and not self.good_flag:
            self.bomb.show()
            self.bomb_flag = True
        elif rnd == 1 and not self.bomb_flag and not self.good_flag:
            self.good.show()
            self.good_flag = True


if __name__ == '__main__':

    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    # создадим спрайт
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image("cat_bg.png")
    # и размеры
    sprite.rect = sprite.image.get_rect()
    # добавим спрайт в группу
    all_sprites.add(sprite)

    fishs = FishGroup(Fish(all_sprites, False), Fish(all_sprites, True))

    l_pow = Pow(all_sprites, True)
    r_pow = Pow(all_sprites, False)

    running = True
    fps = 30  # пикселей в секунду
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # rshift — 303,     lshift — 304
                if event.key == 303:
                    r_pow.press()
                    fishs.press(False)
                elif event.key == 304:
                    l_pow.press()
                    fishs.press(True)
        screen.fill((255, 255, 255))
        print(p1, p2)
        fishs.update()
        all_sprites.update()
        all_sprites.draw(screen)
        show_points(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
