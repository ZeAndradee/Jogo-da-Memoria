import pygame
import sys
from pygame.locals import *
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import time
from random import randint


pygame.init()

imagemvirada = pygame.image.load('pasta dos animais/quadrado-branco.jpg')
imagem1 = pygame.image.load('pasta dos animais/água viva.jpg')
imagem2 = pygame.image.load('pasta dos animais/cachorro.jpg')
imagem3 = pygame.image.load('pasta dos animais/Caracol.jpg')
imagem4 = pygame.image.load('pasta dos animais/baleia.jpg')
imagem5 = pygame.image.load('pasta dos animais/Coala.jpg')
imagem6 = pygame.image.load('pasta dos animais/Cervo.jpg')
imagem7 = pygame.image.load('pasta dos animais/coruja.jpg')
imagem8 = pygame.image.load('pasta dos animais/Butterfly.jpg')
imagem9 = pygame.image.load('pasta dos animais/girafa.jpg')
imagem10 = pygame.image.load('pasta dos animais/Patolino.jpg')
imagem11 = pygame.image.load('pasta dos animais/peixe.jpg')
imagem12 = pygame.image.load('pasta dos animais/Sapo.jpg')
imagem13 = pygame.image.load('pasta dos animais/elefante.jpg')
imagem14 = pygame.image.load('pasta dos animais/tucano.jpg')
imagem15 = pygame.image.load('pasta dos animais/raposa.jpg')
imagem16 = pygame.image.load('pasta dos animais/shark.jpg')
imagem17 = pygame.image.load('pasta dos animais/turtle.jpg')
imagem18 = pygame.image.load('pasta dos animais/rato que voa.jpg')
imagem19 = pygame.image.load('pasta dos animais/Spider.jpg')
imagem20 = pygame.image.load('pasta dos animais/golfinho.jpg')

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


def ganhador():
    pygame.draw.rect(telaganhador, (0, 200, 0), (150, 200, 100, 100))
    telaganhador = pygame.display.set_mode((200, 200))
    fonte = pygame.font.Font('arial', 36)
    textoniveis = f'Você ganhou'
    textotelaganhador = fonte.render(textoniveis, True, (255, 255, 255))
    telaganhador.blit(textotelaganhador, (150, 200))


def perdedor():
    pygame.draw.rect(perdedor, (200, 0), (150, 200, 100, 100))
    telaperdedor = pygame.display.set_mode((200, 200))
    fonte = pygame.font.Font('arial', 36)
    textoniveis = f'Game Over'
    textotelaperdedor = fonte.render(textoniveis, True, (255, 255, 255))
    telaperdedor.blit(textotelaperdedor, (150, 200))


import pygame
import sys
from pygame.locals import *
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import time


pygame.init()

imagemvirada = pygame.image.load('pasta dos animais/quadrado-branco.jpg')
imagem1 = pygame.image.load('pasta dos animais/água viva.jpg')
imagem2 = pygame.image.load('pasta dos animais/cachorro.jpg')
imagem3 = pygame.image.load('pasta dos animais/Caracol.jpg')
imagem4 = pygame.image.load('pasta dos animais/baleia.jpg')
imagem5 = pygame.image.load('pasta dos animais/Coala.jpg')
imagem6 = pygame.image.load('pasta dos animais/Cervo.jpg')
imagem7 = pygame.image.load('pasta dos animais/coruja.jpg')
imagem8 = pygame.image.load('pasta dos animais/Butterfly.jpg')
imagem9 = pygame.image.load('pasta dos animais/girafa.jpg')
imagem10 = pygame.image.load('pasta dos animais/Patolino.jpg')
imagem11 = pygame.image.load('pasta dos animais/peixe.jpg')
imagem12 = pygame.image.load('pasta dos animais/Sapo.jpg')
imagem13 = pygame.image.load('pasta dos animais/elefante.jpg')
imagem14 = pygame.image.load('pasta dos animais/tucano.jpg')
imagem15 = pygame.image.load('pasta dos animais/raposa.jpg')
imagem16 = pygame.image.load('pasta dos animais/shark.jpg')
imagem17 = pygame.image.load('pasta dos animais/turtle.jpg')
imagem18 = pygame.image.load('pasta dos animais/rato que voa.jpg')
imagem19 = pygame.image.load('pasta dos animais/Spider.jpg')
imagem20 = pygame.image.load('pasta dos animais/golfinho.jpg')

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


