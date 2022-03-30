import pygame as pg
pg.init()
pg.display.set_caption("third")

WIDTH = 800
HEIGHT = 600
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
x, y = WIDTH // 2, HEIGHT - 150
r = 25




screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

is_running = True
lose = False


while is_running:
    screen.fill(GREEN)
    clock.tick(FPS)
   
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    if keys[pg.K_LEFT] and x>=45:
        x-= 20
    if keys[pg.K_RIGHT] and x<=755:
        x+= 20
    if keys[pg.K_UP] and y>=35:
        y -= 20
    if keys[pg.K_DOWN] and y<=565:
        y += 20

    

    
    pg.draw.circle(screen, RED, (x, y), r)


    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                lose = False
           

      
        pg.display.flip()
    pg.display.flip()
pg.quit()
