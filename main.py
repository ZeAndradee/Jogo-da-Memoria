import pygame
from pygame.locals import *


pygame.init()

largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
cor_fundo = (0, 0, 170)
cor_botao = (255, 0, 150)

largura_botao = 200
altura_botao = 100
posicao_botao = ((largura_janela - largura_botao) // 2, (altura_janela - altura_botao) // 2)

fonte = pygame.font.Font(None, 36)
texto = fonte.render("Jogar", True, (255, 255, 255))
largura_texto = texto.get_width()
altura_texto = texto.get_height()
posicao_texto = ((largura_botao - largura_texto) // 2, (altura_botao - altura_texto) // 2)

clock = pygame.time.Clock()


def iniciar_jogo():
    nova_altura = 800
    nova_largura = 600
    nova_janela = pygame.display.set_mode((nova_largura, nova_altura))
    nova_janela.fill('purple')

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
                iniciar_jogo()
    
    janela.fill(cor_fundo)
    desenhar_botao()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()