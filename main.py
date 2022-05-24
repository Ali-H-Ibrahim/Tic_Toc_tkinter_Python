# # This is a sample Python script.
#
import states as ss

# import cars as c
# import cells as s
import LogicGameCar as g
#
# #------------------------------ initalizing -------------------------------------#
n = 5
m = 5
a = [['-'] * m for i in range(n)]
#
#
#
bs=ss.States(a,None,0,0,None)
bs.print_gride()

# Tic Tac Toe game with GUI
# using tkinter

# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# sign variable to decide the turn of which player
sign = 0

count = 0
click = True

root = Tk()
root.iconbitmap('tic toc.ico')
root.title('tic toc')
# منشان المستخدم لا يكبر ويصغر حجم الرقعة
root.resizable(False, False)

# سطر 1
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
# سطر 2
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()
btn10 = StringVar()
# سطر 3
btn11 = StringVar()
btn12 = StringVar()
btn13 = StringVar()
btn14 = StringVar()
btn15 = StringVar()
# سطر 4
btn16 = StringVar()
btn17 = StringVar()
btn18 = StringVar()
btn19 = StringVar()
btn20 = StringVar()
# سطر 5
btn21 = StringVar()
btn22 = StringVar()
btn23 = StringVar()
btn24 = StringVar()

btn25 = StringVar()

xPotho = PhotoImage(file='x.png')
oPotho = PhotoImage(file='oo.png')
gg= g.Game(bs)
print(gg.eval_f(bs))
gg.alfa_beta(bs)



def play():

    # سطر 1

    Button1 = Button(root, height=9, width=19, bd=5, command=lambda: press(1, 0, 0), textvariable=btn1, bg='#e5ffe6',
                     relief='ridge')

    Button1.grid(row=0, column=0)
    Button2 = Button(root, bd=5, command=lambda: press(2, 0, 1), textvariable=btn2, height=9, width=19, bg='#e5ffe6',
                     relief='ridge')
    Button2.grid(row=0, column=1)
    Button3 = Button(
        root, bd=5, command=lambda: press(3, 0, 2), textvariable=btn3, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button3.grid(row=0, column=2)
    Button4 = Button(
        root, bd=5, command=lambda: press(4, 0, 3), textvariable=btn4, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button4.grid(row=0, column=3)
    Button5 = Button(
        root, bd=5, command=lambda: press(5, 0, 4), textvariable=btn5, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button5.grid(row=0, column=4)

    # سطر 2

    Button6 = Button(
        root, bd=5, command=lambda: press(6, 1, 0), textvariable=btn6, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button6.grid(row=1, column=0)
    Button7 = Button(
        root, bd=5, command=lambda: press(7, 1, 1), textvariable=btn7, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button7.grid(row=1, column=1)

    Button8 = Button(
        root, bd=5, command=lambda: press(8, 1, 2), textvariable=btn8, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button8.grid(row=1, column=2)

    Button9 = Button(
        root, bd=5, command=lambda: press(9, 1, 3), textvariable=btn9, height=9, width=19, bg='#e5ffe6', relief='ridge')
    Button9.grid(row=1, column=3)

    Button10 = Button(
        root, bd=5, command=lambda: press(10, 1, 4), textvariable=btn10, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button10.grid(row=1, column=4)

    # سطر 3

    Button11 = Button(
        root, bd=5, command=lambda: press(11, 2, 0), textvariable=btn11, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button11.grid(row=2, column=0)

    Button12 = Button(
        root, bd=5, command=lambda: press(12, 2, 1), textvariable=btn12, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button12.grid(row=2, column=1)

    Button13 = Button(
        root, bd=5, command=lambda: press(13, 2, 2), textvariable=btn13, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button13.grid(row=2, column=2)

    Button14 = Button(
        root, bd=5, command=lambda: press(14, 2, 3), textvariable=btn14, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button14.grid(row=2, column=3)

    Button15 = Button(
        root, bd=5, command=lambda: press(15, 2, 4), textvariable=btn15, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button15.grid(row=2, column=4)

    # سطر 4

    Button16 = Button(
        root, bd=5, command=lambda: press(16, 3, 0), textvariable=btn16, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button16.grid(row=3, column=0)

    Button17 = Button(
        root, bd=5, command=lambda: press(17, 3, 1), textvariable=btn17, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button17.grid(row=3, column=1)

    Button18 = Button(
        root, bd=5, command=lambda: press(18, 3, 2), textvariable=btn18, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button18.grid(row=3, column=2)

    Button19 = Button(
        root, bd=5, command=lambda: press(19, 3, 3), textvariable=btn19, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button19.grid(row=3, column=3)

    Button20 = Button(
        root, bd=5, command=lambda: press(20, 3, 4), textvariable=btn20, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button20.grid(row=3, column=4)

    # سطر 5

    Button21 = Button(
        root, bd=5, command=lambda: press(21, 4, 0), textvariable=btn21, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button21.grid(row=4, column=0)
    Button22 = Button(
        root, bd=5, command=lambda: press(22, 4, 1), textvariable=btn22, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button22.grid(row=4, column=1)

    Button23 = Button(
        root, bd=5, command=lambda: press(23, 4, 2), textvariable=btn23, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button23.grid(row=4, column=2)

    Button24 = Button(
        root, bd=5, command=lambda: press(24, 4, 3), textvariable=btn24, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button24.grid(row=4, column=3)

    Button25 = Button(
        root, bd=5, command=lambda: press(25, 4, 4), textvariable=btn25, height=9, width=19, bg='#e5ffe6',
        relief='ridge')
    Button25.grid(row=4, column=4)

    pass



def press(num, r, c):
    global click,count,a

    if click:
        labelPhoto=Label(root,image=xPotho)
        labelPhoto.grid(row=r, column=c)
        click=False
        print("x")
        a[r][c] ='X'
        bs.print_gride()

    else:
        labelPhoto = Label(root, image=oPotho)
        labelPhoto.grid(row=r, column=c)
        click = True
        print("o")
        a[r][c] ='O'
        bs.print_gride()
        pc()
    if bs.is_woin('X'):
        print("X is won")
        g.sys.exit()

        # root.destroy()
    if bs.is_woin('O'):
        print("O is won")

        g.sys.exit()

        # root.destroy()



def pc():
    global click, count,a
    if click:
        bs = ss.States(a, None, 0, 0, None)
        gg = g.Game(bs)
        bs.gool()
        gg.alfa_beta(bs)
        b = gg.p()
        press('X', b.new[0], b.new[1])
        click = False
        print('ssssssss')


play()


pc()



root.mainloop()
