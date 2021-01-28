import pygame, sys
import random


def rightpic():
    if righttime >= 1:
        screen.blit(rightturn, (0, 0))

def rightpic2():
    if righttime >= 12:
        screen.blit(rightturn2, (0, 0))

def rightpic3():
    if righttime >= 25:
        screen.blit(rightturn3, (0, 0))

def rightpic4():
    if righttime >= 37:
        screen.blit(rightturn4, (0, 0))

def rightpic5():
    if righttime >= 50:
        screen.blit(rightturn5, (0, 0))


def leftpic():
    if lefttime >= 1:
        screen.blit(lefturn, (0, 0))

def leftpic2():
    if lefttime >= 12:
        screen.blit(lefturn2, (0, 0))

def leftpic3():
    if lefttime >= 25:
        screen.blit(lefturn3, (0, 0))

def leftpic4():
    if lefttime >= 37:
        screen.blit(lefturn4, (0, 0))

def leftpic5():
    if lefttime >= 50:
        screen.blit(lefturn5, (0, 0))


def pic():
    if current_time >= 1:
        screen.blit(roadsurface, (0, 0))
def pic1():
    if current_time >= 12:
        screen.blit(roadsurface2, (0, 0))
def pic2():
    if current_time >= 25:
        screen.blit(roadsurface3, (0, 0))
def pic3():
    if current_time >= 37:
        screen.blit(roadsurface4, (0, 0))
def pic4():
    if current_time >= 50:
        screen.blit(roadsurface5, (0, 0))

def road_start():
    screen.blit(turn_start, (0, 200))

def show_score(x,y):
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

pygame.init()
screen = pygame.display.set_mode((1550, 800))
clock = pygame.time.Clock()
current_time = 0
time = 0
time2 = 0
turntime2 = 0
time3 = 0
time4 = 0
car_move = 0
righttime = 0
lefttime = 0
harder = 0
speed = 90

turnlist = [1, 2]
turntimelist = [600, 1000, 1300]
timeturn = random.choice(turntimelist)
time_s = 0
textx = 10
texty = 10
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
carheight = 730
force_left = 6
force_right = 6
force_mid = 0
turn_active = False
right_active = False
game_active = True

turn_start = pygame.image.load(r'C:\Users\zinck\Pictures\road.jpg').convert()
roadsurface = pygame.image.load(r'C:\Users\zinck\Pictures\road gif\space road gif_Moment.jpg').convert()
roadsurface2 = pygame.image.load(r'C:\Users\zinck\Pictures\road gif\space road gif_Moment(3).jpg').convert()
roadsurface3 = pygame.image.load(r'C:\Users\zinck\Pictures\road gif\space road gif_Moment(4).jpg').convert()
roadsurface4 = pygame.image.load(r'C:\Users\zinck\Pictures\road gif\space road gif_Moment(5).jpg').convert()
roadsurface5 = pygame.image.load(r'C:\Users\zinck\Pictures\road gif\space road gif_Moment(6).jpg').convert()
roadsurface = pygame.transform.scale(roadsurface, (1550, 800))
roadsurface2 = pygame.transform.scale(roadsurface2, (1550, 800))
roadsurface3 = pygame.transform.scale(roadsurface3, (1550, 800))
roadsurface4 = pygame.transform.scale(roadsurface4, (1550, 800))
roadsurface5 = pygame.transform.scale(roadsurface5, (1550, 800))

rightturn = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\Untitled_Moment.jpg').convert()
rightturn2 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\Untitled_Moment(2).jpg').convert()
rightturn3 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\Untitled_Moment(3).jpg').convert()
rightturn4 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\Untitled_Moment(4).jpg').convert()
rightturn5 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\Untitled_Moment(5).jpg').convert()
rightturn = pygame.transform.scale(rightturn, (1550, 800))
rightturn2 = pygame.transform.scale(rightturn2, (1550, 800))
rightturn3 = pygame.transform.scale(rightturn3, (1550, 800))
rightturn4 = pygame.transform.scale(rightturn4, (1550, 800))
rightturn5 = pygame.transform.scale(rightturn5, (1550, 800))

lefturn = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\left turn swr_Moment.jpg').convert()
lefturn2 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\left turn swr_Moment(2).jpg').convert()
lefturn3 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\left turn swr_Moment(3).jpg').convert()
lefturn4 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\left turn swr_Moment(4).jpg').convert()
lefturn5 = pygame.image.load(r'C:\Users\zinck\Pictures\turn road gif\left turn swr_Moment(5).jpg').convert()
lefturn = pygame.transform.scale(lefturn, (1550, 800))
lefturn2 = pygame.transform.scale(lefturn2, (1550, 800))
lefturn3 = pygame.transform.scale(lefturn3, (1550, 800))
lefturn4 = pygame.transform.scale(lefturn4, (1550, 800))
lefturn5 = pygame.transform.scale(lefturn5, (1550, 800))

