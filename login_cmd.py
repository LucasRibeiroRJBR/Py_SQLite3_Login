from tkinter import *
import tkinter.ttk as ttk
import sqlite3
import pyglet
from ttkthemes import ThemedStyle

pyglet.font.add_file("font/HYWenHei.ttf")

def login():
    with sqlite3.connect('login.db') as db:
        c = db.cursor()

    find_user = ("SELECT * FROM users WHERE user = ? AND password = ?")

    c.execute(find_user, [(input_user, input_password)])

    resul = c.fetchall()
    
    if resul:
        for i in resul:
            resultado['text'] = f"Bem-vindo, {i[0]}!"
    else:
        resultado['text'] = f"Usuário ou senha inválidos!"

    

root = Tk()
root.title('SQ System')
root.geometry('300x350')
root.configure(background = '#202020')

style = ThemedStyle()
style.set_theme('clam')
style.configure("my.TLabel", font=('HYWenHei-85W', 24, 'bold'), bg = '#202020', borderwidth = 0)

# IMAGENS
img_login = PhotoImage(file="img/login.png")
img_user = PhotoImage(file="img/user.png")
img_password = PhotoImage(file="img/password.png")

lb_logo = ttk.Label(root, image=img_login, style = "my.TLabel")
lb_logo.grid(row = 0, columnspan = 2)

lb_login = ttk.Label(root, image = img_user, style = "my.TLabel")
lb_login.grid(row = 1, column = 0)

lb_password = ttk.Label(root, image = img_password, style = "my.TLabel")
lb_password.grid(row = 2, column = 0)

VarUser = StringVar()
VarPassword = StringVar()

input_user = ttk.Entry(root)
input_user.grid(row = 1, column = 1)

input_password = ttk.Entry(root, show = '*')
input_password.grid(row = 2, column = 1)

resultado = ttk.Label(root, text = '', style = "my.TLabel")
resultado.grid(row = 3, columnspan = 2)



root.mainloop()

'''def login():
    while True:
        username = input("Login: ")
        password = input("Senha: ")

        with sqlite3.connect('DB/login.db') as db:
            c = db.cursor()

        find_user = ("SELECT * FROM login WHERE usuario = ? AND senha = ?")
        c.execute(find_user, [(username), (password)])
        results = c.fetchall()

        if results:
            for i in results:
                print(f'Bem-vindo, {i[0]}')
            break
        else:
            print('Usuário ou senha estão incorretos.')
            again = input('Deseja continuar? [S/N]')
            if again.lower() == 'n':
                print('Tchau')
                time.sleep(2)

login()'''