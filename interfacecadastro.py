import tkinter as tk
import customtkinter
from tkinter import *

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

    def botao_entrar():
      usuarioL = textbox.get("0.0", "end").strip()
      #strip esta servindo aqui para eliminar os possíveis espaços em branco que a string pode ter quando o usuário for colocar 
      with open("usuarios.txt", "r") as u: 
         for line in u:  
            listaU = line.strip().split('/n')
            #o split esta aqui para dividir os nomes em linhas 
            
            print(listaU)
            
            #Váriaveis User
            posicao = -1
            tam = len(listaU)

            if posicao <= tam:
              posicao = listaU.index(usuarioL)
            if usuarioL in listaU:
               print('Usuario: ', usuarioL)
               print('existe!')
               u.close()
               abrir_jogo()
               return
      print('Usuario: ', usuarioL)
      print('Não existe')
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
    text2 = textbox2.get("0.0", "end") 
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
    text3 = textbox3.get("0.0", "end") 
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
      senhal = textbox2.get("0.0", "end").strip()
      #strip esta servindo aqui para eliminar os possíveis espaços em branco que a string pode ter quando o usuário for colocar 

      with open("usuarios.txt", "r") as u: 
         
         for line in u:  
            listaS = line.strip().split('/n')
            #o split esta aqui para dividir os nomes em linhas 
            print(listaS)
            if senhal in listaS:  
               print('Senha: ', senhal)
               print('existe!')
               u.close()
               return
                  
      print('Senha: ', senhal)
      print('Não existe')
      u.close()

          
    #botao cadastrar
    button_cadastrar = customtkinter.CTkButton(cadastro_window, text= 'Cadastrar', command= botao_cadastrar)
    button_cadastrar.place(x=130, y= 190)

def abrir_jogo():
    # Criando uma nova janela com o Toplevel
    game_window = customtkinter.CTkToplevel()
    game_window.title("Tela jogo")
    game_window.geometry("400x240")


    
app.mainloop()