car = pygame.image.load(r'C:\Users\zinck\Pictures\space way race.png').convert_alpha()
car = pygame.transform.scale(car, (300, 200))
car_rect = car.get_rect(center = (775, 4200))
carleft = pygame.image.load(r'C:\Users\zinck\Pictures\swr car2.png').convert_alpha()
carleft = pygame.transform.scale(carleft, (270, 165))
carleft_rect = car.get_rect(center = (775, 4200))
carright = pygame.image.load(r'C:\Users\zinck\Pictures\swr car3.png').convert_alpha()
carright = pygame.transform.scale(carright, (270, 165))
carright_rect = car.get_rect(center = (775, 4200))


flap_sound = pygame.mixer.Sound(r'C:\Users\zinck\Music\sound\swr music.wav')
flap_sound.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game_active:
                car_move += force_right
                carright_rect.centery = carheight
                carleft_rect.centery = 4200
                car_rect.centery = 4200
            if event.key == pygame.K_RIGHT and game_active == False:
                game_active = True
                turn_active = True
            if event.key == pygame.K_LEFT and game_active:
                car_move -= force_left
                carright_rect.centery = 4200
                carleft_rect.centery = carheight
                car_rect.centery = 4200
            if event.key == pygame.K_LEFT and game_active == False:
                game_active = True
                turn_active = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_move = force_mid
                carleft_rect.centery = 4200
                carright_rect.centery = 4200
                car_rect.centery = 700
    if car_rect.centerx <= 160:
        game_active = False
        car_rect.centerx = 775
        carleft_rect.centerx = 775
        carright_rect.centerx = 775
        score_value = 0
    if carleft_rect.centerx <= 160:
        game_active = False
        car_rect.centerx = 775
        carleft_rect.centerx = 775
        carright_rect.centerx = 775
        score_value = 0
    if carright_rect.centerx <= 160:
        game_active = False
        car_rect.centerx = 775
        carleft_rect.centerx = 775
        carright_rect.centerx = 775
        score_value = 0



    if car_rect.centerx >= 1400:
        game_active = False
        car_rect.centerx = 775
        carleft_rect.centerx = 775
        carright_rect.centerx = 775
        score_value = 0
    if carleft_rect.centerx >= 1400:
        game_active = False
        car_rect.centerx = 775
        carleft_rect.centerx = 775
        carright_rect.centerx = 775
        score_value = 0
    if carright_rect.centerx >= 1400:
        game_active = False
        car_rect.centerx = 775
        carleft_rect.centerx = 775
        carright_rect.centerx = 775
        score_value = 0

    speed += 0.10


    time4 += 1
    if time4 == 100:
        time4 = 0
        score_value += 1

    time3 += 1
    if timeturn == 600:
        timeturn2 = 1000
    if timeturn == 1000:
        timeturn2 = 1300
    if timeturn == 1300:
        timeturn2 = 1600

    if time3 >= timeturn2:
        time3 = 0
        time_s = 0
    if time3 == 300:
        timeturn = random.choice(turntimelist)
    if time3 == timeturn:
        time_s = random.choice(turnlist)
    if game_active == False:
        force_mid = 0
        force_left = 6
        force_right = 6
        harder = 0
        speed = 90
    harder += 0.001
    current_time += 1
    pic()

    if game_active:
        pic()
        pic1()
        pic2()
        pic3()
        pic4()
        if current_time >= 62:
            current_time = 0
        if time_s == 1:
            right_active = True
            if right_active == True:
                time += 1

                if time == 10:
                    force_left = 6
                    force_right = 4
                    force_mid = 4 + harder
                if time >= 1:
                    righttime += 1
                    rightpic()
                    rightpic2()
                    rightpic3()
                    rightpic4()
                    rightpic5()
                if righttime >= 62:
                    righttime = 0

                if time >= 300:
                    force_left = 6
                    force_right = 6
                    force_mid = 0
                    time = 0
                    turn_active = False
                    time_s = 0
        if time_s == 2:
            turn_active = True
            if turn_active == True:
                time2 += 1

                if time2 == 10:
                    force_left = 4
                    force_right = 6
                    force_mid = -4 - harder
                if time2 >= 1:
                    lefttime += 1
                    leftpic()
                    leftpic2()
                    leftpic3()
                    leftpic4()
                    leftpic5()
                if lefttime >= 62:
                    lefttime = 0

                if time2 >= 300:
                    force_left = 6
                    force_right = 6
                    force_mid = 0
                    time2 = 0
                    turn_active = False
                    time_s = 0
    screen.blit(car,car_rect)
    screen.blit(carright, carright_rect)
    screen.blit(carleft, carleft_rect)
    car_rect.centerx += car_move
    carleft_rect.centerx += car_move
    carright_rect.centerx += car_move
    show_score(textx, texty)
    pygame.display.update()
    clock.tick(speed)