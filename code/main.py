import pygame
import math
import random
import os
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_target(position,BALLCOLOR):
    pygame.draw.circle(screen,
                       color=BALLCOLOR,
                       center=(position, 450),
                       radius=60)

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

        display_text("Distance (m)", 2, 830, (255, 255, 255),35)
        for i in range(17):
            display_text(str(i), (i*97)+2, 860, (255, 255, 255),45)

        display_text("ball1 velocity", 100, 25, (255, 255, 255),45)
        display_text(str(round(ball1velocity,2))+" m/s", 100, 50,(255,0,0),45)
        display_text("ball1 mass", 100, 125, (255, 255, 255),45)
        display_text(str(round(ball1mass,2))+" kg", 100, 150,(0,255,0),45)

        display_text("ball2 velocity", 350, 25, (255, 255, 255),45)
        display_text(str(round(ball2velocity,2))+" m/s", 350, 50,(255,0,0),45)
        display_text("ball2 mass", 350, 125, (255, 255, 255),45)
        display_text(str(round(ball2mass,2))+" kg", 350, 150,(0,255,0),45)

        display_text("system momentum", 600, 25, (255, 255, 255),45)
        display_text(str(round((ball2velocity*ball2mass)+(ball1velocity*ball1mass),2))+" kg*m/s",600,50,(0,0,255),45)

        display_text("system kinetic energy", 600, 125, (255, 255, 255),45)
        display_text(str(round(.5*ball1mass*ball1velocity**2 + .5*ball2mass*ball2velocity**2, 2))+" J", 600, 150,(0,0,255),45)

        if abs(ball1position - ball2position) <= 120:
            v1, v2 = collide(ball1mass, ball2mass, ball1velocity, ball2velocity)
            ball1velocity = v1
            ball2velocity = v2
            #print(ball1velocity, ball2velocity)

        if ball1position <= 60 or ball1position >= 1540:
            ball1velocity = -ball1velocity

        if ball2position <= 60 or ball2position >= 1540:
            ball2velocity = -ball2velocity
        pygame.display.update()


        clock.tick(100)
    pygame.quit()

if __name__ == "__main__":
    main()