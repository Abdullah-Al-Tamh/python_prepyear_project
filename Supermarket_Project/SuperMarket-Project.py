from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import math
import random

import self as self
import top as top

The_Window = Tk()


class SuperMarket_Cm02:
    def __init__(self, The_Window):
        self.The_Window = The_Window
        self.The_Window.geometry('1920x1080')
        self.The_Window.config(background='#2D3B5E')
        self.The_Window.title('IAU SUPERMARKET')
        Label(self.The_Window, text='IAU SUPERMARKET', fg='white', bg='#8896AD', font=('Times New Roman', 20)).pack(
            fill=X)

        def The_sign_in_window():
            sign = Toplevel(The_Window)
            sign.geometry('1920x1080')
            sign.config(background='#2D3B5E')
            Label(sign, text='Enter your Email:',
                  fg='white',
                  bg='#2D3B5E',
                  font=('Times New Roman',
                        15
                        , 'bold')).place(x=490, y=300)

            email_entre = Entry(sign,
                                justify='center',
                                font=15,
                                width=20)

            email_entre.place(x=650,
                              y=301)

            password_enter = Entry(sign,
                                   justify='center',
                                   font=15,
                                   width=20)

            Label(sign, text='Enter your password:',
                  fg='white',
                  bg='#2D3B5E',
                  font=('Times New Roman', 15, 'bold')).place(x=460, y=350)

            password_enter.place(x=650, y=350)
            Button(sign, text='Entering / دخول', width=31, height=2, bd=1, relief=GROOVE,
                   font=('Times New Roman', 10, 'bold')).place(x=650, y=390)

        button_sign = Button(The_Window, text="sign in / تسجيل الدخول",
                             width=30,
                             height=3,
                             font=('Times New Roman', 10, 'bold'),
                             cursor='hand2',
                             bd=1,
                             relief=GROOVE,
                             command=The_sign_in_window)

        button_sign.place(x=650, y=301)

        def The_GUEST_Window():
            guest = Toplevel()
            guest.geometry('1920x1080')
            fream = Label(guest)
            fream.pack()
            fream.config(background='#2D3B5E')

        button_guest = Button(The_Window, text="GUEST", width=30, height=3,
                              font=('Times New Roman', 10, 'bold'), command=The_GUEST_Window)
        button_guest.place(x=650, y=370)

        frame2 = Tk()
        frame2.geometry('1920x1080')
        frame2.config(background='#2D3B5E')
        frame_OPTI = tk.Frame(frame2)
        frame_OPTI.pack(side=tk.LEFT)
        frame_OPTI.pack_propagate(False)
        frame_OPTI.configure(width=250, height=1080)
        FRUITS_SECTION_butt = Button(frame_OPTI, text='FRUITS SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'))
        FRUITS_SECTION_butt.place(x=20, y=50)
        VEGETABLES_SECTION_butt = Button(frame_OPTI, text='VEGETABLES SECTION', width=30, height=5,
                                         font=('Times New Roman', 10, 'bold'))
        VEGETABLES_SECTION_butt.place(x=20, y=150)
        BAKERY_SECTION_butt = Button(frame_OPTI, text='BAKERY SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'))
        BAKERY_SECTION_butt.place(x=20, y=250)
        DRINKS_SECTION_butt = Button(frame_OPTI, text='DRINKS SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'))
        DRINKS_SECTION_butt.place(x=20, y=350)



        def fruites():
            fruites_Frame = tk.Frame(frame2)
            Label(fruites_Frame, text='hello').pack()



frame_FOR_frutis = Tk()
frame_FOR_frutis.geometry('1920x1080')
frame_FOR_frutis.config(background='#2D3B5E')
frame_FOR_frutis.title('WELCOME TO FRUITS SECTION')
Label(frame_FOR_frutis, text='WELCOME TO FRUITS SECTION', fg='black', bg='#8896AD',
      font=('Times New Roman', 20, 'bold')).pack(side='top', fill=X)

w = SuperMarket_Cm02(The_Window)
The_Window.mainloop()
frame_FOR_frutis.mainloop()
