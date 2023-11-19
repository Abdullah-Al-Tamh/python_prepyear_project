from tkinter import *
import tkinter as tk

# =============[The_Window]========#

The_Window = Tk()
The_Window.geometry('1920x1080')
The_Window.config(background='#2D3B5E')
The_Window.title('IAU SUPERMARKET')
Label(The_Window, text='IAU SUPERMARKET', fg='white', bg='#8896AD', font=('Times New Roman', 20)).pack(fill=X)
Label(The_Window, text='Enter your Email:', fg='white', bg='#2D3B5E', font=('Times New Roman', 15, 'bold')).place(x=490,
                                                                                                                  y=300)

# =============[email_entre]========#

email_entre = Entry(The_Window, justify='center', font=15, width=20)
email_entre.place(x=650, y=301)

# =============[password_enter]========#

password_enter = Entry(The_Window, justify='center', font=15, width=20)
Label(The_Window, text='Enter your password:', fg='white', bg='#2D3B5E', font=('Times New Roman', 15, 'bold')).place(
    x=460, y=350)
password_enter.place(x=650, y=350)

# =============[Button(GUEST),(دخول)]========#

Entering_btn = Button(The_Window, text='Entering / دخول', width=31, height=2, bd=1, relief=GROOVE,
                      font=('Times New Roman', 10, 'bold'))
Entering_btn.place(x=650, y=390)
GUEST_btn = Button(The_Window, text="GUEST", width=30, height=3, font=('Times New Roman', 10, 'bold'),
                   command=lambda: frame_OPTI.tkraise())
GUEST_btn.place(x=650, y=450)

# =============[frame 2]========#

frame_OPTI = Toplevel()
frame_OPTI.geometry('1920x1080')
frame_OPTI.config(background='red')
frame_OPTI.configure(width=250, height=1080)


# =============[hide frames]========#

def frames_CH_end():
    for CH_fruite_frames in frame_OF_fruite().winfo_children():
        CH_fruite_frames.destroy()
    for CH_vegetable_frames in frame_OF_vegetable().winfo_children():
        CH_vegetable_frames.destroy()
    for CH_bakery_frames in frame_OF_bakery().winfo_children():
        CH_bakery_frames.destroy()
    for CH_drink_frames in frame_OF_drink().winfo_children():
        CH_drink_frames.destroy()


def For_fruite(frames1):
    for another_frame in frames1:
        another_frame.pack_forget()


def For_vegetable(frames2):
    for another_frame in frames2:
        another_frame.pack_forget()


def For_bakery(frames3):
    for another_frame in frames3:
        another_frame.pack_forget()


def For_drink(frames4):
    for another_frame in frames4:
        another_frame.pack_forget()


def all_things_for_F():
    frames_CH_end()
    For_fruite([frame_OF_vegetable(), frame_OF_drink(), frame_OF_bakery()])


def all_things_for_V():
    frames_CH_end()
    For_vegetable([frame_OF_bakery(), frame_OF_fruite(), frame_OF_drink()])


def all_things_for_B():
    frames_CH_end()
    For_bakery([frame_OF_vegetable(), frame_OF_fruite(), frame_OF_drink()])


def all_things_for_D():
    frames_CH_end()
    For_drink([frame_OF_vegetable(), frame_OF_bakery(), frame_OF_fruite()])


# =============[frame for each section]========#
buttons_frame = tk.Frame(frame_OPTI)
buttons_frame.config(background='black')
buttons_frame.configure(width=260, height=1080)
buttons_frame.pack(side=LEFT)


# =============[All frames]========#


# [frame for FRUITS section]:


def frame_OF_fruite():
    frame_fruite = tk.Frame(frame_OPTI, highlightbackground='black', highlightthickness=3)
    frame_fruite.config(background='red')
    frame_fruite.configure(width=1290, height=1080)
    Label(frame_fruite, text='hhh').pack()
    frame_fruite.place(x=1410, y=1080)
    Button(frame_fruite, text='Apple').pack()
    Button(frame_fruite, text='Orange').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    Button(frame_fruite, text='hello').pack()
    return frame_fruite


# [frame for VEGETABLES section]:

def frame_OF_vegetable():
    frame_vegetable = tk.Frame(frame_OPTI, highlightbackground='black', highlightthickness=3)
    frame_vegetable.config(background='green')
    frame_vegetable.configure(width=1350, height=1080)
    frame_vegetable.place(x=500, y=1080)
    return frame_vegetable


# [frame for BAKERY section]:

def frame_OF_bakery():
    frame_bakery = tk.Frame(frame_OPTI, highlightbackground='black', highlightthickness=3)
    frame_bakery.config(background='blue')
    frame_bakery.configure(width=1290, height=1080)
    frame_bakery.pack(side=BOTTOM)
    return frame_bakery


# [frame for DRINKS section]:

def frame_OF_drink():
    frame_drink = tk.Frame(frame_OPTI, highlightbackground='black', highlightthickness=3)
    frame_drink.config(background='black')
    frame_drink.configure(width=1190, height=1080)
    frame_drink.pack(side=BOTTOM)
    return frame_drink


# =============[Button for each section]========#
# [FRUITS_SECTION_butt]:

FRUITS_SECTION_butt = Button(buttons_frame, text='FRUITS SECTION', width=30, height=5,
                             font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                             command=lambda: all_things_for_F())
FRUITS_SECTION_butt.place(x=20, y=50)

# [VEGETABLES_SECTION_butt]:

VEGETABLES_SECTION_butt = Button(buttons_frame, text='VEGETABLES SECTION', width=30, height=5,
                                 font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                                 command=lambda: all_things_for_V())
VEGETABLES_SECTION_butt.place(x=20, y=150)

# [BAKERY_SECTION_butt]:

BAKERY_SECTION_butt = Button(buttons_frame, text='BAKERY SECTION', width=30, height=5,
                             font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                             command=lambda: all_things_for_B())
BAKERY_SECTION_butt.place(x=20, y=250)

# [DRINKS_SECTION_butt]:


DRINKS_SECTION_butt = Button(buttons_frame, text='DRINKS SECTION', width=30, height=5,
                             font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                             command=lambda: all_things_for_D())
DRINKS_SECTION_butt.place(x=20, y=350)

# [EXIT_Button]:

EXIT_Button = Button(buttons_frame, text='EXIT', width=7, height=3, font=('Times New Roman', 10, 'bold'), bd=1,
                     relief=GROOVE,
                     command=lambda: frame_OPTI.quit())
EXIT_Button.place(x=20, y=720)

# =============[Back Button]========#
back_btn = Button(buttons_frame, text='BACK', width=7, height=3, font=('Times New Roman', 9, 'bold'), bd=1,
                  relief=GROOVE, command=lambda: The_Window.tkraise())
back_btn.place(x=190, y=720)

# [Delete Frame Children Widgets ]:


# [mainloop]:

The_Window.mainloop()

