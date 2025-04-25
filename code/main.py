import pygame
import math
import random
import os
import sys
import time

pygame.init()

WIDTH, HEIGHT = 850, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_target(position,BALLCOLOR):
    pygame.draw.circle(screen,
                       color=BALLCOLOR,
                       center=(position, 285),
                       radius=30)

def collide(mass1, mass2, velocity1, velocity2):
    v1new = (((mass1 - mass2) * velocity1) + (2 * (mass2 * velocity2))) / (mass1+mass2)
    v2new = (((mass2 - mass1) * velocity2) + (2 * (mass1 * velocity1))) / (mass1 + mass2)
    return v1new, v2new

def display_text(text,x,y,color,font):
    font = pygame.font.SysFont(None, font)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x,y))

def main():
    running = True
    clock = pygame.time.Clock()

    ball1position, ball2position = 100, 750

    ball1velocity, ball2velocity = 3, -2
    ball1mass, ball2mass = 1 , 2


    while running:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_target(ball1position,(200,100,100))
        draw_target(ball2position,(50,100,200))

        ball1position += ball1velocity
        ball2position += ball2velocity

        display_text("Distance (m)", 0, 460, (255, 255, 255),25)
        for i in range(9):
            display_text(str(i), (i*100), 480, (255, 255, 255),23)

        display_text("ball1 velocity", 100, 25, (255, 255, 255),30)
        display_text(str(round(ball1velocity,2))+" m/s", 100, 50,(255,0,0),30)
        display_text("ball1 mass", 100, 125, (255, 255, 255),30)
        display_text(str(round(ball1mass,2))+" kg", 100, 150,(0,255,0),30)

        display_text("ball2 velocity", 350, 25, (255, 255, 255),30)
        display_text(str(round(ball2velocity,2))+" m/s", 350, 50,(255,0,0),30)
        display_text("ball2 mass", 350, 125, (255, 255, 255),30)
        display_text(str(round(ball2mass,2))+" kg", 350, 150,(0,255,0),30)

        display_text("system momentum", 600, 25, (255, 255, 255),30)
        display_text(str(round((ball2velocity*ball2mass)+(ball1velocity*ball1mass),2))+" kg*m/s",600,50,(0,0,255),30)

        display_text("system kinetic energy", 600, 125, (255, 255, 255),30)
        display_text(str(round(.5*ball1mass*ball1velocity**2 + .5*ball2mass*ball2velocity**2, 2))+" J", 600, 150,(0,0,255),30)

        if abs(ball1position - ball2position) <= 60:
            v1, v2 = collide(ball1mass, ball2mass, ball1velocity, ball2velocity)
            ball1velocity = v1
            ball2velocity = v2
            #print(ball1velocity, ball2velocity)

        if ball1position <= 30 or ball1position >= 770:
            ball1velocity = -ball1velocity

        if ball2position <= 30 or ball2position >= 770:
            ball2velocity = -ball2velocity
        pygame.display.update()


        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()