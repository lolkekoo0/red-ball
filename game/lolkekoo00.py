import pygame


pygame.init()

screen_x = 1500
screen_h = 800

screen = pygame.display.set_mode((screen_x,screen_h))

font = pygame.font.SysFont("Agency FB",80)
font2 = pygame.font.SysFont("Agency FB",50)
font3 = pygame.font.SysFont("Agency FB",30)

speed = 6
x_run, y_run = 500 , 200

freddy = pygame.image.load('img/freddy.png')
freddy = pygame.transform.scale(freddy, (400, 500))

sound = pygame.mixer.Sound("sound/deep.mp3")
sound2 = pygame.mixer.Sound("sound/fnaf.mp3")

tv_new = pygame.image.load('img/tv_new.png')
tv_new = pygame.transform.scale(tv_new, (1500,800))
tv_new2 = pygame.image.load("img/fon .jpg")
tv_new2 = pygame.transform.scale(tv_new2, (1500,800))
screen.blit(tv_new, (0,0))
x1=100
x2=1300

sound2.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(tv_new2, (0,0))
            sound2.stop()
            x1-=500
            x2+=900
            x_run+= 1000



    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_run+=speed
        sound.play()
    if keys[pygame.K_w]:
        y_run-=speed
        sound.play()
    if keys[pygame.K_a]:
        x_run -= speed
        sound.play()
    if keys[pygame.K_s]:
        y_run += speed
        sound.play()



    screen.blit(freddy, (x_run, y_run))


    text = font.render("Five",True,(255, 255, 255))
    screen.blit(text,(x1,45))
    text2 = font.render("Nights", True, (255, 255, 255))
    screen.blit(text2, (x1, 140))
    text3 = font.render("at", True, (255, 255, 255))
    screen.blit(text3, (x1, 210))
    text3 = font.render("Freddy's", True, (255, 255, 255))
    screen.blit(text3, (x1, 290))
    text3 = font2.render("New Game", True, (255, 255, 255))
    screen.blit(text3, (x1, 500))
    text3 = font2.render("Continue", True, (255, 255, 255))
    screen.blit(text3, (x1, 580))
    text3 = font3.render("Night 1", True, (255, 255, 255))
    screen.blit(text3, (x1, 630))
    text3 = font3.render("funmade 2023", True, (176, 191, 163))
    screen.blit(text3, (x2, 750))
    text3 = font.render("options", True, (255, 255, 255))
    screen.blit(text3, (x2, 550))
    text3 = font3.render("Demo 0.0.1", True, (176, 191, 163))
    screen.blit(text3, (x1, 750))


    pygame.display.update()