import pygame
import sys
from pygame.locals import *
import time
from sys import exit

pygame.init()

largura = 1000
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Memória')
cor_fundo = (0, 200, 250)

fonte = pygame.font.SysFont('arial', 40, True, True)

def dificulade():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            pygame.draw.rect(tela, (0, 250, 0), (250, 220, 500, 70))
            pygame.draw.rect(tela, (250, 250, 0), (250, 330, 500, 70))
            pygame.draw.rect(tela, (250, 0, 0), (250, 440, 500, 70))
            texto = fonte.render("ESCOLHA A DIFICULDADE:", True, (255, 255, 255))
            texto1 = fonte.render("Fácil", True, (255, 255, 255))
            texto2 = fonte.render("Intermediário", True, (255, 255, 255))
            texto3 = fonte.render("Difícil", True, (255, 255, 255))
            tela.blit(texto, (250, 100))
            tela.blit(texto1, (450, 235))
            tela.blit(texto2, (380, 340))
            tela.blit(texto3, (450, 450))
            pygame.display.update()
        tela.fill(cor_fundo)


def jogofacil():
    telafacil = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Jogo da Memoria - Nível Fácil')
    pontos = 50
    tempo = 300
    cont = 0
    #imagemvirada = pygame.image.load('')
    while tempo > 0 and pontos > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(telafacil, (0, 255, 0), (0, 0, 400, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textotelafacil = fonte.render(textoniveis, True, (255, 255, 255))
        telafacil.blit(textotelafacil, (1, 1))
        #telafacil.blit(imagemvirada, (100, 100))
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        telafacil.blit(textotempo, (280, 1))
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        cor_fundo = (0, 0, 0)
        pygame.display.update()
        telafacil.fill(cor_fundo)

def jogointermediario():
    telaintermediario = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Jogo da Memoria - Nível Intermediário')
    pontos = 100
    tempo = 600
    cont = 0
    while tempo > 0 and pontos > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(telaintermediario, (220, 220, 0), (0, 0, 600, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textotelafacil = fonte.render(textoniveis, True, (255, 255, 255))
        telaintermediario.blit(textotelafacil, (1, 1))
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        telaintermediario.blit(textotempo, (485, 1))
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        cor_fundo = (0, 0, 0)
        pygame.display.update()
        telaintermediario.fill(cor_fundo)

def jogodificil():
    teladificil = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Jogo da Memoria - Nível Difícil')
    pontos = 150
    tempo = 900
    cont = 0
    while tempo > 0 and pontos > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(teladificil, (255, 0, 0), (0, 0, 1000, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textotelafacil = fonte.render(textoniveis, True, (255, 255, 255))
        teladificil.blit(textotelafacil, (1, 1))
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        teladificil.blit(textotempo, (880, 1))
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        cor_fundo = (0, 0, 0)
        pygame.display.update()
        teladificil.fill(cor_fundo)

        
def perdedor():
  telaperdedor = pygame.display.set_mode((500, 500))
  pygame.display.set_caption('Resultado')
  cont = 0
  fonte = pygame.font.SysFont('arial black', 40, True, True)
  cor_fundo = (0, 200, 250)
  while cont != 10:
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
      pygame.draw.rect(telaperdedor, (255, 0, 0), (130, 225, 280, 80))
      texto = fonte.render("Você Perdeu!", True, (250, 255, 255))
      telaperdedor.blit(texto, (165, 250))
      cont += 1
      time.sleep(1)
      pygame.display.update()
      telaperdedor.fill(cor_fundo)

def ganhador():
  telaganhador = pygame.display.set_mode((500, 500))
  pygame.display.set_caption('Resultado')
  cont = 0
  fonte = pygame.font.SysFont('arial black', 40, True, True)
  cor_fundo = (0, 200, 250)
  while cont != 10:
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
      pygame.draw.rect(telaganhador, (0, 255, 0), (130, 225, 280, 80))
      texto = fonte.render("Você Ganhou!", True, (250, 255, 255))
      telaganhador.blit(texto, (160, 250))
      cont += 1
      time.sleep(1)
      pygame.display.update()
      telaganhador.fill(cor_fundo)
