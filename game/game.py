import pygame

pygame.init()

speed = 7

flag2 = False

screen_x = 1500
screen_h = 800

x_run, y_run = 0 , 415

screen = pygame.display.set_mode((screen_x, screen_h))

red = pygame.image.load('img/red.png')
red = pygame.transform.scale(red, (1500,800))


fon = pygame.image.load('img/fon.jpg')
fon = pygame.transform.scale(fon, (1500, 800))


pyla2 = pygame.image.load('img/pyla2.png')
pyla2 = pygame.transform.scale(pyla2, (200,100))

tryba = pygame.image.load('img/tryba.png')
tryba = pygame.transform.scale(tryba, (400, 400))

ball = pygame.image.load('img/ball.png')

screen.blit(red, (0, 0))


sound = pygame.mixer.Sound("sound/red_music.mp3")
sound.play()

flag = False
x, y = 0, 400

while True:
    if flag == False:
        screen.blit(red, (0, 0))

    else:

        screen.blit(fon, (0, 0))
        screen.blit(ball, (x_run, y_run))
        screen.blit(tryba, (800,400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
         sound.stop()
         flag2 = True
         # screen.blit(zemlo, (0, 606))
         # screen.blit(zemlo, (500, 606))
         # screen.blit(sky, (0,0))
         x += 3
         screen.blit(pyla2, (x+250, y))
         flag = True
    else:
        flag2 = False
        x = x_run


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]  and x_run<700:
       x_run += speed



    if keys[pygame.K_a]:
        x_run -= speed


    if y_run < 415:
        y_run+=6
    else:
        if keys[pygame.K_w]:
            y_run-=200

    pygame.display.update()