def ganhador():
    pygame.draw.rect(telaganhador, (0, 200, 0), (150, 200, 100, 100))
    telaganhador = pygame.display.set_mode((200, 200))
    fonte = pygame.font.Font('arial', 36)
    textoniveis = f'Você ganhou'
    textotelaganhador = fonte.render(textoniveis, True, (255, 255, 255))
    telaganhador.blit(textotelaganhador, (150, 200))


def perdedor():
    pygame.draw.rect(perdedor, (200, 0), (150, 200, 100, 100))
    telaperdedor = pygame.display.set_mode((200, 200))
    fonte = pygame.font.Font('arial', 36)
    textoniveis = f'Game Over'
    textotelaperdedor = fonte.render(textoniveis, True, (255, 255, 255))
    telaperdedor.blit(textotelaperdedor, (150, 200))


def modo_facil():
    imagemvirada = pygame.image.load('pasta dos animais/quadrado-branco.jpg')
    imagem1 = pygame.image.load('pasta dos animais/água viva.jpg')
    imagem2 = pygame.image.load('pasta dos animais/cachorro.jpg')
    imagem3 = pygame.image.load('pasta dos animais/Caracol.jpg')
    imagem4 = pygame.image.load('pasta dos animais/baleia.jpg')
    imagem5 = pygame.image.load('pasta dos animais/Coala.jpg')
    imagem6 = pygame.image.load('pasta dos animais/Cervo.jpg')
    posicao_botão1 = (100, 100)
    posicao_botão2 = (150, 150)
    posicao_botão3 = (200, 200)
    posicao_botão4 = (250, 250)
    posicao_botão5 = (300, 300)
    posicao_botão6 = (350, 350)
    largurabotão1, alturabotão1 = imagem1.get_size()
    largurabotão2, alturabotão2 = imagem2.get_size()
    largurabotão3, alturabotão3 = imagem3.get_size()
    largurabotão4, alturabotão4 = imagem4.get_size()
    largurabotão5, alturabotão5 = imagem5.get_size()
    largurabotão6, alturabotão6 = imagem6.get_size()
    telafacil = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Jogo da Memoria - Nível Fácil')
    pontos = 50
    tempo = 300
    cont = 0
    Num_imagens = 6
    posicaoimagens = []
    listaimagensfacil = [imagem1, imagem1, imagem2, imagem2, imagem3, imagem3, imagem4, imagem4, imagem5, imagem5]
    listaposicoesfacil = [(100, 100), (150, 150), (200, 200), (250, 250), (300, 300), (350, 350)]
    posicoesaleatorias = sorted(listaposicoesfacil)
    listaimagensapagada = []
    carta_virada = [False, False, False, False, False, False, False, False, False, False]
    while True:
        escolhausuario1 = 0
        escolhausuario2 = 0
        for i in range(Num_imagens):
            posicaoimagens.append(posicoesaleatorias[i])
            if carta_virada[i]:
                telafacil.blit(imagemvirada, (posicoesaleatorias[i]))
            else:
                telafacil.blit(listaimagensfacil[i], (posicoesaleatorias[i]))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(telafacil, (0, 255, 0), (0, 0, 400, 25))
        fonte = pygame.font.SysFont('arial', 20, True, True)
        textoniveis = f'Pontos: {pontos}'
        textotelafacil = fonte.render(textoniveis, True, (255, 255, 255))
        telafacil.blit(textotelafacil, (1, 1))
        telafacil.blit(imagem1, posicao_botão1)
        for evento1 in pygame.event.get():
            if evento1.type == QUIT:
                pygame.quit()
                sys.exit()

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão1[0] <= mouse_pos[0] <= posicao_botão1[0] + largurabotão1 and \
                        posicao_botão1[1] <= mouse_pos[1] <= posicao_botão1[1] + alturabotão1:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[0]:
                            del imagemvirada[posicoesaleatorias[0]]
                            telafacil.blit(imagem1, posicoesaleatorias[0])
                            escolhausuario1 = 1
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[0]:
                            del imagemvirada[posicoesaleatorias[0]]
                            telafacil.blit(imagem1, posicoesaleatorias[0])
                            escolhausuario2 = 1

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão1[0] <= mouse_pos[0] <= posicao_botão1[0] + largurabotão1 and \
                        posicao_botão1[1] <= mouse_pos[1] <= posicao_botão1[1] + alturabotão1:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[1]:
                            del imagemvirada[posicoesaleatorias[1]]
                            telafacil.blit(imagem1, posicoesaleatorias[1])
                            escolhausuario1 = 1
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[1]:
                            del imagemvirada[posicoesaleatorias[1]]
                            telafacil.blit(imagem1, posicoesaleatorias[1])
                            escolhausuario2 == 1

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão2[0] <= mouse_pos[0] <= posicao_botão2[0] + largurabotão2 and \
                        posicao_botão2[2] <= mouse_pos[2] <= posicao_botão2[2] + alturabotão2:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[2]:
                            del imagemvirada[posicoesaleatorias[2]]
                            telafacil.blit(imagem2, posicoesaleatorias[2])
                            escolhausuario1 == 2
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[2]:
                            del imagemvirada[posicoesaleatorias[2]]
                            telafacil.blit(imagem2, posicoesaleatorias[2])
                            escolhausuario2 == 2

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão2[0] <= mouse_pos[0] <= posicao_botão2[0] + largurabotão2 and \
                        posicao_botão2[2] <= mouse_pos[2] <= posicao_botão2[2] + alturabotão2:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[3]:
                            del imagemvirada[posicoesaleatorias[3]]
                            telafacil.blit(imagem2, posicoesaleatorias[3])
                            escolhausuario1 = 2
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[3]:
                            del imagemvirada[posicoesaleatorias[3]]
                            telafacil.blit(imagem2, posicoesaleatorias[3])
                            escolhausuario2 = 2

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão3[0] <= mouse_pos[0] <= posicao_botão3[0] + largurabotão3 and \
                        posicao_botão3[3] <= mouse_pos[3] <= posicao_botão3[3] + alturabotão3:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[4]:
                            del imagemvirada[posicoesaleatorias[4]]
                            telafacil.blit(imagem3, posicoesaleatorias[4])
                            escolhausuario1 = 3
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[4]:
                            del imagemvirada[posicoesaleatorias[4]]
                            telafacil.blit(imagem3, posicoesaleatorias[4])
                            escolhausuario2 = 3

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão3[0] <= mouse_pos[0] <= posicao_botão3[0] + largurabotão3 and \
                        posicao_botão3[3] <= mouse_pos[3] <= posicao_botão3[3] + alturabotão3:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[5]:
                            del imagemvirada[posicoesaleatorias[5]]
                            telafacil.blit(imagem3, posicoesaleatorias[5])
                            escolhausuario1 = 3
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[5]:
                            del imagemvirada[posicoesaleatorias[5]]
                            telafacil.blit(imagem3, posicoesaleatorias[5])
                            escolhausuario2 = 3

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão4[0] <= mouse_pos[0] <= posicao_botão4[0] + largurabotão4 and \
                        posicao_botão4[4] <= mouse_pos[4] <= posicao_botão4[4] + alturabotão4:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[6]:
                            del imagemvirada[posicoesaleatorias[6]]
                            telafacil.blit(imagem4, posicoesaleatorias[6])
                            escolhausuario1 = 4
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[6]:
                            del imagemvirada[posicoesaleatorias[6]]
                            telafacil.blit(imagem4, posicoesaleatorias[6])
                            escolhausuario2 = 4

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão4[0] <= mouse_pos[0] <= posicao_botão4[0] + largurabotão4 and \
                        posicao_botão4[4] <= mouse_pos[4] <= posicao_botão4[4] + alturabotão4:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[7]:
                            del imagemvirada[posicoesaleatorias[7]]
                            telafacil.blit(imagem4, posicoesaleatorias[7])
                            escolhausuario1 = 4
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[7]:
                            del imagemvirada[posicoesaleatorias[7]]
                            telafacil.blit(imagem4, posicoesaleatorias[7])
                            escolhausuario2 == 4

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão5[0] <= mouse_pos[0] <= posicao_botão5[0] + largurabotão5 and \
                        posicao_botão5[5] <= mouse_pos[5] <= posicao_botão5[5] + alturabotão5:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[8]:
                            del imagemvirada[posicoesaleatorias[8]]
                            telafacil.blit(imagem5, posicoesaleatorias[8])
                            escolhausuario1 == 5
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[8]:
                            del imagemvirada[posicoesaleatorias[8]]
                            telafacil.blit(imagem5, posicoesaleatorias[8])
                            escolhausuario2 == 5

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão5[0] <= mouse_pos[0] <= posicao_botão5[0] + largurabotão5 and \
                        posicao_botão5[5] <= mouse_pos[5] <= posicao_botão5[5] + alturabotão5:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[9]:
                            del imagemvirada[posicoesaleatorias[9]]
                            telafacil.blit(imagem5, posicoesaleatorias[9])
                            escolhausuario1 = 5
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[9]:
                            del imagemvirada[posicoesaleatorias[9]]
                            telafacil.blit(imagem5, posicoesaleatorias[9])
                            escolhausuario2 = 5

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão6[0] <= mouse_pos[0] <= posicao_botão6[0] + largurabotão6 and \
                        posicao_botão6[6] <= mouse_pos[6] <= posicao_botão6[6] + alturabotão6:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[10]:
                            del imagemvirada[posicoesaleatorias[10]]
                            telafacil.blit(imagem5, posicoesaleatorias[10])
                            escolhausuario1 = 6
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[10]:
                            del imagemvirada[posicoesaleatorias[10]]
                            telafacil.blit(imagem5, posicoesaleatorias[10])
                            escolhausuario2 = 6

            elif evento1.type == MOUSEBUTTONDOWN:
                mouse_pos == pygame.mouse.get_pos()
                if posicao_botão6[0] <= mouse_pos[0] <= posicao_botão6[0] + largurabotão6 and \
                        posicao_botão6[6] <= mouse_pos[6] <= posicao_botão6[6] + alturabotão6:
                    for escolha1 in range(0, 2):
                        if escolha1 == listaimagensfacil[11]:
                            del imagemvirada[posicoesaleatorias[11]]
                            telafacil.blit(imagem6, posicoesaleatorias[11])
                            escolhausuario1 = 6
                    for escolha2 in range(0, 2):
                        if escolha2 == listaimagensfacil[11]:
                            del imagemvirada[posicoesaleatorias[11]]
                            telafacil.blit(imagem6, posicoesaleatorias[11])
                            escolhausuario2 = 6

                if escolhausuario1 == escolhausuario2:
                    pontos += 2
                    del carta_virada[escolhausuario1 - 1]
                    del carta_virada[escolhausuario1 + 1]
                    carta_virada.insert(escolhausuario1, True)
                    carta_virada.insert(escolhausuario1, True)
                    
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
                pygame.display.flip()
                pygame.display.update()
                telafacil.fill(cor_fundo)
        pygame.quit()

