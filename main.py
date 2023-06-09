import pygame
from pygame import *
from sys import exit
pygame.init()
largura = 500
altura = 500
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da memória')
while True:
    screen.fill((0,70,200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()             
    
    pygame.draw.rect(screen, (255,0,0), (150,200,200,60))
    pygame.font.init()
    fonte = pygame.font.SysFont('arial', 40, True, True)
    texto = fonte.render('Jogar', True, (255,255,255))
    screen.blit(texto ,(195,205))
    pygame.display.update()