import tkinter as tk
import customtkinter
from tkinter import *
import pygame
import sys
from pygame.locals import *
import time
import random

pygame.init()

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk()  
app.geometry("400x240")
app.title('Cadastramento')

usuarios = []
senhas = []

def switch_theme():
      if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
      else:
        customtkinter.set_appearance_mode("light")   

#tela de início
label = customtkinter.CTkLabel(app, text="Bem Vindo", font=customtkinter.CTkFont(size=20, weight="bold"))
label.place(x=150, y=30)

button = customtkinter.CTkButton(app, text='Fazer Login', command=lambda:abrir_login())
button.place(x=130, y= 100)

button = customtkinter.CTkButton(app, text='Cadastre-se', command=lambda:abrir_cadastro())
button.place(x=130, y= 150)

switch_var = customtkinter.StringVar(value="off")
switch = customtkinter.CTkSwitch(app, text="Dark Mode", command=switch_theme,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.place(x= 260, y= 200)


def abrir_login():
    # Criando uma nova janela com o Toplevel
    login_window = customtkinter.CTkToplevel()
    login_window.title("Tela de login")
    login_window.geometry("400x240")


    # Criando uma label com o custom tkinter
    label = customtkinter.CTkLabel(login_window, text="Tela login", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.place(x=150, y=10)

    #label nome
    label = customtkinter.CTkLabel(login_window, text="Apelido", font=customtkinter.CTkFont(size=12, weight="normal"))
    label.place(x=80, y=50)

    #Criando TextBox
    textbox = customtkinter.CTkTextbox(login_window, width=250, height=30, border_color= '#3b8ed0', border_width=2)
    textbox.place(x= 75, y=75)
    textbox.insert("0.0", "new text to insert") 
    textbox.delete("0.0", "end") 
    textbox.configure(state="normal")

    #asteristicos na senha


    def botao_entrar():
      usuarioL = textbox.get("0.0", "end").strip()
      usuarioS = textbox2.get("0.0", "end").strip()


      #recebe o input do login usuario
      with open("usuarios.txt", "r", encoding="utf-8") as u:   
        listaU = u.read().splitlines()
        #o split esta aqui para dividir os nomes em linhas 
            
        print(listaU)
            
        #Váriaveis User
        posicao = -1

        posicaoA = listaU.index(usuarioL)
        if usuarioL in listaU:
           print('Usuario: ', usuarioL)
           print('existe!')
           u.close()

           with open('senhas.txt', "r", encoding="utf-8") as s:
            listaS = s.read().splitlines()
            print(listaS)

            posicaoS = listaS.index(usuarioS)
            print(posicaoS, posicaoA)
            if posicaoS == posicaoA:
                print('O usuario e senha conferem.')
                abrir_jogo()
            else:
                print('Usuario: ', usuarioL)
                print('Usuário não existe.')
                print('Senha: ', usuarioS)
                print('Senha incorreta.')
      u.close()  


    #Botão Entrar
    button_login = customtkinter.CTkButton(login_window, text='Fazer Login', command=botao_entrar)
    button_login.place(x=130, y= 190)

    #Pesquisando usuarios

    labelsenha = customtkinter.CTkLabel(login_window, text="Senha", font=customtkinter.CTkFont(size=12, weight="normal"))
    labelsenha.place(x=80, y=120)

    #Criando TextBox
    textbox2 = customtkinter.CTkTextbox(login_window, width=250, height=30, border_color= '#3b8ed0', border_width=2)
    textbox2.place(x= 75, y=145)
    textbox2.insert("0.0", "new text to insert")
    textbox2.delete("0.0", "end")
    textbox2.configure(state="normal") 


def abrir_cadastro():
    #criando tela de cadastro
    cadastro_window = customtkinter.CTkToplevel()
    cadastro_window.title('Tela de Cadastro')
    cadastro_window.geometry("400x240")

    #criando label com nome 
    label3 = customtkinter.CTkLabel(cadastro_window, text= "Tela de Cadastro", font= customtkinter.CTkFont(size= 20, weight= "bold"))
    label3.place(x=120, y=10)

    #label apelido
    label = customtkinter.CTkLabel(cadastro_window, text="Apelido", font=customtkinter.CTkFont(size=12, weight="normal"))
    label.place(x=80, y=50)

    #criando textbox apelido
    textbox3 = customtkinter.CTkTextbox(cadastro_window, width=250, height=30, border_color= '#3b8ed0', border_width=2)
    textbox3.place(x= 75, y=75)
    textbox3.insert("0.0", "new text to insert") 
    
    textbox3.delete("0.0", "end")
    textbox3.configure(state="normal") 

    #criando senha
    labelsenha = customtkinter.CTkLabel(cadastro_window, text="Senha", font=customtkinter.CTkFont(size=12, weight="normal"))
    labelsenha.place(x=80, y=120)

    #criando textbox senha
    textbox2 = customtkinter.CTkTextbox(cadastro_window, width=250, height=30, border_color= '#3b8ed0', border_width=2)
    textbox2.place(x= 75, y=145)
    textbox2.insert("0.0", "new text to insert") 
    text2 = textbox2.get("0.0", "end") 
    textbox2.delete("0.0", "end")
    textbox2.configure(state="normal") 

    def botao_cadastrar():
      nickC = textbox3.get("0.0", "end").strip()
      senhaC = textbox2.get("0.0", "end").strip()

      #Verifica se o usuario já existe
      with open("usuarios.txt", "r") as u:
        listaU = u.read().splitlines()
        print(listaU)
        if nickC in listaU:
           print('O usuario já existe.')
        else:
           print('Usuario Adicionado.')
           #Adiciona o usuário a lista
           with open("usuarios.txt", "a+") as c: 
             listaU = c.write(nickC+'\n')
             c.close() 
           with open("senhas.txt", "a+") as s: 
             listaS = s.write(senhaC+'\n')
             s.close()   
        u.close()
          
          
    #botao cadastrar
    button_cadastrar = customtkinter.CTkButton(cadastro_window, text= 'Cadastrar', command= botao_cadastrar)
    button_cadastrar.place(x=130, y= 190)

def abrir_jogo():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    OLIVA = (128,128, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
    GRAY = (128, 128, 128)
    BROWN = (165, 42, 42)
    CYAN = (0, 255, 255)
    LIGHT_BLUE = (173, 216, 230)
    LIME = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    NAVY_BLUE = (0, 0, 128)

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

    def tela_perdedor():
        WIDTH = 500
        HEIGHT = 500
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tela Resultado')
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render("Você PERDEU!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()

    def tela_ganhador():
        WIDTH = 500
        HEIGHT = 500
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tela Resultado')
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render("Você VENCEU!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()

    def modo_facil():
        screen_width = 400
        screen_height = 400
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Jogo da Memória- Modo Facil")
        
        card_width = 88
        card_height = 100
        card_padding = 10

        fonte = pygame.font.Font(None, 36)

        colors = [GREEN, RED, BLUE, YELLOW, ORANGE, PINK]

        cards = [color for color in colors for _ in range(2)]
        random.shuffle(cards)

        flipped = []

        matched = []

        game_over = False
        pontos = 50
        tempo = 300
        cont = 0
        while not game_over:
            time.sleep(1)
            tempo -= 1
            cont += 1
            time.sleep(1)
            if cont == 30:
                pontos -= 5
                cont -= 30

            if pontos <= 0 or tempo <= 0:
                tela_perdedor()
                pygame.time.wait(3000)
                game_over = True

            if len(matched) == 12:
                tela_ganhador()
                pygame.time.wait(3000)
                game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_card = mouse_pos[0] // (card_width + card_padding), mouse_pos[1] // (card_height + card_padding)

                    if clicked_card not in flipped and clicked_card not in matched:
                        flipped.append(clicked_card)

                    if len(flipped) == 2:
                        card1, card2 = flipped
                        if cards[card1[1] * 4 + card1[0]] == cards[card2[1] * 4 + card2[0]]:
                            matched.extend(flipped)
                            pontos += 2
                        flipped = []

            screen.fill(BLACK)

            for i in range(4):
                for j in range(3):
                    card_index = j * 4 + i
                    x = i * (card_width + card_padding) + card_padding
                    y = j * (card_height + card_padding) + card_padding

                    if (i, j) in flipped or (i, j) in matched:
                        pygame.draw.rect(screen, cards[card_index], (x, y, card_width, card_height))
                    else:
                        pygame.draw.rect(screen, WHITE, (x, y, card_width, card_height))

            score_text = fonte.render("Pontos: " + str(pontos), True, WHITE)
            screen.blit(score_text, (10, screen_height - 50))

            timer_texto = fonte.render(f"Tempo:  {tempo}", True, WHITE)
            screen.blit(timer_texto, (250, screen_height - 50))

            pygame.display.flip()

    def modo_intermédiario():
            screen_width = 600
            screen_height = 600
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption("Jogo da Memória")

            card_width = 49
            card_height = 260
            card_padding = 10

            fonte = pygame.font.Font(None, 36)

            colors = [GREEN, RED, BLUE, YELLOW, ORANGE, OLIVA, PURPLE, PINK, GRAY, BROWN]

            cards = [color for color in colors for _ in range(2)]
            random.shuffle(cards)

            flipped = []

            matched = []

            game_over = False
            pontos = 100
            tempo = 600
            cont = 0

            while not game_over:
                cont = 0
                tempo -= 1
                cont += 1
                time.sleep(1)
                if cont == 30:
                    pontos -= 5
                    cont -= 30

                if pontos <= 0 or tempo <= 0:
                    tela_perdedor()
                    pygame.time.wait(3000)
                    game_over = True

                if len(matched) == 20:
                    tela_ganhador()
                    pygame.time.wait(3000)
                    game_over = True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        clicked_card = mouse_pos[0] // (card_width + card_padding), mouse_pos[1] // (
                                    card_height + card_padding)

                        if clicked_card not in flipped and clicked_card not in matched:
                            flipped.append(clicked_card)
                            pontos -= 2

                        if len(flipped) == 2:
                            card1, card2 = flipped
                            if cards[card1[1] * 10 + card1[0]] == cards[card2[1] * 10 + card2[0]]:
                                matched.extend(flipped)
                                pontos += 2
                            flipped = []

                screen.fill(BLACK)

                for i in range(10):
                    for j in range(2):
                        card_index = j * 6 + i
                        x = i * (card_width + card_padding) + card_padding
                        y = j * (card_height + card_padding) + card_padding

                        if (i, j) in flipped or (i, j) in matched:
                            pygame.draw.rect(screen, cards[card_index], (x, y, card_width, card_height))
                        else:
                            pygame.draw.rect(screen, WHITE, (x, y, card_width, card_height))

                pontos = 100
                score_texto = fonte.render(f"Pontos: {pontos}", True, WHITE)
                screen.blit(score_texto, (10, screen_height - 50))

                timer_texto = fonte.render(f"Tempo:  {tempo}", True, WHITE)
                screen.blit(timer_texto, (450, screen_height - 50))

                pygame.display.flip()

    def modo_dificil():
        screen_width = 1000
        screen_height = 700
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Jogo da Memória")

        card_width = 61
        card_height = 310
        card_padding = 10

        fonte = pygame.font.Font(None, 36)

        colors = [GREEN, RED, BLUE, YELLOW, ORANGE, CYAN, PURPLE, PINK, GRAY, BROWN, MAGENTA, BLACK, (128, 0, 0),
                  (0, 128, 0)]

        cards = [color for color in colors for _ in range(2)]
        random.shuffle(cards)

        flipped = []

        matched = []

        game_over = False
        pontos = 150
        tempo = 1200
        cont = 0

        while not game_over:
            cont = 0
            tempo -= 1
            cont += 1
            time.sleep(1)
            if cont == 30:
                pontos -= 5
                cont -= 30

            if pontos <= 0 or tempo <= 0:
                tela_perdedor()
                pygame.time.wait(3000)
                game_over = True

            if len(matched) == 28:
                tela_ganhador()
                pygame.time.wait(3000)
                game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_card = mouse_pos[0] // (card_width + card_padding), mouse_pos[1] // (
                                card_height + card_padding)

                    if clicked_card not in flipped and clicked_card not in matched:
                        flipped.append(clicked_card)
                        pontos -= 2

                    if len(flipped) == 2:
                        card1, card2 = flipped
                        if cards[card1[1] * 14 + card1[0]] == cards[card2[1] * 14 + card2[0]]:
                            matched.extend(flipped)
                            pontos += 2
                        flipped = []
            screen.fill(BLACK)

            for i in range(14):
                for j in range(2):
                    card_index = j * 14 + i
                    x = i * (card_width + card_padding) + card_padding
                    y = j * (card_height + card_padding) + card_padding

                    if (i, j) in flipped or (i, j) in matched:
                        pygame.draw.rect(screen, cards[card_index], (x, y, card_width, card_height))
                    else:
                        pygame.draw.rect(screen, WHITE, (x, y, card_width, card_height))

            pontos = 100
            score_texto = fonte.render(f"Pontos: {pontos}", True, WHITE)
            screen.blit(score_texto, (10, screen_height - 50))

            timer_texto = fonte.render(f"Tempo:  {tempo}", True, WHITE)
            screen.blit(timer_texto, (830, screen_height - 50))

            pygame.display.flip()

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
     
app.mainloop()