def modo_intermédiario():
    cor_fundo2 = (0, 0, 0)
    telaintermediario = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Jogo da Memoria - Nível Intermediário')
    pontos = 100
    tempo = 600
    cont = 0
    rodada = 0
    Num_imagens = 12
    posicaoimagens = []

    listaimagensintermediario = [imagem1, imagem2, imagem3, imagem4, imagem5, imagem6, imagem7, imagem8, imagem9,
                                 imagem10,
                                 imagem11, imagem12]

    listaimagensviradas = [imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
                           imagemvirada,
                           imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
                           imagemvirada, imagemvirada]

    listaposicoesintermediario = [(50, 50), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300), (350, 350),
                                  (400, 400), (450, 450), (500, 500), (550, 550), (600, 600)]

    posicoesaleatorias = sorted(listaimagensintermediario)
    listaimagensapagada = []
    while tempo > 0 and pontos > 0:
        cont2 = 0
        cont3 = 0
        cont4 = -1
        b = 0
        c = 1
        for x in range(0, Num_imagens, 2):
            posicaoimagens.append(posicoesaleatorias[cont2])
            posicaoimagens.append(posicoesaleatorias[cont3])
            telaintermediario.blit(listaimagensintermediario[cont2], (posicoesaleatorias[b]))
            telaintermediario.blit(listaimagensintermediario[cont3], (posicoesaleatorias[c]))
            telaintermediario.blit(imagemvirada, (posicoesaleatorias[c]))
            telaintermediario.blit(imagemvirada, (posicoesaleatorias[x]))
            cont2 += 1
            b += 2
            c += 2
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
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[0]
                del listaimagensviradas[0]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[0]
                del listaimagensviradas[0]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[1]
                del listaimagensviradas[1]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[1]
                del listaimagensviradas[1]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[2]
                del listaimagensviradas[2]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[2]
                del listaimagensviradas[2]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[3]
                del listaimagensviradas[3]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[3]
                del listaimagensviradas[3]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[4]
                del listaimagensviradas[4]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[4]
                del listaimagensviradas[4]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[5]
                del listaimagensviradas[5]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[5]
                del listaimagensviradas[5]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[6]
                del listaimagensviradas[6]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[6]
                del listaimagensviradas[6]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[7]
                del listaimagensviradas[7]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[7]
                del listaimagensviradas[7]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[8]
                del listaimagensviradas[8]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[8]
                del listaimagensviradas[8]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[9]
                del listaimagensviradas[9]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[9]
                del listaimagensviradas[9]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[10]
                del listaimagensviradas[10]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[10]
                del listaimagensviradas[10]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[11]
                del listaimagensviradas[11]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[11]
                del listaimagensviradas[11]
            for c in range(0, 16, 2):
                cont4 += 2
                if c < 12:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesintermediario.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesintermediario.pop(c)
                        listaposicoesintermediario.pop(cont4)

                if c == 12:
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
                        tempo -= 1
                        telaintermediario.blit(imagemvirada, (posicoesaleatorias[c]))
                        telaintermediario.blit(imagemvirada, (posicoesaleatorias[cont4]))
            rodada += 1
            if len(listaimagensapagada) == 12:
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


