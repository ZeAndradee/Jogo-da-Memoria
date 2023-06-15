import pygame
import sys
from pygame.locals import *
import time

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


def modo_facil():
    cor_fundo1 = (0, 0, 0)
    telafacil = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Jogo da Memoria - Nível Fácil')
    pontos = 50
    tempo = 300
    cont = 0
    # imagemvirada = pygame.image.load('')
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
        # telafacil.blit(imagemvirada, (100, 100))
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        telafacil.blit(textotempo, (280, 1))
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        pygame.display.update()
        telafacil.fill(cor_fundo1)


def modo_intermédiario():
    cor_fundo2 = (0, 0, 0)
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
        telaintermediario.fill(cor_fundo2)


def modo_dificil():
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
        cor_fundo3 = (0, 0, 0)
        pygame.display.update()
        teladificil.fill(cor_fundo3)


def criar_nova_janela():
    nova_largura = 800
    nova_altura = 600
    nova_janela = pygame.display.set_mode((nova_largura, nova_altura))
    nova_cor_fundo = (170, 100, 0)
    cor_botao1 = (0, 250, 0)
    cor_botao2 = (250, 250, 0)
    cor_botao3 = (250, 0, 0)
    texto1 = fonte.render("Fácil", True, (255, 255, 255))
    texto2 = fonte.render("Intermediário", True, (255, 255, 255))
    texto3 = fonte.render("Difícil", True, (255, 255, 255))
    posicao_texto1 = ((largura_botao - texto1.get_width()) // 2, (altura_botao - texto1.get_height()) // 2)
    posicao_texto2 = ((largura_botao - texto2.get_width()) // 2, (altura_botao - texto2.get_height()) // 2)
    posicao_texto3 = ((largura_botao - texto3.get_width()) // 2, (altura_botao - texto3.get_height()) // 2)
    largura_botao1 = 200
    altura_botao1 = 80
    posicao_botao1 = ((nova_largura - largura_botao1) // 2, (nova_altura - altura_botao1) // 2 - 120)
    largura_botao2 = 200
    altura_botao2 = 80
    posicao_botao2 = ((nova_largura - largura_botao2) // 2, (nova_altura - altura_botao2) // 2)
    largura_botao3 = 200
    altura_botao3 = 80
    posicao_botao3 = ((nova_largura - largura_botao3) // 2, (nova_altura - altura_botao3) // 2 + 120)

    def desenhar_botoes():
        pygame.draw.rect(nova_janela, cor_botao1, (posicao_botao1, (largura_botao1, altura_botao1)))
        pygame.draw.rect(nova_janela, cor_botao2, (posicao_botao2, (largura_botao2, altura_botao2)))
        pygame.draw.rect(nova_janela, cor_botao3, (posicao_botao3, (largura_botao3, altura_botao3)))
        nova_janela.blit(texto1, (posicao_botao1[0] + posicao_texto1[0], posicao_botao1[1] + posicao_texto1[1]))
        nova_janela.blit(texto2, (posicao_botao2[0] + posicao_texto2[0], posicao_botao2[1] + posicao_texto2[1]))
        nova_janela.blit(texto3, (posicao_botao3[0] + posicao_texto3[0], posicao_botao3[1] + posicao_texto3[1]))

    rodar2 = True
    while rodar2:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodar2 = False
            elif evento.type == MOUSEBUTTONDOWN:
                mouse_pos1 = pygame.mouse.get_pos()
                if posicao_botao1[0] <= mouse_pos1[0] <= posicao_botao1[0] + largura_botao1 and \
                        posicao_botao1[1] <= mouse_pos1[1] <= posicao_botao1[1] + altura_botao1:
                    modo_facil()
                elif posicao_botao2[0] <= mouse_pos1[0] <= posicao_botao2[0] + largura_botao2 and \
                        posicao_botao2[1] <= mouse_pos1[1] <= posicao_botao2[1] + altura_botao2:
                    modo_intermédiario()
                else:
                    posicao_botao3[0] <= mouse_pos1[0] <= posicao_botao3[0] + largura_botao3 and \
                    posicao_botao3[1] <= mouse_pos1[1] <= posicao_botao3[1] + altura_botao3
                    modo_dificil()

        nova_janela.fill(nova_cor_fundo)
        desenhar_botoes()
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

pygame.quit()
