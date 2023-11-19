from tkinter import *
import tkinter as tk

# =========[frame]========#
frame2 = Tk()
frame2.geometry('1920x1080')
frame2.config(background='#2D3B5E')
frame_OPTI = tk.Frame(frame2)
frame_OPTI.place(x=0, y=0)
frame_OPTI.pack_propagate(False)
frame_OPTI.configure(width=250, height=1080)

#==========[destroy]=======#




# =========[FRUITS]========#
def frame_FRUITS():
    fruit.pack()
    vegetable.pack_forget()
    bakery.pack_forget()
    drink.pack_forget()
    Button(frame2, text='Apple').pack()
    Button(frame2, text='Orange').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()
    Button(frame2, text='hello').pack()


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
    frame4 = tk.Frame(frame2, highlightbackground='black', highlightthickness=3)
    frame4.pack(side=tk.RIGHT, expand=True)
    frame4.pack_propagate(False)
    frame4.config(width=1290, height=1080, bg='#8896AD')
    bakery.pack()
    fruit.pack_forget()
    vegetable.destroy()
    drink.destroy()


BAKERY_SECTION_butt = Button(frame_OPTI, text='BAKERY SECTION', width=30, height=5,
                             font=('Times New Roman', 10, 'bold'), command=frame_BAKERY)
BAKERY_SECTION_butt.place(x=20, y=250)


# =========[DRINKS]========#
def frame_DRINKS():
    frame5 = tk.Frame(frame2, highlightbackground='black', highlightthickness=3)
    frame5.pack(side=tk.RIGHT, expand=False)
    frame5.pack_propagate(False)
    frame5.config(width=1290, height=1080, bg='#8896AD')
    drink.pack()
    fruit.pack_forget()
    vegetable.pack_forget()
    bakery.pack_forget()
    fruit.destroy()
    vegetable.destroy()
    bakery.destroy()



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
