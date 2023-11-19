def hide_all_without_drink():
    frame_vegetable.pack_forget()
    frame_fruite.pack_forget()
    frame_bakery.pack_forget()


def hide_all_without_fruite():
    frame_drink.pack_forget()
    frame_vegetable.pack_forget()
    frame_bakery.pack_forget()


def hide_all_without_bakery():
    frame_drink.pack_forget()
    frame_fruite.pack_forget()
    frame_vegetable.pack_forget()


def hide_all_without_vegetable():
    frame_drink.pack_forget()
    frame_fruite.pack_forget()
    frame_bakery.pack_forget()

    def frame_OF_fruite():
        frame_fruite = tk.Frame(self, highlightbackground='black', highlightthickness=3)
        frame_fruite.config(background='red')
        frame_fruite.configure(width=1290, height=1080)
        Label(frame_fruite, text='hhh').pack()
        frame_fruite.place(x=1410, y=1080)
        return frame_fruite

    # [frame for VEGETABLES section]:

    def frame_OF_vegetable():
        frame_vegetable = tk.Frame(self, highlightbackground='black', highlightthickness=3)
        frame_vegetable.config(background='green')
        frame_vegetable.configure(width=1350, height=1080)
        frame_vegetable.place(x=500, y=1080)
        return frame_vegetable

    # [frame for BAKERY section]:

    def frame_OF_bakery():
        frame_bakery = tk.Frame(self, highlightbackground='black', highlightthickness=3)
        frame_bakery.config(background='blue')
        frame_bakery.configure(width=1290, height=1080)
        frame_bakery.pack(side=BOTTOM)
        return frame_bakery

    # [frame for DRINKS section]:

    def frame_OF_drink():
        frame_drink = tk.Frame(self, highlightbackground='black', highlightthickness=3)
        frame_drink.config(background='black')
        frame_drink.configure(width=1190, height=1080)
        frame_drink.pack(side=BOTTOM)
        return frame_drink