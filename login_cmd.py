from tkinter import *
import tkinter.ttk as ttk
import sqlite3

def login():
    with sqlite3.connect('login.db') as db:
        c = db.cursor()

    find_user = "SELECT * FROM users WHERE user = ? AND password = ?"

    c.execute(find_user[()])

    

root = Tk()
root.title('SQ System')

# IMAGENS
img_login = PhotoImage(file="img/login.png")
img_user = PhotoImage(file="img/user.png")
img_password = PhotoImage(file="img/password.png")

lb_logo = Label(root, image=img_login)
lb_logo.grid(row = 0, columnspan = 2)

lb_login = Label(root, image = img_user)
lb_login.grid(row = 1, column = 0)

lb_password = Label(root, image = img_password)
lb_password.grid(row = 2, column = 0)



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