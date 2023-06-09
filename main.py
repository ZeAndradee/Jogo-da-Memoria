import pygame
from pygame import *
from pygame.locals import *
from sys import exit

pygame.init()

largura = 500
altura = 500
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
pygame.display.set_caption('Jogo da memória')

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('attack_1.png'))
        self.sprites.append(pygame.image.load('attack_2.png'))
        self.sprites.append(pygame.image.load('attack_3.png'))
        self.sprites.append(pygame.image.load('attack_4.png'))
        self.sprites.append(pygame.image.load('attack_5.png'))
        self.sprites.append(pygame.image.load('attack_6.png'))
        self.sprites.append(pygame.image.load('attack_7.png'))
        self.sprites.append(pygame.image.load('attack_8.png'))
        self.sprites.append(pygame.image.load('attack_9.png'))
        self.sprites.append(pygame.image.load('attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
    
    def update(self):
        self.atual = self.atual + 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.atual = self.sprites[int(self.atual)]
        

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

while True:
    clock.tick(30)
    screen.fill((0,70,200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()             
    
        todas_as_sprites.draw(screen)
        todas_as_sprites.update()
    pygame.draw.rect(screen, (255,0,0), (150,200,200,60))
    pygame.font.init()
    fonte = pygame.font.SysFont('arial', 40, True, True)
    texto = fonte.render('Jogar', True, (255,255,255))
    screen.blit(texto ,(195,205))
    pygame.draw
    pygame.display.update()