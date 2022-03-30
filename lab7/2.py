
import pygame
import os
WIDTH, HEIGHT =400,600
pygame.init()
def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_prev_song():
    global _songs
    _songs =  [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


_songs = ['1.mp3.mp3','2.mp3.mp3','3.mp3.mp3','4.mp3.mp3','5.mp3.mp3','6.mp3.mp3']
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
background_img = pygame.image.load("./backside.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
font = pygame.font.SysFont("Times New Roman", 40, True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:  #kelesi
                pygame.mixer.music.stop()
                play_next_song()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                pygame.mixer.music.load('1.mp3.mp3')
                pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:    #artka
                pygame.mixer.music.stop()
                play_prev_song()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  #tokta
                pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:    #pausa
             pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:    #unpause
                pygame.mixer.music.unpause()
    screen.blit(background_img, (0,0))  
    

    pygame.display.flip()