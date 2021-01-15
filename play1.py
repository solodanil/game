import pygame
import random
import time

magenta = (255, 0, 255)
orchid = (218, 112, 214)
turquoise = (0, 255, 230)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


def run_car():
    fps = pygame.time.Clock()

    size = (900, 800)
    screensize = pygame.display.set_mode(size)
    done = 0
    screensize.fill(white)

    pygame.init()
    font = pygame.font.Font(None, 50)
    nameofgame = font.render("Правила игры:", 1, red)
    caption = font.render("Кто первый дойдет до красной линии, тот выиграл", 1, black)
    caption1 = font.render("1 Игрок управляет стрелочками", 1, red)
    caption3 = font.render("2 Игрок управляет W,A,S,D", 1, black)
    caption2 = font.render("нажмите пробел для старта", 1, red)

    screensize.blit(nameofgame, (200, 200))
    screensize.blit(caption, (10, 300))
    screensize.blit(caption1, (200, 400))
    screensize.blit(caption3, (200, 500))
    screensize.blit(caption2, (200, 600))
    pygame.display.flip()

    while done == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = 2

    global k_x, k_y
    k_x = 310
    k_y = 750
    k_x1 = 560
    k_y1 = 750
    count = 0

    while done == 2:

        screensize.fill(white)
        pygame.draw.rect(screensize, black, [0, 0, 150, 900], 0)
        pygame.draw.rect(screensize, black, [750, 0, 150, 900], 0)
        pygame.draw.rect(screensize, black, [0, 600, 300, 300], 0)
        pygame.draw.rect(screensize, black, [600, 600, 300, 300], 0)
        pygame.draw.rect(screensize, black, [350, 500, 200, 400], 0)
        pygame.draw.rect(screensize, black, [200, 450, 250, 100], 0)
        pygame.draw.rect(screensize, black, [450, 450, 250, 100], 0)
        pygame.draw.rect(screensize, black, [150, 0, 250, 400], 0)
        pygame.draw.rect(screensize, black, [500, 0, 300, 400], 0)

        pygame.init()
        pygame.draw.rect(screensize, red, [400, 60, 100, 8], 0)

        for event in pygame.event.get():
            count = count + 1
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                randy = random.randint(0, 800)
                if count % 2 == 0:
                    randx = random.randint(0, 900)
                    pygame.draw.circle(screensize, green, [randx, randy], 100, 0)

                if event.key == pygame.K_LEFT:
                    if k_y1 >= 580:
                        if k_y1 >= 550:
                            if k_x1 == 300 or k_x1 == 550:
                                k_x1 -= 0
                            else:
                                k_x1 -= 10
                        else:
                            k_x1 -= 10

                    elif 400 <= k_y1 <= 570:
                        if 430 <= k_y1 <= 540:
                            if k_x1 == 150 or k_x1 == 700:
                                k_x1 -= 0
                            else:
                                k_x1 -= 10

                        elif k_x1 == 150:
                            k_x1 -= 0
                        else:
                            k_x1 -= 10

                    elif k_y1 <= 390:
                        if k_x1 == 400:
                            k_x1 -= 0
                        else:
                            k_x1 -= 10

                    else:
                        k_x1 += 10

                elif event.key == pygame.K_RIGHT:
                    if k_x1 == 320:
                        if k_y1 >= 550:
                            k_x1 += 0
                        else:
                            k_x1 += 10
                    elif k_x1 == 570:
                        if k_y1 >= 580:
                            k_x1 += 0
                        else:
                            k_x1 += 10

                    elif 400 <= k_y1 <= 570:
                        if 430 <= k_y1 <= 540:
                            if k_x1 == 170 or k_x1 == 720:
                                k_x1 += 0
                            else:
                                k_x1 += 10

                        elif k_x1 == 720:
                            k_x1 += 0
                        else:
                            k_x1 += 10

                    elif k_y1 <= 390:
                        if k_x1 == 470:
                            k_x1 += 0
                        else:
                            k_x1 += 10

                    else:
                        k_x1 += 10

                elif event.key == pygame.K_UP:
                    if k_y1 == 550:
                        if 550 <= k_x1 <= 690:
                            k_y1 -= 0
                        elif 180 <= k_x1 <= 320:
                            k_y1 -= 0
                        else:
                            k_y1 -= 10
                    elif k_y1 == 400:
                        if 480 <= k_x1 <= 720:
                            k_y1 -= 0
                        elif 150 <= k_x1 <= 390:
                            k_y1 -= 0
                        else:
                            k_y1 -= 10
                    else:
                        k_y1 -= 10

                elif event.key == pygame.K_DOWN:
                    if k_y1 == 570:
                        if 580 <= k_x1 <= 720:
                            k_y1 += 0
                        elif 150 <= k_x1 <= 290:
                            k_y1 += 0
                        else:
                            k_y1 += 10
                    elif k_y1 == 420:
                        if 180 <= k_x1 <= 690:
                            k_y1 += 0
                        else:
                            k_y1 += 10
                    else:
                        k_y1 += 10

                if event.key == pygame.K_a:
                    if k_y >= 580:
                        if k_y >= 550:
                            if k_x == 300 or k_x == 550:
                                k_x -= 0
                            else:
                                k_x -= 10
                        else:
                            k_x -= 10

                    elif 400 <= k_y <= 570:
                        if 430 <= k_y <= 540:
                            if k_x == 150 or k_x == 700:
                                k_x -= 0
                            else:
                                k_x -= 10

                        elif k_x == 150:
                            k_x -= 0
                        else:
                            k_x -= 10

                    elif k_y <= 390:
                        if k_x == 400:
                            k_x -= 0
                        else:
                            k_x -= 10

                    else:
                        k_x += 10

                elif event.key == pygame.K_d:
                    if k_x == 320:
                        if k_y >= 550:
                            k_x += 0
                        else:
                            k_x += 10
                    elif k_x == 570:
                        if k_y >= 580:
                            k_x += 0
                        else:
                            k_x += 10

                    elif 400 <= k_y <= 570:
                        if 430 <= k_y <= 540:
                            if k_x == 170 or k_x == 720:
                                k_x += 0
                            else:
                                k_x += 10

                        elif k_x == 720:
                            k_x += 0
                        else:
                            k_x += 10

                    elif k_y <= 390:
                        if k_x == 470:
                            k_x += 0
                        else:
                            k_x += 10

                    else:
                        k_x += 10

                elif event.key == pygame.K_w:
                    if k_y == 550:
                        if 550 <= k_x <= 690:
                            k_y -= 0
                        elif 180 <= k_x <= 320:
                            k_y -= 0
                        else:
                            k_y -= 10
                    elif k_y == 400:
                        if 480 <= k_x <= 720:
                            k_y -= 0
                        elif 150 <= k_x <= 390:
                            k_y -= 0
                        else:
                            k_y -= 10
                    else:
                        k_y -= 10

                elif event.key == pygame.K_s:
                    if k_y == 570:
                        if 580 <= k_x <= 720:
                            k_y += 0
                        elif 150 <= k_x <= 290:
                            k_y += 0
                        else:
                            k_y += 10
                    elif k_y == 420:
                        if 180 <= k_x <= 690:
                            k_y += 0
                        else:
                            k_y += 10
                    else:
                        k_y += 10

                if k_y1 == 60:
                    screensize.fill(black)
                    font = pygame.font.Font(None, 150)
                    winner1 = font.render("1 выиграл", 1, turquoise)
                    screensize.blit(winner1, (170, 200))
                    pygame.display.flip()
                    time.sleep(5)
                    done = 0
                elif k_y == 60:
                    screensize.fill(black)
                    font = pygame.font.Font(None, 150)
                    winner2 = font.render("2 выиграл", 1, turquoise)
                    screensize.blit(winner2, (170, 200))
                    pygame.display.flip()
                    time.sleep(5)
                    done = 0

        pygame.draw.rect(screensize, magenta, [k_x, k_y, 30, 30], 0)
        pygame.draw.rect(screensize, turquoise, [k_x1, k_y1, 30, 30], 0)
        pygame.display.flip()
        fps.tick(6)

    pygame.quit()
