import pygame


pygame.init()

WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

start = False
game_started = False
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


global running

def main():
    global running

    running = True
    global start
    clock = pygame.time.Clock()

    ball1position, ball2position = 100, 750

    ball1velocity, ball2velocity = "", ""
    ball1mass, ball2mass = "" , ""

    input_active = None
    input_boxes = {"mass1":str(ball1mass),"mass2":str(ball2mass),"velocity1":str(ball1velocity),"velocity2":str(ball2velocity)}

    while running:

        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True
                elif event.key == pygame.K_RETURN:
                    try:
                        ball1mass = float(input_boxes["mass1"])
                        ball2mass = float(input_boxes["mass2"])
                        ball1velocity = float(input_boxes["velocity1"])
                        ball2velocity = float(input_boxes["velocity2"])
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE and input_active:
                    input_boxes[input_active] = input_boxes[input_active][:-1]
                elif input_active and event.unicode.isdigit() or event.unicode == "-" or event.unicode == ".":
                    input_boxes[input_active] += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 1230 <= x <= 1290 and 50 <= y <= 90:
                    input_active = "mass1"
                elif 1400 <= x <= 1460 and 50 <= y <= 90:
                    input_active = "velocity1"
                elif 1230 <= x <= 1290 and 120 <= y <= 160:
                    input_active = "mass2"
                elif 1400 <= x <= 1460 and 120 <= y <= 160:
                    input_active = "velocity2"


                elif 1250 <= x <= 1400 and 200 <= y <= 240:  # Reset button area
                    ball1position, ball2position, ball1velocity, ball2velocity, ball1mass, ball2mass, start, input_boxes = reset_game()
                else:
                    input_active = None



        if start:
            #Inputs
            display_text("Ball1 Mass (kg)", 1200, 25, (0, 200, 0), 25)
            display_text(input_boxes["mass1"], 1250, 55, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0, 0, 200), (1230, 50, 60, 40), 2)

            display_text("Ball1 Velocity (m/s)", 1350, 25, (200, 0, 0), 25)
            display_text(input_boxes["velocity1"], 1420, 55, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0, 0, 200), (1400, 50, 60, 40), 2)

            display_text("Ball2 Mass (kg)", 1200, 95, (0, 200, 0), 25)
            display_text(input_boxes["mass2"], 1250, 125, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0, 0, 200), (1230, 120, 60, 40), 2)

            display_text("Ball2 Velocity (m/s)", 1350, 95, (200, 0, 0), 25)
            display_text(input_boxes["velocity2"], 1420, 125, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0, 0, 200), (1400, 120, 60, 40), 2)

            display_text("reset game",1250,200,(255,255,255),45)
            draw_target(ball1position,(200,100,100))
            draw_target(ball2position,(50,100,200))

            ball1position += ball1velocity*2.5
            ball2position += ball2velocity*2.5

            display_text("Distance (m)", 2, 830, (255, 255, 255),35)
            for i in range(17):
                display_text(str(i), (i*97)+2, 860, (255, 255, 255),45)

            display_text("ball1 velocity", 100, 25, (255, 255, 255),45)
            display_text(str(round(float(ball1velocity),2))+" m/s", 100, 50,(255,0,0),45)
            display_text("ball1 mass", 100, 125, (255, 255, 255),45)
            display_text(str(round(float(ball1mass),2))+" kg", 100, 150,(0,255,0),45)

            display_text("ball2 velocity", 350, 25, (255, 255, 255),45)
            display_text(str(round(float(ball2velocity),2))+" m/s", 350, 50,(255,0,0),45)
            display_text("ball2 mass", 350, 125, (255, 255, 255),45)
            display_text(str(round(float(ball2mass),2))+" kg", 350, 150,(0,255,0),45)

            display_text("system momentum", 600, 25, (255, 255, 255),45)
            display_text(str(round((ball2velocity*ball2mass)+(ball1velocity*ball1mass),2))+" kg*m/s",600,50,(0,0,255),45)

            display_text("system kinetic energy", 600, 125, (255, 255, 255),45)
            display_text(str(round(.5*ball1mass*ball1velocity**2 + .5*ball2mass*ball2velocity**2, 2))+" J", 600, 150,(0,0,255),45)



            if abs(ball1position - ball2position) <= 120:
                v1, v2 = collide(ball1mass, ball2mass, ball1velocity, ball2velocity)
                ball1velocity = v1
                ball2velocity = v2
                #prfloat(ball1velocity, ball2velocity)

            if ball1position <= 60 or ball1position >= 1540:
                ball1velocity = -ball1velocity

            if ball2position <= 60 or ball2position >= 1540:
                ball2velocity = -ball2velocity
            pygame.display.update()
            clock.tick(60)



        else:

            display_text("Elastic Collision Simulator",1030,370,(255,200,200),60)
            display_text("Made By Alex Keen", 1145, 430, (200,200,255), 45)
            display_text("Enter Quantities in the top right",1050,500,(200,255,200),45)
            display_text("and press space to start",1100,550,(200,255,200),45)
            display_text("(press enter before you hit space! :)",1100,590,(200,255,200),30)


            display_text("Ball1 Mass (kg)",1200,25,(0,200,0),25)
            display_text(str(input_boxes["mass1"]), 1250, 55, (255, 255, 255), 45)
            pygame.draw.rect(screen,(0,0,200),(1230,50,60,40),2)

            display_text("Ball1 Velocity (m/s)", 1350, 25, (200,0,0), 25)
            display_text(str(input_boxes["velocity1"]), 1420, 55, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0,0,200), (1400, 50, 60, 40), 2)

            display_text("Ball2 Mass (kg)", 1200, 95, (0,200,0), 25)
            display_text(str(input_boxes["mass2"]), 1250, 125, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0,0,200), (1230, 120, 60, 40), 2)

            display_text("Ball2 Velocity (m/s)", 1350, 95, (200,0,0), 25)
            display_text(str(input_boxes["velocity2"]), 1420, 125, (255, 255, 255), 45)
            pygame.draw.rect(screen, (0,0,200), (1400, 120, 60, 40), 2)

            draw_target(ball1position, (200, 100, 100))
            draw_target(ball2position, (50, 100, 200))



            display_text("Distance (m)", 2, 830, (255, 255, 255), 35)
            for i in range(17):
                display_text(str(i), (i * 97) + 2, 860, (255, 255, 255), 45)
            if ball1velocity != "":
                display_text("ball1 velocity", 100, 25, (255, 255, 255), 45)
                if input_boxes["velocity1"] == "" or input_boxes["velocity1"] == "-":
                    display_text("0 m/s", 100, 50, (255, 0, 0), 45)
                else:
                    display_text(str(round(float(input_boxes["velocity1"]), 2)) + " m/s", 100, 50, (255, 0, 0), 45)
            if ball1mass != "":
                display_text("ball1 mass", 100, 125, (255, 255, 255), 45)
                if input_boxes["mass1"] == "" or input_boxes["mass1"] == "-":
                    display_text("0 kg", 100, 50, (255, 0, 0), 45)
                else:
                    display_text(str(round(float(input_boxes["mass1"]), 2)) + " kg", 100, 150, (0, 255, 0), 45)
            if ball2velocity != "":
                display_text("ball2 velocity", 350, 25, (255, 255, 255), 45)
                if input_boxes["velocity2"] == "" or input_boxes["velocity2"] == "-":
                    display_text("0 m/s", 100, 50, (255, 0, 0), 45)
                else:
                    display_text(str(round(float(input_boxes["velocity2"]), 2)) + " m/s", 350, 50, (255, 0, 0), 45)
            if ball2mass != "":
                display_text("ball2 mass", 350, 125, (255, 255, 255), 45)
                if input_boxes["mass2"] == '' or input_boxes["mass2"] == "-":
                    display_text("0 kg", 100, 50, (255, 0, 0), 45)
                else:
                    display_text(str(round(float(input_boxes["mass2"]), 2)) + " kg", 350, 150, (0, 255, 0), 45)

            if ball1velocity != "" and ball2velocity != "" and ball1mass != "" and ball2mass != "":
                display_text("system momentum", 600, 25, (255, 255, 255), 45)
                display_text(str(round((ball2velocity * ball2mass) + (ball1velocity * ball1mass), 2)) + " kg*m/s", 600, 50,
                             (0, 0, 255), 45)

                display_text("system kinetic energy", 600, 125, (255, 255, 255), 45)
                display_text(
                    str(round(.5 * ball1mass * ball1velocity ** 2 + .5 * ball2mass * ball2velocity ** 2, 2)) + " J", 600,
                    150, (0, 0, 255), 45)

            pygame.display.update()
            clock.tick(60)

    pygame.quit()

def reset_game():
    global start
    ball1position = 100
    ball2position = 750
    ball1velocity = 0
    ball2velocity = 0
    ball1mass = 0
    ball2mass = 0
    start = False
    input_boxes = {
        "mass1": "",
        "mass2": "",
        "velocity1": "",
        "velocity2": ""
    }
    return ball1position, ball2position, ball1velocity, ball2velocity, ball1mass, ball2mass, start, input_boxes


if __name__ == "__main__":
    main()