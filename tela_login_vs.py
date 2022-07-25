from cProfile import label
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import Cursor, DatabaseError

#CRIANDO A JANELA
janela_principal = Tk()
janela_principal.title("LOGIN DE USUÁRIOS")
janela_principal.geometry("600x350")
janela_principal.resizable(False, False)
janela_principal.attributes("-alpha", 0.9)
janela_principal.configure(background="black")

#------------BASE DE DADOS---------------
#Criando base de dados ou conectando a uma base existente
conn = sqlite3.connect('base_usuarios.db')
#Criando uma instância do cursor
c = conn.cursor()
#Criando a tabela na base de dados
c.execute("""CREATE TABLE IF NOT EXISTS tab_usuarios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

def login_sistema():
    User = entrada_usuario.get()
    Pass = entrada_senha.get()

    c.execute("""
    SELECT* FROM tab_usuarios
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print('Selecionou')
    VerifyLogin = c.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="INFORMAÇÃO DE LOGIN", message="Acesso confirmado. Boas-vindas!")
    except:
        messagebox.showinfo(title="INFORMAÇÃO DE LOGIN", message="Acesso negado. Verifique se já possui cadastro no sistema.")

def registro_sistema():
    #Removendo botões
    btn_login.place(x=3000)
    btn_cadastro.place(x=3000)
    #inserindo botões
    btn_inserir_cadastro.place(x=210, y=200)
    btn_voltar.place(x=300, y=200)
    #Inserindo widgets para registro
    lbl_email.place(x=65, y=107)
    entrada_email.place(x=160, y=110)
    lbl_nome.place(x=72, y=148)
    entrada_nome.place(x=160, y=150)

def registro_banco_dados():
    Name = entrada_nome.get()
    Email = entrada_email.get()
    User = entrada_usuario.get()
    Pass = entrada_senha.get()
    if (Name == "" and Email == "" and User == "" and Pass == ""):
        messagebox.showerror(title="ERRO DE REGISTRO", message="Não deixe nenhum campo vazio, preencha todos os campos.")
    else:
        c.execute("""
        INSERT INTO tab_usuarios(Name, Email, User, Password) VALUES(?, ?, ?, ?)
        """, (Name, Email, User, Pass))
        conn.commit()
        messagebox.showinfo(title="INFORMAÇÃO DE REGISTRO", message="Conta criada com sucesso!")
    
def volta_login():
    #removendo botões e widgets de cadastro
    lbl_nome.place(x=3000)
    entrada_nome.place(x=3000)
    lbl_email.place(x=3000)
    entrada_email.place(x=3000)
    btn_voltar.place(x=3000)
    btn_inserir_cadastro.place(x=3000)
    #inserindo de volta os botões da tela login
    btn_login.place(x=210, y=200)
    btn_cadastro.place(x=300, y=200)
    #limpa entrada depois de cadastrar
    entrada_usuario.delete(0, END)
    entrada_senha.delete(0, END)

def encerra_programa():
    janela_principal.destroy()

#WIDGETS
lbl_usuario = Label(janela_principal, text='Usuário: ', font=("Elephant", 18), bg="black", fg="white")
lbl_usuario.place(x=50, y=25)
entrada_usuario = Entry(width=25, font=("Elephant", 15))
entrada_usuario.place(x=160, y=30)

lbl_senha = Label(janela_principal, text='Senha: ', font=("Elephant", 18), bg="black", fg="white")
lbl_senha.place(x=70, y=65)
entrada_senha = Entry(width=25, font=("Elephant", 15), show="*")
entrada_senha.place(x=160, y=70)

lbl_email = Label(janela_principal, text='E-mail: ', font=("Elephant", 18), bg="black", fg="white")
#place está na def registro
entrada_email = Entry(width=25, font=("Elephant", 15))
#place está na def registro

lbl_nome = Label(janela_principal, text='Nome: ', font=("Elephant", 18), bg="black", fg="white")
#place está na def registro
entrada_nome = Entry(width=25, font=("Elephant", 15))
#place está na def registro

#BOTÕES
btn_login = ttk.Button(text="LOGIN", command=login_sistema)
btn_login.place(x=210, y=200)
btn_cadastro = ttk.Button(text='CADASTRO', command=registro_sistema)
btn_cadastro.place(x=300, y=200)
btn_inserir_cadastro = ttk.Button(text="INSERIR", command=registro_banco_dados)
btn_voltar = ttk.Button(text="VOLTAR", command=volta_login)
btn_sair = ttk.Button(text="SAIR", command=encerra_programa)
btn_sair.place(x=260, y=250)

#ASSINATURA
lbl_assinatura = Label(janela_principal, text="Desenvolvido por Marco Moraes", font=("Elephant", 15), bg="black", fg="white")
lbl_assinatura.place(x=150, y=300)

janela_principal.mainloop()