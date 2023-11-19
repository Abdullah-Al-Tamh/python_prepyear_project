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
        # =========[frame]========#
        frame2 = Tk()
        frame2.geometry('1920x1080')
        frame2.config(background='#2D3B5E')
        frame_OPTI = tk.Frame(frame2)
        frame_OPTI.place(x=0, y=0)
        frame_OPTI.pack_propagate(False)
        frame_OPTI.configure(width=250, height=1080)

        # =========[FRUITS]========#
        def frame_FRUITS():
            fruit.pack()
            vegetable.pack_forget()
            bakery.pack_forget()
            drink.pack_forget()
            Button(frame2, text='Apple').pack()
            Button(frame2, text='Banana').pack()
            Button(frame2, text='Pineapple').pack()
            Button(frame2, text='Blueberry').pack()
            Button(frame2, text='Grape').pack()
            Button(frame2, text='Mango').pack()
            Button(frame2, text='raspberry').pack()
            Button(frame2, text='Strawberry').pack()
            Button(frame2, text='Orange').pack()
            Button(frame2, text='Coconut').pack()
            Button(frame2, text='Watermelon').pack()
            Button(frame2, text='Sweet-melon').pack()
            Button(frame2, text='Blackberry').pack()
            Button(frame2, text='Peach').pack()
            Button(frame2, text='Pear').pack()

        FRUITS_SECTION_butt = Button(frame_OPTI, text='FRUITS SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'), command=frame_FRUITS)
        FRUITS_SECTION_butt.place(x=20, y=50)

        # =========[VEGETABLES]========#
        def frame_VEGETABLES():
            frame3 = tk.Frame(frame2, highlightbackground='black', highlightthickness=3)
            frame3.pack(side=tk.RIGHT, expand=True)
            frame3.pack_propagate(False)
            frame3.config(width=1290, height=1080, bg='#8896AD')

            vegetable.pack()
            fruit.pack_forget()
            bakery.pack_forget()
            drink.pack_forget()

        VEGETABLES_SECTION_butt = Button(frame_OPTI, text='VEGETABLES SECTION', width=30, height=5,
                                         font=('Times New Roman', 10, 'bold'), command=frame_VEGETABLES)
        VEGETABLES_SECTION_butt.place(x=20, y=150)

        # =========[BAKERY]========#
        def frame_BAKERY():
            bakery.pack()
            fruit.pack_forget()
            vegetable.pack_forget()
            drink.pack_forget()

        BAKERY_SECTION_butt = Button(frame_OPTI, text='BAKERY SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'), command=frame_BAKERY)
        BAKERY_SECTION_butt.place(x=20, y=250)

        # =========[DRINKS]========#
        def frame_DRINKS():
            drink.pack()
            fruit.pack_forget()
            vegetable.pack_forget()
            bakery.pack_forget()

        DRINKS_SECTION_butt = Button(frame_OPTI, text='DRINKS SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'), command=frame_DRINKS)
        DRINKS_SECTION_butt.place(x=20, y=350)

        # =========[FRUITS]========#
        fruit = tk.Frame(frame2)
        fruit_label = tk.Label(fruit, text='This is fruit')
        fruit_label.pack(side='top')
        # =========[VEGETABLES]========#
        vegetable = tk.Frame(frame2)
        vegetable_label = tk.Label(vegetable, text='This is vegetable')
        vegetable_label.pack(side='top')
        # =========[BAKERY]========#
        bakery = tk.Frame(frame2)
        bakery_label = tk.Label(bakery, text='This is bakery')
        bakery_label.pack(side='top')
        # =========[DRINKS]========#
        drink = tk.Frame(frame2)
        drink_label = tk.Label(drink, text='This is drink')
        drink_label.pack(side='top')

        frame2.mainloop()


w = SuperMarket_Cm02(The_Window)
The_Window.mainloop()
