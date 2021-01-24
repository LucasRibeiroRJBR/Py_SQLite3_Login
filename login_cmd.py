from tkinter import *
import tkinter.ttk as ttk
import sqlite3
import pyglet
from ttkthemes import ThemedStyle

pyglet.font.add_file("font/HYWenHei.ttf")


def login():

    conn = sqlite3.connect('db/login.db')
    c = conn.cursor()

    c.execute(
        f'SELECT * FROM users WHERE user = "{VarUser.get()}" AND password = "{VarPassword.get()}"')

    resul = c.fetchall()

    if resul:
        for i in resul:
            resultado['text'] = f"Bem-vindo(a), {i[0]}!"
    else:
        resultado['text'] = f"Dados inválidos!"


root = Tk()
root.title('SQ System')
# root.geometry('200x350')
root.configure(background='#202020')
root.call('tk','windowingsystem')
root.overrideredirect

style = ThemedStyle()
style.set_theme('clam')
style.configure("my.TLabel", font=('HYWenHei-85W', 24, 'bold'),
                background='#202020', foreground='white', borderwidth=0)
style.configure("my.TButton", font=('HYWenHei-85W', 24, 'bold'), background='#202020', foreground='#202020', relief=GROOVE)
style.configure("my.TEntry", font=('HYWenHei-85W', 14, 'bold'), padding=5)

# IMAGENS
img_login = PhotoImage(file="img/login.png")
img_user = PhotoImage(file="img/user.png")
img_password = PhotoImage(file="img/password.png")
button = PhotoImage(file="img/button.png")

lb_logo = ttk.Label(root, image=img_login, style="my.TLabel")
lb_logo.grid(row=0, columnspan=2)

lb_login = ttk.Label(root, image=img_user, style="my.TLabel")
lb_login.grid(row=1, column=0)

lb_password = ttk.Label(root, image=img_password, style="my.TLabel")
lb_password.grid(row=2, column=0)

VarUser = StringVar()
VarPassword = StringVar()

input_user = ttk.Entry(root, font=(
    'HYWenHei-85W', 14, 'bold'), width=25, textvariable=VarUser)
input_user.grid(row=1, column=1, padx=15)

input_password = ttk.Entry(
    root, show='*', font=('HYWenHei-85W', 14, 'bold'), width=25, textvariable=VarPassword)
input_password.grid(row=2, column=1, padx=15)

bt_consultar = Button(root, text='Consultar', image = button, background='#202020', relief=FLAT, borderwidth=0, command=login)
bt_consultar.grid(row=3, columnspan=2)

resultado = ttk.Label(root, text='', style="my.TLabel")
resultado.grid(row=4, columnspan=2, pady=30)


root.mainloop()
