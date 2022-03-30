import pygame as pg
import datetime
pg.init()
pg.display.set_caption("Sagat")



WIDTH = 800
HEIGHT = 600
FPS = 60

background_img = pg.image.load("./back.png")
background_img = pg.transform.scale(background_img, (WIDTH, HEIGHT))
background_img2 = pg.image.load("./ruka2.png")

background_img3 = pg.image.load("./ruka1.png")

screen = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.SysFont("Times New Roman", 40, True)
done = True
#pg.SRCALPHA
def blitRotate2(surf, image, topleft, angle):
    
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    
def angle(x):
    return 360-6*x
while done:
    screen.fill((0,0,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = False
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    
    
    
    
    screen.blit(background_img, (0, 0))
    
    blitRotate2(screen, background_img3, (250,150),angle(second))
    blitRotate2(screen, background_img2, (250,150),angle(minute))
    
    pg.display.flip()
pg.quit()