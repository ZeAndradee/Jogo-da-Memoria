import pygame
import sys 
from pygame.locals import *
import time
<<<<<<< HEAD


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
    cor_fundo1 = (0,0,0)
=======
from random import randint

pygame.init()

imagemvirada = pygame.image.load('')
imagem1 = pygame.image.load('')
imagem2 = pygame.image.load('')
imagem3 = pygame.image.load('')
imagem4 = pygame.image.load('')
imagem5 = pygame.image.load('')
imagem6 = pygame.image.load('')
imagem7 = pygame.image.load('')
imagem8 = pygame.image.load('')
imagem9 = pygame.image.load('')
imagem10 = pygame.image.load('')
imagem11 = pygame.image.load('')
imagem12 = pygame.image.load('')
imagem13 = pygame.image.load('')
imagem14 = pygame.image.load('')
imagem15 = pygame.image.load('')
imagem16 = pygame.image.load('')
imagem17 = pygame.image.load('')
imagem18 = pygame.image.load('')
imagem19 = pygame.image.load('')
imagem20 = pygame.image.load('')

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
>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
    telafacil = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Jogo da Memoria - Nível Fácil')
    pontos = 50
    tempo = 300
    cont = 0
    rodada = 0
    posicaoimagens = []
    listaimagensfacil = [imagem1, imagem2, imagem3, imagem4, imagem5]
    listaimagensviradas = [imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada]
    listaposicoesfacil = [(colocar posicoes selecionadas em tuplas), (0,0), (0,0), (0,0), (0,0)]
    posicoesaleatorias = randint(listaimagensfacil)
    listaimagensapagada = []
    while True:
        cont2 = 0
        cont3 = 0
        cont4 = -1
        for x in range(0, 11, 2):
            posicaoimagens.append(posicoesaleatorias[cont2])
            telafacil.blit(listaimagensfacil[cont2], (posicoesaleatorias[x]))
            telafacil.blit(imagemvirada, (posicoesaleatorias[x]))
            cont2 += 1
        for x in range(1, 11, 2):
            posicaoimagens.append(posicoesaleatorias[cont3])
            telafacil.blit(listaimagensfacil[cont3], (posicoesaleatorias[x]))
            telafacil.blit(imagemvirada, (posicoesaleatorias[x]))
            cont3 += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(telafacil, (0, 255, 0), (0, 0, 400, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textotelafacil = fonte.render(textoniveis, True, (255, 255, 255))
        telafacil.blit(textotelafacil, (1, 1))
        for escolha in range(0, 2):
            # configurar todas as posicões das cartas como botões
            #escolha == MOUSEBUTTONUP:
                #escolha1 = guardar a posicção em que q a posição da imagem apagada estava na lista de posições
                #imagemvirada.pop(listaimagensviradas[posicao da imagem apagada])
            #escolha == MOUSEBUTTONUP:
                #escolha2 =  guardar a posicção em que q a posição da imagem apagada estava na lista de posições
                #imagemvirada.pop(listaimagensviradas[posicao da imagem apagada])
            for c in range(0, 11, 2):
                cont4 += 2
                if c < 10:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesfacil.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesfacil.pop(c)
                        listaposicoesfacil.pop(cont4)
                        
                if c == 10:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesfacil.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesfacil.pop(c)
                        listaposicoesfacil.pop(cont4)
                    else:
                        time.sleep(1)
                        tempo -= 1
                        time.sleep(1)
                        tempo -=(1)
                        telafacil.blit(imagemvirada, (posicoesaleatorias[c]))
                        telafacil.blit(imagemvirada, (posicoesaleatorias[cont4]))
            rodada += 1
            if len(listaimagensapagada) == 10:
                pontos += tempo
                ganhador() ir para tela de ganhador
            if tempo > 0 and pontos > 0:
                perdedor()
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        telafacil.blit(textotempo, (280, 1))
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        pygame.display.update()
<<<<<<< HEAD
        telafacil.fill(cor_fundo1)
def modo_intermédiario():
    cor_fundo2 = (0,0,0)
=======
        telafacil.fill(cor_fundo)


def modo_intermédiario():
    cor_fundo2 = (0, 0, 0)
>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
    telaintermediario = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Jogo da Memoria - Nível Intermediário')
    pontos = 100
    tempo = 600
    cont = 0
    posicaoimagens = []
    
    listaimagensintermediario = [imagem1, imagem2, imagem3, imagem4, imagem5, imagem6, imagem7, imagem8, imagem9, imagem10,
    imagem11, imagem12, imagem13, imagem14, imagem15]
    
    listaimagensviradas = [imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
    imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada]
    
    listaposicoesintermediario = [(colocar posicoes selecionadas em tuplas), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0),
    (0,0), (0,0), (0,0) +5]
    
    posicoesaleatorias = randint(listaimagensintermediarios)
    listaimagensapagada = []
    while tempo > 0 and pontos > 0:
        cont2 = 0
        cont3 = 0
        cont4 = -1
        for x in range(0, 16, 2):
            posicaoimagens.append(posicoesaleatorias[cont2])
            telaintermediario.blit(listaimagensintermediario[cont2], (posicoesaleatorias[x]))
            telaintermediario.blit(imagemvirada, (posicoesaleatorias[x]))
            cont2 += 1
        for x in range(1, 16, 2):
            posicaoimagens.append(posicoesaleatorias[cont3])
            telaintermediario.blit(listaimagensintermediario[cont3], (posicoesaleatorias[x]))
            telaintermediario.blit(imagemvirada, (posicoesaleatorias[x]))
            cont3 += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(telaintermediario, (220, 220, 0), (0, 0, 600, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textotelaintermediario = fonte.render(textoniveis, True, (255, 255, 255))
        telaintermediario.blit(textotelaintermediario, (1, 1))
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        telaintermediario.blit(textotempo, (485, 1))
        for escolha in range(0, 2):
            # configurar todas as posicões das cartas como botões
            #escolha == MOUSEBUTTONUP(n sei se é esse o comando):
                #escolha1 = guardar a posicção em que q a posição da imagem apagada estava na lista de posições
                #imagemvirada.pop(listaimagensviradas[posicao da imagem apagada])
            #escolha == MOUSEBUTTONUP(n sei se é esse):
                #escolha2 =  guardar a posicção em que q a posição da imagem apagada estava na lista de posições
                #imagemvirada.pop(listaimagensviradas[posicao da imagem apagada])
            for c in range(0, 16, 2):
                cont4 += 2
                if c < 15:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesintermediario.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesintermediario.pop(c)
                        listaposicoesintermediario.pop(cont4)
                        
                if c == 15:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesintermediario.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesintermediario.pop(c)
                        listaposicoesintermediario.pop(cont4)
                    else:
                        time.sleep(1)
                        tempo -= 1
                        time.sleep(1)
                        tempo -=(1)
                        telaintermediario.blit(imagemvirada, (posicoesaleatorias[c]))
                        telaintermediario.blit(imagemvirada, (posicoesaleatorias[cont4]))
            rodada += 1
            if len(listaimagensapagada) == 15 #numero de imagens q vai ter na tela:
                pontos += tempo
                ganhador()
            if tempo > 0 and pontos > 0:
                perdedor()
                
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        cor_fundo = (0, 0, 0)
        pygame.display.update()
        telaintermediario.fill(cor_fundo2)
<<<<<<< HEAD
=======


>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
def modo_dificil():
    teladificil = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Jogo da Memoria - Nível Difícil')
    pontos = 150
    tempo = 900
    cont = 0
    posicaoimagens = []
    
    listaimagensdificil = [imagem1, imagem2, imagem3, imagem4, imagem5, imagem6, imagem7, imagem8, imagem9, imagem10,
    imagem11, imagem12, imagem13, imagem14, imagem15, imagem16, imagem17, imagem18, imagem19, imagem20]
    
    listaimagensviradas = [imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
    imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
    imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada]
    
    listaposicoesdificil = [(colocar posicoes selecionadas em tuplas), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0),
    (0,0), (0,0), (0,0) +10]
    
    while tempo > 0 and pontos > 0:
        for x in range(0, 21, 2):
            posicaoimagens.append(posicoesaleatorias[cont2])
            teladificil.blit(listaimagensdificil[cont2], (posicoesaleatorias[x]))
            teladificil.blit(imagemvirada, (posicoesaleatorias[x]))
            cont2 += 1
        for x in range(1, 21, 2):
            posicaoimagens.append(posicoesaleatorias[cont3])
            teladificil.blit(listaimagensdificil[cont3], (posicoesaleatorias[x]))
            teladificil.blit(imagemvirada, (posicoesaleatorias[x]))
            cont3 += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(teladificil, (255, 0, 0), (0, 0, 1000, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textoteladificil = fonte.render(textoniveis, True, (255, 255, 255))
        teladificil.blit(textoteladificil, (1, 1))
        textotempo = fonte.render(f'Tempo: {tempo}', True, (255, 255, 255))
        teladificil.blit(textotempo, (880, 1))
        for escolha in range(0, 2):
            # configurar todas as posicões das cartas como botões
            #escolha == MOUSEBUTTONUP(n sei se é esse o comando):
                #escolha1 = guardar a posicção em que q a posição da imagem apagada estava na lista de posições
                #imagemvirada.pop(listaimagensviradas[posicao da imagem apagada])
            #escolha == MOUSEBUTTONUP(n sei se é esse):
                #escolha2 =  guardar a posicção em que q a posição da imagem apagada estava na lista de posições
                #imagemvirada.pop(listaimagensviradas[posicao da imagem apagada])
            for c in range(0, 21, 2):
                cont4 += 2
                if c < 20:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesdificil.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesdificil.pop(c)
                        listaposicoesdificil.pop(cont4)
                        
                if c == 20:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesdificil.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesdificil.pop(c)
                        listaposicoesdificil.pop(cont4)
                    else:
                        time.sleep(1)
                        tempo -= 1
                        time.sleep(1)
                        tempo -=(1)
                        teladificil.blit(imagemvirada, (posicoesaleatorias[c]))
                        teladificil.blit(imagemvirada, (posicoesaleatorias[cont4]))
            rodada += 1
            if len(listaimagensapagada) == 20 #numero de imagens q vai ter na tela:
                pontos += tempo
                ganhador()
            if tempo > 0 and pontos > 0:
                perdedor()
                
        tempo -= 1
        cont += 1
        time.sleep(1)
        if cont == 30:
            pontos -= 5
            cont -= 30
        cor_fundo3 = (0, 0, 0)
        pygame.display.update()
        teladificil.fill(cor_fundo3)
<<<<<<< HEAD
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
    altura_botao1 = 100
    posicao_botao1 = ((nova_largura - largura_botao1) // 2, (nova_altura - altura_botao1) // 2 - 120)
    largura_botao2 = 200
    altura_botao2 = 100
    posicao_botao2 = ((nova_largura - largura_botao2) // 2, (nova_altura - altura_botao2) // 2)
    largura_botao3 = 200
    altura_botao3 = 100
    posicao_botao3 = ((nova_largura - largura_botao3) // 2, (nova_altura - altura_botao3) // 2 + 120)

=======


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

>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
    def desenhar_botoes():
        pygame.draw.rect(nova_janela, cor_botao1, (posicao_botao1, (largura_botao1, altura_botao1)))
        pygame.draw.rect(nova_janela, cor_botao2, (posicao_botao2, (largura_botao2, altura_botao2)))
        pygame.draw.rect(nova_janela, cor_botao3, (posicao_botao3, (largura_botao3, altura_botao3)))
        nova_janela.blit(texto1, (posicao_botao1[0] + posicao_texto1[0], posicao_botao1[1] + posicao_texto1[1]))
        nova_janela.blit(texto2, (posicao_botao2[0] + posicao_texto2[0], posicao_botao2[1] + posicao_texto2[1]))
        nova_janela.blit(texto3, (posicao_botao3[0] + posicao_texto3[0], posicao_botao3[1] + posicao_texto3[1]))
<<<<<<< HEAD
    
=======

>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
    rodar2 = True
    while rodar2:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodar2 = False
            elif evento.type == MOUSEBUTTONDOWN:
                mouse_pos1 = pygame.mouse.get_pos()
                if posicao_botao1[0] <= mouse_pos1[0] <= posicao_botao1[0] + largura_botao1 and \
<<<<<<< HEAD
                   posicao_botao1[1] <= mouse_pos1[1] <= posicao_botao1[1] + altura_botao1:
                    modo_facil()
                elif posicao_botao2[0] <= mouse_pos1[0] <= posicao_botao2[0] + largura_botao2 and \
                     posicao_botao2[1] <= mouse_pos1[1] <= posicao_botao2[1] + altura_botao2:
                      modo_intermédiario()
                else:
                     posicao_botao3[0] <= mouse_pos1[0] <= posicao_botao3[0] + largura_botao3 and \
                     posicao_botao3[1] <= mouse_pos1[1] <= posicao_botao3[1] + altura_botao3
                     modo_dificil()
=======
                        posicao_botao1[1] <= mouse_pos1[1] <= posicao_botao1[1] + altura_botao1:
                    modo_facil()
                elif posicao_botao2[0] <= mouse_pos1[0] <= posicao_botao2[0] + largura_botao2 and \
                        posicao_botao2[1] <= mouse_pos1[1] <= posicao_botao2[1] + altura_botao2:
                    modo_intermédiario()
                else:
                    posicao_botao3[0] <= mouse_pos1[0] <= posicao_botao3[0] + largura_botao3 and \
                    posicao_botao3[1] <= mouse_pos1[1] <= posicao_botao3[1] + altura_botao3
                    modo_dificil()
>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8

        nova_janela.fill(nova_cor_fundo)
        desenhar_botoes()
        pygame.display.flip()
        clock.tick(30)

<<<<<<< HEAD
=======

>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
def desenhar_botao():
    pygame.draw.rect(janela, cor_botao, (posicao_botao, (largura_botao, altura_botao)))
    janela.blit(texto, (posicao_botao[0] + posicao_texto[0], posicao_botao[1] + posicao_texto[1]))

<<<<<<< HEAD
=======

>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        elif evento.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if posicao_botao[0] <= mouse_pos[0] <= posicao_botao[0] + largura_botao and \
<<<<<<< HEAD
               posicao_botao[1] <= mouse_pos[1] <= posicao_botao[1] + altura_botao:
=======
                    posicao_botao[1] <= mouse_pos[1] <= posicao_botao[1] + altura_botao:
>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
                criar_nova_janela()

    janela.fill(cor_fundo)
    desenhar_botao()
    pygame.display.flip()
    clock.tick(30)

<<<<<<< HEAD
pygame.quit()
=======
pygame.quit()
>>>>>>> 6f3197a95c51e4ca7aa8b0a6aa8c2f5f231e35c8
