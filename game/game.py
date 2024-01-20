import pygame

pygame.init()

speed = 7

screen_x = 1500
screen_h = 800

x_run, y_run = 0 , 415

screen = pygame.display.set_mode((screen_x, screen_h))

red = pygame.image.load('img/red.png')
red = pygame.transform.scale(red, (1500,800))


zemlo = pygame.image.load('img/zemlo.jpg')

sky = pygame.image.load('img/sky.png')
sky = pygame.transform.scale(sky, (1500,700))

ball = pygame.image.load('img/ball.png')

screen.blit(red, (0, 0))


sound = pygame.mixer.Sound("sound/red_music.mp3")
sound.play()

flag = False

while True:
    if flag == False:
        screen.blit(red, (0, 0))

    else:
        screen.blit(sky, (0, 0))
        screen.blit(zemlo, (0, 606))
        screen.blit(zemlo, (500, 606))
        screen.blit(ball, (x_run, y_run))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
         sound.stop()
         # screen.blit(zemlo, (0, 606))
         # screen.blit(zemlo, (500, 606))
         # screen.blit(sky, (0,0))
         flag = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_run += speed


    if keys[pygame.K_a]:
        x_run -= speed
    if keys[pygame.K_e]:
        quit()
    if y_run < 415:
        y_run+=6
    else:
        if keys[pygame.K_w]:
            y_run-=200

    pygame.display.update()




