import os
import sys

import pygame
import pygame.examples.eventlist


class Background(pygame.sprite.Sprite):
    def __init__(self, group, bg_filename):
        super(Background, self).__init__()
        self.img = load_image(bg_filename)
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = 0, 0
        print(0)


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.examples.eventlist.main()
