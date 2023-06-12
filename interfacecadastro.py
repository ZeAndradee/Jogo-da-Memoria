import tkinter as tk
import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title('Cadastramento')


def switch_theme():
      if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
      else:
        customtkinter.set_appearance_mode("light")   

#tela de início
label = customtkinter.CTkLabel(app, text="Bem Vindo", font=customtkinter.CTkFont(size=20, weight="bold"))
label.place(x=150, y=30)

button = customtkinter.CTkButton(app, text='Fazer Login', command=lambda:abrir_tela_login())
button.place(x=130, y= 100)

button = customtkinter.CTkButton(app, text='Cadastre-se', command=lambda:abrir_cadastro())
button.place(x=130, y= 150)

switch_var = customtkinter.StringVar(value="off")
switch = customtkinter.CTkSwitch(app, text="Dark Mode", command=switch_theme,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.place(x= 260, y= 200)



def abrir_tela_login():
    # Criando uma nova janela com o Toplevel
    login_window = customtkinter.CTkToplevel()
    login_window.title("Tela de login")
    login_window.geometry("400x240")

    # Criando uma label com o custom tkinter
    label = customtkinter.CTkLabel(login_window, text="Escolha um usuário", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.place(x=110, y=30)
    #label apelido
    label = customtkinter.CTkLabel(login_window, text="Jogadores:", font=customtkinter.CTkFont(size=14, weight="normal"))
    label.place(x=120, y=90)

    optionmenu_var = customtkinter.StringVar(value="- Escolha uma opção -") # set initial value
    optionmenu = customtkinter.CTkOptionMenu(login_window,
    values=["Vinicius", 'Hiarita', 'Lucas', 'Victor', 'Caio'],
    command='',
    variable=optionmenu_var)
    optionmenu.place(x= 120, y=120)
    
def abrir_cadastro():
    #criando tela de cadastro
    cadastro_window = customtkinter.CTkToplevel()
    cadastro_window.title('Tela de Cadastro')
    cadastro_window.geometry("400x240")

    #criando label com nome 
    label3 = customtkinter.CTkLabel(cadastro_window, text= "Crie um usuário", font= customtkinter.CTkFont(size= 20, weight= "bold"))
    label3.place(x=120 ,y=30 )

    #label apelido
    label = customtkinter.CTkLabel(cadastro_window, text="Apelido", font=customtkinter.CTkFont(size=12, weight="normal"))
    label.place(x=80, y=95)

    #criando textbox apelido
    textbox3 = customtkinter.CTkTextbox(cadastro_window, width=250, height=30)
    textbox3.place(x= 75, y=120)
    textbox3.insert("0.0", "new text to insert") # insere na linha 0 caractere 0
    text3 = textbox3.get("0.0", "end") # obtém o texto da linha 0 caractere 0 até o final
    textbox3.delete("0.0", "end") # deleta todo o texto
    textbox3.configure(state="normal") # configura a caixa de texto para ser somente leitura

app.mainloop()