def modo_dificil():
    teladificil = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Jogo da Memoria - Nível Difícil')
    pontos = 150
    tempo = 900
    cont = 0
    rodada = 0
    Num_imagens = 19
    posicaoimagens = []

    listaimagensdificil = [imagem1, imagem2, imagem3, imagem4, imagem5, imagem6, imagem7, imagem8, imagem9, imagem10,
                           imagem11, imagem12, imagem13, imagem14, imagem15, imagem16, imagem17, imagem18, imagem19]

    listaimagensviradas = [imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
                           imagemvirada,
                           imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada,
                           imagemvirada, imagemvirada,
                           imagemvirada, imagemvirada, imagemvirada, imagemvirada, imagemvirada]
    listaimagensapagada = []
    listaposicoesdificil = [(50, 100), (100, 150), (150, 200), (200, 250), (250, 300), (300, 350), (350, 400), (400, 450),
                            (450, 500), (500, 550), (550, 600), (600, 650), (650, 700), (700, 750), (750, 800),
                            (800, 850), (850, 900), (900, 950), (950, 1000)]
    posicoesaleatorias = sorted(listaposicoesdificil)
    while tempo > 0 and pontos > 0:
        cont2 = 0
        cont3 = 0
        cont4 = -1
        b = 0
        c = 1
        for x in range(0, Num_imagens, 2):
            posicaoimagens.append(posicoesaleatorias[cont2])
            posicaoimagens.append(posicoesaleatorias[cont3])
            teladificil.blit(listaimagensdificil[cont2], (posicoesaleatorias[b]))
            teladificil.blit(listaimagensdificil[cont3], (posicoesaleatorias[c]))
            teladificil.blit(imagemvirada, (posicoesaleatorias[c]))
            teladificil.blit(imagemvirada, (posicoesaleatorias[x]))
            cont2 += 1
            b += 2
            c += 2
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
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[0]
                del listaimagensviradas[0]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[1]
                del listaimagensviradas[1]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[2]
                del listaimagensviradas[2]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[3]
                del listaimagensviradas[3]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[4]
                del listaimagensviradas[4]
            if escolha == MOUSEBUTTONDOWN:
                escolha2 = posicoesaleatorias[5]
                del listaimagensviradas[5]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[6]
                del listaimagensviradas[6]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[7]
                del listaimagensviradas[7]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[8]
                del listaimagensviradas[8]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[9]
                del listaimagensviradas[9]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[10]
                del listaimagensviradas[10]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[11]
                del listaimagensviradas[11]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[12]
                del listaimagensviradas[12]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[13]
                del listaimagensviradas[13]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[14]
                del listaimagensviradas[14]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[15]
                del listaimagensviradas[15]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[16]
                del listaimagensviradas[16]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[17]
                del listaimagensviradas[17]
            if escolha == MOUSEBUTTONDOWN:
                escolha1 = posicoesaleatorias[18]
                del listaimagensviradas[18]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[0]
                del listaimagensviradas[0]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[1]
                del listaimagensviradas[1]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[2]
                del listaimagensviradas[2]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[3]
                del listaimagensviradas[3]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[4]
                del listaimagensviradas[4]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[5]
                del listaimagensviradas[5]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[6]
                del listaimagensviradas[6]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[7]
                del listaimagensviradas[7]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[8]
                del listaimagensviradas[8]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[9]
                del listaimagensviradas[9]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[10]
                del listaimagensviradas[10]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[11]
                del listaimagensviradas[11]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[12]
                del listaimagensviradas[12]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[13]
                del listaimagensviradas[13]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[14]
                del listaimagensviradas[14]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[15]
                del listaimagensviradas[15]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[16]
                del listaimagensviradas[16]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[17]
                del listaimagensviradas[17]
            if escolha == MOUSEBUTTONUP:
                escolha2 = posicoesaleatorias[18]
                del listaimagensviradas[18]

            for c in range(0, 21, 2):
                cont4 += 2
                if c < 19:
                    if escolha1 + escolha2 == posicoesaleatorias[c] + posicoesaleatorias[cont4]:
                        pontos += 2
                        listaposicoesdificil.append(posicoesaleatorias[c])
                        posicoesaleatorias.append([cont4])
                        listaimagensviradas.pop(c)
                        listaimagensviradas.pop(cont4)
                        listaposicoesdificil.pop(c)
                        listaposicoesdificil.pop(cont4)

                if c == 19:
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
                        tempo -= 1
                        teladificil.blit(imagemvirada, (posicoesaleatorias[c]))
                        teladificil.blit(imagemvirada, (posicoesaleatorias[cont4]))
            rodada += 1
            if len(listaimagensapagada) == 19:
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