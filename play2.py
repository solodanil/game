import pygame
import random


def run_game():
    pygame.init()
    width = 850
    height = 450
    my_win = pygame.display.set_mode( (width, height) )
    radius = 15
    bumper_w = 25
    bumper_h = 110
    xspeed1 = 0
    xspeed2 = 0
    yspeed1 = 0
    yspeed2 = 0
    frame_count = 0
    p1_score = 0
    p2_score = 0
    myFont = pygame.font.Font( None, 48 )
    x = width / 2
    y = height / 2
    b1_x = 0
    b1_y = 190
    b2_x = 825
    b2_y = 190
    num = random.randint(1, 4)
    if num == 1:
        x_v = 4
        y_v = -4
    if num == 2:
        x_v = 4
        y_v = 4
    if num == 3:
        x_v = -4
        y_v = 4
    if num == 4:
        x_v = -4
        y_v = -4

    flag = True
    while (flag):
        pygame.time.delay( 15 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name( event.key ) == "w":
                    yspeed1 = -12
                if pygame.key.name( event.key ) == "d":
                    xspeed1 = 12
                if pygame.key.name( event.key ) == "s":
                    yspeed1 = 12
                if pygame.key.name( event.key ) == "a":
                    xspeed1 = -12
                if pygame.key.name( event.key ) == "up":
                    yspeed2 = -12
                if pygame.key.name( event.key ) == "right":
                    xspeed2 = 12
                if pygame.key.name( event.key ) == "down":
                    yspeed2 = 12
                if pygame.key.name( event.key ) == "left":
                    xspeed2 = -12
            elif event.type == pygame.KEYUP:
                if pygame.key.name( event.key ) == "w":
                    yspeed1 = 0
                if pygame.key.name( event.key ) == "d":
                    xspeed1 = 0
                if pygame.key.name( event.key ) == "s":
                    yspeed1 = 0
                if pygame.key.name( event.key ) == "a":
                    xspeed1 = 0
                if pygame.key.name( event.key ) == "up":
                    yspeed2 = 0
                if pygame.key.name( event.key ) == "right":
                    xspeed2 = 0
                if pygame.key.name( event.key ) == "down":
                    yspeed2 = 0
                if pygame.key.name( event.key ) == "left":
                    xspeed2 = 0

        x += x_v
        y += y_v

        frame_count += 1
        increment = 1

        if frame_count >= 500:
            frame_count = 0
            if x_v > 0:
                x_v += increment
            if x_v < 0:
                x_v += -(increment)
            if y_v > 0:
                y_v += increment
            if y_v < 0:
                y_v += -(increment)
        b1_x += xspeed1
        b1_y += yspeed1
        b2_x += xspeed2
        b2_y += yspeed2
        if b1_x < 0:
            b1_x = 0
        if b1_x > 399:
            b1_x = 399
        if b1_y < 0:
            b1_y = 0
        if b1_y > 370:
            b1_y = 370
        if b2_x < 426:
            b2_x = 426
        if b2_x > 825:
            b2_x = 825
        if b2_y < 0:
            b2_y = 0
        if b2_y > 370:
            b2_y = 370
        if x < -(radius):
            p2_score += 1
            (x, y) = (width / 2, height / 2)
            frame_count = 0
            num = random.randint( 1, 4 )
            if num == 1:
                x_v = 4
                y_v = -4
            if num == 2:
                x_v = 4
                y_v = 4
            if num == 3:
                x_v = -4
                y_v = 4
            if num == 4:
                x_v = -4
                y_v = -4
        if x > (width + radius):
            p1_score += 1
            (x, y) = (width / 2, height / 2)
            frame_count = 0
            num = random.randint( 1, 4 )
            if num == 1:
                x_v = 4
                y_v = -4
            if num == 2:
                x_v = 4
                y_v = 4
            if num == 3:
                x_v = -4
                y_v = 4
            if num == 4:
                x_v = -4
                y_v = -4
        if (y <= radius):
            y_v = -1 * y_v
        if (y >= (height - radius)):
            y_v = -1 * y_v
        if (x_v < 0) and (xspeed1 >= 0):
            if ((x - b1_x) <= (radius + bumper_w)) and ((x - b1_x) > ((radius + bumper_w) - bumper_w)):
                if ((y - b1_y) > -(radius)) and ((y - b1_y) <= (bumper_h / 2)):
                    x_v = -1 * x_v
                    y_v = -1 * abs( y_v )
                if ((y - b1_y) > (bumper_h / 2)) and ((y - b1_y) < (bumper_h + radius)):
                    x_v = -1 * x_v
                    y_v = abs( y_v )

        if (x_v > 0) and (xspeed2 <= 0):
            if ((b2_x - x) <= radius) and ((b2_x - x) > (radius - bumper_w)):
                if ((y - b2_y) > -(radius)) and ((y - b2_y) <= (bumper_h / 2)):
                    x_v = -1 * x_v
                    y_v = -1 * abs( y_v )
                if ((y - b2_y) > (bumper_h / 2)) and ((y - b2_y) < (bumper_h + radius)):
                    x_v = -1 * x_v
                    y_v = abs( y_v )

        my_win.fill( pygame.color.Color( "lightblue" ) )

        score_label_1 = myFont.render( "P1: " + str( p1_score ), True, pygame.color.Color( "darkgreen" ) )
        my_win.blit( score_label_1, (10, 5) )

        score_label_2 = myFont.render( "P2: " + str( p2_score ), True, pygame.color.Color( "darkgreen" ) )
        my_win.blit( score_label_2, (760, 5) )

        pygame.draw.circle( my_win, pygame.color.Color( "black" ), (int( width / 2 ), int( height / 2 )), 125 )

        pygame.draw.circle( my_win, pygame.color.Color( "lightblue" ), (int( width / 2 ), int( height / 2 )), 123 )

        pygame.draw.rect( my_win, pygame.color.Color( "black" ), (424, 0, 2, height) )

        pygame.draw.circle( my_win, pygame.color.Color( "red" ), (int( x ), int( y )), int( radius ) )

        pygame.draw.rect( my_win, pygame.color.Color( "blue" ), (b1_x, b1_y, bumper_w, bumper_h) )

        pygame.draw.rect( my_win, pygame.color.Color( "orange" ), (b2_x, b2_y, bumper_w, bumper_h) )

        pygame.display.update()

    pygame.quit()

run_game()
