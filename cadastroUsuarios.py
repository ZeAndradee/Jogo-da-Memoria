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

    # Label Titulo Login
    label = customtkinter.CTkLabel(login_window, text="Tela login", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.place(x=150, y=10)

    #label Apelido
    label = customtkinter.CTkLabel(login_window, text="Apelido", font=customtkinter.CTkFont(size=12, weight="normal"))
    label.place(x=80, y=50)

    #Criando TextBox Login
    textbox = customtkinter.CTkTextbox(login_window, width=250, height=30, border_color= '#3b8ed0', border_width=2)
    textbox.place(x= 75, y=75)
    textbox.insert("0.0", "new text to insert") 
    textbox.delete("0.0", "end") 
    textbox.configure(state="normal")



    #Label Senha

    labelsenha = customtkinter.CTkLabel(login_window, text="Senha", font=customtkinter.CTkFont(size=12, weight="normal"))
    labelsenha.place(x=80, y=120)

    #Criando TextBox Senha
    textbox2 = customtkinter.CTkTextbox(login_window, width=250, height=30, border_color= '#3b8ed0', border_width=2)
    textbox2.place(x= 75, y=145)
    textbox2.insert("0.0", "new text to insert")
     
    textbox2.delete("0.0", "end")
    textbox2.configure(state="normal") 

    def botao_entrar():
      usuarioL = textbox.get("0.0", "end").strip()
      usuarioS = textbox2.get("0.0", "end")
      #Verifica o input do login usuario
      with open("usuarios.txt", "r", encoding="utf-8") as u:   
        listaU = u.read().splitlines()
        print(listaU)
            
        #Váriaveis User
        posicaoL = -1
        tam = len(listaU)

      #Verifica o input do login usuario
        if posicaoL <= tam:
            posicaoL = listaU.index(usuarioL)
        if usuarioL in listaU:
            print('Usuario: ', usuarioL)
            print('existe!')
            u.close()
            return
      print('Usuario: ', usuarioL)
      print('Não existe')
      u.close()

      #Verifica o input senha
      with open("senhas.txt", "r", encoding="utf-8") as s:   
        listaS = s.read().splitlines()
        print(listaS)

        #Variaveis de verificação
        posicaoS = listaS.index(usuarioS)

        #Verifica se a senha está na lista
        if usuarioS in listaS:
            print('Senha: ', usuarioS)
            print('existe!')
            s.close()
            if posicaoS != posicaoL:
               print('A senha não pertence ao usuario digitado.')
            else:
               print(f'A senha pertence ao usuario {listaU[posicaoL]}')   
        
      print('Senha: ', usuarioS)
      print('Não existe')
      u.close()

    #Botão Fazer Login
    button_login = customtkinter.CTkButton(login_window, text='Fazer Login', command=botao_entrar)
    button_login.place(x=130, y= 190)   


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
      senhal = textbox2.get("0.0", "end").strip()

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
        u.close()
          
          
    #botao cadastrar
    button_cadastrar = customtkinter.CTkButton(cadastro_window, text= 'Cadastrar', command= botao_cadastrar)
    button_cadastrar.place(x=130, y= 190)

#Def resposável por abrir a tela do jogo
def abrir_jogo():
    # Criando uma nova janela com o Toplevel
    game_window = customtkinter.CTkToplevel()
    game_window.title("Tela jogo")
    game_window.geometry("400x240")
  
app.mainloop()
