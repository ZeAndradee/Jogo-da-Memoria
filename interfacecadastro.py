import tkinter as tk
from tkinter import *
#criando a primeira janela
def abrir_janela():
    conclusaocadastro = tk.Toplevel()
    conclusaocadastro.title("janela nova")
janela = tk.Tk()
# permite a janela aparecer e o usuário manusear nela
janela.title("Cadastramento")
janela.geometry("250x100")

label = Label(janela, text="nome")
label.grid(row=0, column=0)
nome = Entry(janela, width= 10 )
nome.grid(row=0, column=1)

lista_dificuldade = ["fácil", "médio", "difícil"]
dificultade = StringVar(janela)
dificultade.set(lista_dificuldade[0])
#criando um option menu
label_dificuldade = Label(janela, text="dificuldade")
label_dificuldade.grid(row=1,column=0)
opnivel= OptionMenu(janela, dificultade ,*lista_dificuldade)
opnivel.grid( row=1, column= 1, columnspan = 2)

botao = tk.Button(janela, text= "enviar dados", command = abrir_janela )
botao.grid(row = 9, column = 10)
janela.mainloop()
