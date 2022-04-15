import pygame as pg
import random
import json
pg.init()
WIDTH = 800
HEIGHT = 600
FPS = 60
font2 = pg.font.SysFont("Verdana", 55, True, True)

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0,128,128)
score = 0
d = {}
d['highscore'] = -1
y = 0
money =0 
ry = 2
pg.mixer.init()
pg.mixer.music.load("./music/background.mp3")
pg.mixer.music.play(-1)
lose = False
MEGA_COIN = pg.USEREVENT + 1
FREEZE = pg.USEREVENT + 2
FLIP = pg.USEREVENT + 3

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("racer")
speed = random.randint(3, 5)

font = pg.font.SysFont('Times New Roman', 40)
pg.time.set_timer(FLIP, 150)

road = pg.image.load('./images/background.png')


with open('save.json', 'r', encoding='utf8') as f:
    x = f.read() 
      
d = json.loads(x)


class Player(pg.sprite.Sprite): # класс для игрока
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r'./images/player11.png')
        self.surf = pg.Surface((40, 60),pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(400, 500))
        self.speed = 5

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)
    

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Enemy(pg.sprite.Sprite): # класс для машин 
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r'./images/enemy.png')
        self.surf = pg.Surface((40, 60),pg.SRCALPHA)
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def ubivat(self):
        if self.rect.top > HEIGHT:
            self.kill()


class Coin(pg.sprite.Sprite): # класс для монеток
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((20, 20),pg.SRCALPHA)
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(1, 8)
        self.animation_index = 0
        self.random_number = random.randint(0, 9)
        self.images = [
           './coinim/c1.png',  # движение монеток
            './coinim/c2.png',
            './coinim/c3.png',
            './coinim/c4.png',
            './coinim/c5.png',
            './coinim/c6.png'
        ]
        self.image = pg.image.load(self.images[0])
        self.mega_coin()

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (20, 20)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def animate(self):
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.image = pg.image.load(self.images[self.animation_index])

    def ubivat(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def mega_coin(self):
        if self.random_number in [0, 1, 2]:
            self.image = pg.image.load(self.images[1])
            # self.speed = 15
        else:
            self.image = pg.image.load(self.images[0])

    def is_mega_coin(self):
        return self.random_number == 5


P1 = Player()
enemies = pg.sprite.Group([Enemy() for _ in range(3)])
coins = pg.sprite.Group([Coin() for _ in range(5)])
if score >= 20:
    P1.speed+=1

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == MEGA_COIN:
            P1.speed = 30
        if event.type == FLIP:
            for coin in coins:
                coin.animate()

    screen.fill(WHITE)
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, y % HEIGHT))
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, -HEIGHT + (y % HEIGHT)))

    y += ry

    P1.draw()
    P1.move()
    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.ubivat()

    for coin in coins:
        coin.draw()
        coin.move()
        # coin.animate()
        coin.ubivat()

    if enemies.__len__() < 3:
        enemies.add(Enemy())

    if coins.__len__() < 5:
        coins.add(Coin())

    if pg.sprite.spritecollide(P1, enemies, False): 
        lose = True
        losing = pg.mixer.Sound('crash.wav') # при столкновении музыка
        losing.play(1)
        running = False
        with open('save.json', 'w') as f:
            f.write(json.dumps(d, indent=4))

    for coin in pg.sprite.spritecollide(P1, coins, True):
        score += 1
        pickcoin = pg.mixer.Sound('pickcoinc.mp3')
        pickcoin.play(0)
        if coin.is_mega_coin():
            score += 100
            pg.time.set_timer(MEGA_COIN, 5000, loops=False)

    if score > d['highscore']:
        d['highscore'] = score

    text = font.render(f"{score}", True, FUCHSIA)
    screen.blit(text, (20, 20))
    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                lose = False
        pg.mixer.music.stop()        
       
        
        pg.draw.rect(screen, (0,0,0), (0,0, 800, 600))
        text1 = font2.render('GAME OVER', True,(FUCHSIA))        
        screen.blit(text1, (WIDTH // 2 - 175, HEIGHT // 2 - 60))
        
        pg.display.flip()
    pg.display.update()
pg.quit()