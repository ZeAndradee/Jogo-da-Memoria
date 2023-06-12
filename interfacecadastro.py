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
    label = customtkinter.CTkLabel(login_window, text="Tela login", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.place(x=150, y=30)
    #label nome
    label = customtkinter.CTkLabel(login_window, text="Apelido", font=customtkinter.CTkFont(size=12, weight="normal"))
    label.place(x=80, y=75)
    #Criando TextBox
    textbox = customtkinter.CTkTextbox(login_window, width=250, height=30)
    textbox.place(x= 75, y=100)
    textbox.insert("0.0", "new text to insert") # insere na linha 0 caractere 0
    text = textbox.get("0.0", "end") # obtém o texto da linha 0 caractere 0 até o final
    textbox.delete("0.0", "end") # deleta todo o texto
    textbox.configure(state="normal") # configura a caixa de texto para ser somente leitura

    labelsenha = customtkinter.CTkLabel(login_window, text="Senha", font=customtkinter.CTkFont(size=12, weight="normal"))
    labelsenha.place(x=80, y=145)

    #Criando TextBox
    textbox2 = customtkinter.CTkTextbox(login_window, width=250, height=30)
    textbox2.place(x= 75, y=170)
    textbox2.insert("0.0", "new text to insert") # insere na linha 0 caractere 0
    text2 = textbox2.get("0.0", "end") # obtém o texto da linha 0 caractere 0 até o final
    textbox2.delete("0.0", "end") # deleta todo o texto
    textbox2.configure(state="normal") # configura a caixa de texto para ser somente leitura
    
def abrir_cadastro():
    cadastro_window = customtkinter.CTkToplevel()
    cadastro_window.title('Tela de Cadastro')
    cadastro_window.geometry("400x240")
    label3 = customtkinter.CTkLabel(cadastro_window, text= "Tela de Cadastro", font= customtkinter.CTkFont(size= 20, weight= "bold"))
    label3.place(x=135 ,y=30 )

#nome = tk.Label(login, 'digite seu nome')
#label2 = customtkinter.CTkLabel(login,text='Login', font=customtkinter.CTkFont(size= 20, weight='bold'))
#label2.place(x=150, y=30)
#label2 = tk.Label(login,text='nome')

app.mainloop()
