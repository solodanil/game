import os
import sys
import random

import pygame
import pygame.examples.eventlist

FPS = 30
size = WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


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
    pygame.init()
    win_screen = pygame.display.set_mode(size)
    fon = load_image('win.png')
    draw_bg = load_image('draw.png')
    clock = pygame.time.Clock()
    p_font = pygame.font.Font(None, 30)
    players_font = pygame.font.Font('Montserrat-Medium.ttf', 40)
    run_game = True
    timer = 0
    p1_i = -1
    p2_i = -1

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()
                return None
        timer += 1
        p1_i += 1
        p2_i += 1
        if timer == 10:
            create_particles((random.randint(0, 850), random.randint(0, 450)))
            timer = 0
        if p1_i <= p1:
            points1 = p_font.render(str(p1_i), True, (40, 50, 75))
        if p2_i <= p2:
            points2 = p_font.render(str(p2_i), True, (40, 50, 75))
        winner = players_font.render('Игрок слева', True, (255, 255, 255))
        looser = players_font.render('Игрок справа', True, (255, 255, 255))
        if p2 > p1:
            winner, looser = looser, winner
            if p2_i == p2:
                points1, points2 = points2, points1

        all_sprites.update()
        win_screen.fill((0, 0, 0))
        win_screen.blit(fon, (0, 0))
        win_screen.blit(points1, (443, 240))
        win_screen.blit(winner, (510, 160))
        win_screen.blit(points2, (443, 448))
        win_screen.blit(looser, (510, 380))
        if p1 == p2:
            win_screen.blit(draw_bg, (0, 0))
        all_sprites.draw(win_screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    win(3, 7)
#    pygame.examples.eventlist.main()
