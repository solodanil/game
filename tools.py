import os
import sys
import random

import pygame
import pygame.examples.eventlist

FPS = 30
size = WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    pygame.init()
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


screen_rect = (0, 0, WIDTH, HEIGHT)
GRAVITY = 5


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def win(p1, p2):  # нужно обязательно сделать
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image('start_bg.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # создаём частицы по щелчку мыши
                    create_particles(pygame.mouse.get_pos())

                all_sprites.update()
                screen.fill((0, 0, 0))
                all_sprites.draw(screen)
                pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    pygame.examples.eventlist.main()
