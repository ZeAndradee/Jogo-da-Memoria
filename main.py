import pygame
from pygame.locals import *


pygame.init()

largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
cor_fundo = (100, 170, 100)
cor_botao = (200, 70, 100)

largura_botao = 200
altura_botao = 100
posicao_botao = ((largura_janela - largura_botao) // 2, (altura_janela - altura_botao) // 2)

fonte = pygame.font.Font(None, 36)
texto = fonte.render("Jogar", True, (255, 255, 255))
largura_texto = texto.get_width()
altura_texto = texto.get_height()
posicao_texto = ((largura_botao - largura_texto) // 2, (altura_botao - altura_texto) // 2)

clock = pygame.time.Clock()

def criar_nova_janela():
    nova_largura = 800
    nova_altura = 600
    nova_janela = pygame.display.set_mode((nova_largura, nova_altura))
    nova_cor_fundo = (170, 100, 0)
    def desenhando_botões():
        pygame.draw.rect(nova_janela, (0, 250, 0), (150, 220, 500, 70))
        pygame.draw.rect(nova_janela, (250, 250, 0), (150, 330, 500, 70))
        pygame.draw.rect(nova_janela, (250, 0, 0), (150, 440, 500, 70))
        texto = fonte.render("ESCOLHA A DIFICULDADE:", True, (255, 255, 255))
        texto1 = fonte.render("Fácil", True, (255, 255, 255))
        texto2 = fonte.render("Intermediário", True, (255, 255, 255))
        texto3 = fonte.render("Difícil", True, (255, 255, 255))
        nova_janela.blit(texto, (200, 100))
        nova_janela.blit(texto1, (380, 235))
        nova_janela.blit(texto2, (340, 340))
        nova_janela.blit(texto3, (380, 450))
        pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                return

        nova_janela.fill(nova_cor_fundo)
        desenhando_botões()
        pygame.display.flip()
        clock.tick(30)

def desenhar_botao():
    pygame.draw.rect(janela, cor_botao, (posicao_botao, (largura_botao, altura_botao)))
    janela.blit(texto, (posicao_botao[0] + posicao_texto[0], posicao_botao[1] + posicao_texto[1]))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        elif evento.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if posicao_botao[0] <= mouse_pos[0] <= posicao_botao[0] + largura_botao and \
               posicao_botao[1] <= mouse_pos[1] <= posicao_botao[1] + altura_botao:
                criar_nova_janela()

    janela.fill(cor_fundo)
    desenhar_botao()
    pygame.display.flip()
    clock.tick(30)

pygame.quit