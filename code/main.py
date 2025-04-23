import pygame
import math
import random
import os
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_target(position,BALLCOLOR):
    pygame.draw.circle(screen,
                       color=BALLCOLOR,
                       center=(position, 285),
                       radius=30)

def collide(mass1, mass2, velocity1, velocity2):
    v1new = (((mass1 - mass2) * velocity1) + 2 * (mass2 * velocity2)) / (mass1+mass2)
    v2new = (((mass2 - mass1) * velocity2) + 2 * (mass1 * velocity1)) / (mass1 + mass2)
    return v1new, v2new

def display_text(text,x,y):
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(text, True, (100, 255, 255))
    screen.blit(text_surface, (x,y))

def main():
    running = True
    clock = pygame.time.Clock()

    ball1position, ball2position = 100, 500

    ball1velocity, ball2velocity = 3, -2
    ball1mass, ball2mass = 1,2


    while running:
        screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_target(ball1position,(200,100,100))
        draw_target(ball2position,(50,100,200))

        ball1position += ball1velocity
        ball2position += ball2velocity
        #print(ball1velocity, ball2velocity)
        #print(ball1position, ball2position)
        display_text(str(ball1velocity), 50, 100)
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