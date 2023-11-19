from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import bcrypt
import datetime


# [THE_LOCAL_PAGE]:
class Local_page(tk.Frame):
    def __init__(self, Frame1, The_controller_pages):
        tk.Frame.__init__(self, Frame1)
        self.The_controller_pages = The_controller_pages

        self.config(background='#2D3B5E')
        Label(self, text='IAU SUPERMARKET', fg='white', bg='#8896AD', font=('Times New Roman', 20)).pack(fill=X)
        # =============[email_entre]========#
        global user_entre
        user_entre = Entry(self, justify='center', font=15, width=20)
        Label(self, text='Enter your username:', fg='white', bg='#2D3B5E', font=('Times New Roman', 15, 'bold')).place(
            x=460, y=301)
        user_entre.place(x=650, y=301)

        # =============[password_enter]========#
        global password_enter
        password_enter = Entry(self, justify='center', font=15, width=20, show='*')
        Label(self, text='Enter your password:', fg='white', bg='#2D3B5E',
              font=('Times New Roman', 15, 'bold')).place(x=460, y=350)
        password_enter.place(x=650, y=350)

        # =============[Button(GUEST),(LOGIN)]========#

        Entering_btn = Button(self, text='LOGIN', width=31, height=2,
                              font=('Times New Roman', 10, 'bold'),
                              command=lambda: login())
        Entering_btn.place(x=650, y=390)

        GUEST_btn = Button(master=self, text="GUEST", width=31,
                           height=2, font=('Times New Roman', 10, 'bold'),
                           command=lambda: The_controller_pages.get_page('Secondry_page'))
        GUEST_btn.place(x=650, y=450)

        # =============[Button(SIGNUP)]========#

        signup_btn = Button(self, text='SIGN-UP', width=8, command=lambda: The_controller_pages.get_page('forth_Page'))
        Label(self, text="You don't have an account?", fg='white', bg='#2D3B5E',
              font=('Times New Roman', 12, 'bold')).place(x=600, y=505)
        signup_btn.place(x=790, y=505)

        # =============[Function for LOGIN]========#

        def login():
            username = user_entre.get()
            passowrd = password_enter.get()
            if username != '' and passowrd != '':
                cursor.execute('SELECT password FROM users WHERE username=?', [username])
                resulte = cursor.fetchone()
                if resulte:
                    if bcrypt.checkpw(passowrd.encode('utf-8'), resulte[0]):
                        messagebox.showinfo('Success', 'Logged in successfully.')
                        self.pack_forget()
                        The_controller_pages.get_page('Secondry_page').pack()
                    else:
                        messagebox.showerror('Error', 'Invalid password')
                else:
                    messagebox.showerror('Error', 'Enter all data')
            else:
                messagebox.showerror('Error', 'Enter all data')

        Developers_prog = ("مشعل العتيبي", 'عبدالله الطعمة', "محمد الخليفة", "سعودالموسى", "عبدالله الدار")


# [THE_SECOND_PAGE]:##########################################


class Secondry_page(tk.Frame):
    def __init__(self, Frame1, The_controller_pages):
        tk.Frame.__init__(self, Frame1)
        self.The_controller_pages = The_controller_pages
        Label(self, text='IAU SUPERMARKET', fg='#5C6882', bg='#5C6882', font=('Times New Roman', 20)).pack(fill=X)

        All_products = {
            0: ["APPLE", 5],
            1: ["PINEAPPLE", 7],
            2: ["BANANA", 3],
            3: ["BLUEBERRY", 9],
            4: ["GRAPE", 7],
            5: ["MANGO", 1],
            6: ["RASPBERRY", 2],
            7: ["STRAWBERRY", 3],
            8: ["ORANGE", 7],
            9: ["COCONUT", 5],
            10: ["WATERMELON", 3],
            11: ["SWEET-MELON", 3],
            12: ["BLACKBERRY", 4],
            13: ["PEACH", 6],
            14: ["PEAR", 9],
            15: ["CUCUMBER", 5],
            16: ["POTATO", 8],
            17: ["CORN", 5],
            18: ["ONION", 7],
            19: ["PEA", 3],
            20: ["PUMPKIN", 2],
            21: ["TOMATO", 3],
            22: ["MUSHROOM", 3],
            23: ["CARROT", 7],
            24: ["BROCCOLI", 8],
            25: ["BEET", 4],
            26: ["CHILLI", 3],
            27: ["OLIVES", 4],
            28: ["PARSLEY", 5],
            29: ["LETTUCE", 3],
            30: ["WHITE BREAD", 5],
            31: ["BROWN BREAD", 8],
            32: ["BURGER BREAD", 3],
            33: ["WHITE TOAST", 5],
            34: ["TORTILLA", 4],
            35: ["BAGEL", 3],
            36: ["CUPCAKE", 5],
            37: ["CAKE", 3],
            38: ["CROISSANT", 4],
            39: ["PANCAKE", 7],
            40: ["WAFFLE", 5],
            41: ["PRETZEL", 2],
            42: ["DONUTS", 9],
            43: ["COOKIES", 9],
            44: ["BAGUETTE", 7],
            45: ["WATER", 1],
            46: ["MILK", 5],
            47: ["OAT MILK", 3],
            48: ["COCA COLA", 4],
            49: ["SOY MILK", 4],
            50: ["APPLE JUICE", 5],
            51: ["PEPSI", 9],
            52: ["REDBULL", 9],
            53: ["CODE-RED", 5],
            54: ["ORANGE JUICE", 5],
            55: ["LEMONADE", 5],
            56: ["DIET PEPSI", 5],
            57: ["PEPSI MAX", 5],
            58: ["TEA", 5],
            59: ["ICE TEA", 5],
        }

        def Check_out_finall():
            All_total = 0
            for add_All in self.Check_out.get_children():
                self.Check_out.delete(add_All)
            for chaker in range(len(list_for_ALL)):
                if int(list_for_ALL[chaker].get()) > 0:
                    All_salary = int(list_for_ALL[chaker].get()) * All_products[chaker][1]
                    All_total += All_salary
                    name = (str(All_products[chaker][1]), str(list_for_ALL[chaker].get()), str(All_salary))
                    self.Check_out.insert('', 'end', iid=str(chaker), text=str(All_products[chaker][0]), values=name)
            Total_for_products = All_total
            Put_The_Total.insert('1', str(Total_for_products) + ' SR')
            Put_The_Date.insert('1', str(datetime.datetime.now().strftime('%Y-%m-%d')))

        # [Frame_Hold_Btn]:
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.config(background='#5C6882')
        self.buttons_frame.configure(width=260, height=1080)
        self.buttons_frame.pack(side=LEFT)

        # [Frame_for_order]:

        # [Button_for_order]:

        # [Frame_Hold_content]:
        self.info_OF_frame = tk.Frame(self, bg='#8896AD', width=400, highlightbackground='black', highlightthickness=4)
        self.info_OF_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.Frame_of_Check_out = tk.Frame(self, highlightbackground='black', width=500, highlightthickness=4)
        self.Frame_of_Check_out.pack(side=RIGHT, fill=BOTH, expand=True)

        # self.frame_for_order = tk.Frame(self, background='black')
        # self.frame_for_order.config(width=800, height=100)
        # self.frame_for_order.place(x=200, y=600)
        # ==============[Frame_Hold_content]==============:

        self.Check_out = ttk.Treeview(self.Frame_of_Check_out, selectmode='browse')
        self.Check_out.place(x=20, y=10, width=450, height=800)

        self.Check_out['columns'] = ('1', '2', '3')
        self.Check_out.column('0', width=7, anchor='c')
        self.Check_out.column('1', width=7, anchor='c')
        self.Check_out.column('2', width=5, anchor='c')
        self.Check_out.column('3', width=5, anchor='c')
        self.Check_out.heading('#0', text='Product', anchor='c')
        self.Check_out.heading('#1', text='Price', anchor='c')
        self.Check_out.heading('#2', text='Quantity', anchor='c')
        self.Check_out.heading('#3', text='Total', anchor='c')

        # ============[Button for order]========

        # [ALL_PRODUCTS_SECTION_btn]:
        All_products_SECTION_btn = Button(self.buttons_frame, text='VIEW ALL PRODUCTS', width=30, height=5,
                                          font=('Times New Roman', 10, 'bold'), bd=2, relief=GROOVE,
                                          command=lambda: self.Pack_ALL_SECTION(self.info_OF_frame))
        All_products_SECTION_btn.place(x=20, y=50)

        # [INFO_CHEAK_btn]:

        add_btn = Button(self.buttons_frame, text='ADD TO CART', width=20, height=5,
                         font=('Times New Roman', 10, 'bold'), bd=5, relief=GROOVE,
                         command=Check_out_finall)
        add_btn.place(x=60, y=350)

        # [Bill_btn]:
        bill = Button(self.buttons_frame, text='CHECK OUT', width=20, height=5, font=('Times New Roman', 10, 'bold'),
                      bd=5, relief=GROOVE,
                      command=lambda: The_controller_pages.get_page('Third_Page'))
        bill.place(x=60, y=580)

        # [EXIT_btn]:
        EXIT_Button = Button(self.buttons_frame, text='EXIT', width=7, height=3, font=('Times New Roman', 10, 'bold'),
                             bd=2,
                             relief=RIDGE, command=self.quit)
        EXIT_Button.place(x=30, y=720)

        # [back_btn]:
        back_btn = Button(self.buttons_frame, text='BACK', width=7, height=3, font=('Times New Roman', 9, 'bold'), bd=2,
                          relief=RIDGE, command=lambda: The_controller_pages.get_page('Local_page'))
        back_btn.place(x=190, y=720)

    def Pack_ALL_SECTION(self, info_OF_frame):
        for The_ALL_Widget in info_OF_frame.winfo_children():
            The_ALL_Widget.destroy()

        global list_for_ALL
        list_for_ALL = []

        Label(info_OF_frame, text='Fruit Section', font=('Times New Roman', 16)).grid(row=2, column=2)
        Label(info_OF_frame, text='APPLE', width=12, height=3, borderwidth=2, relief='groove').grid(row=5, column=2)
        Label(info_OF_frame, text='PINEAPPLE', width=12, height=3, borderwidth=2, relief='groove').grid(row=9, column=2)
        Label(info_OF_frame, text='BANANA', width=12, height=3, borderwidth=2, relief='groove').grid(row=12, column=2)
        Label(info_OF_frame, text='BLUEBERRY', width=12, height=3, borderwidth=2, relief='groove').grid(row=15,
                                                                                                        column=2)
        Label(info_OF_frame, text='GRAPE', width=12, height=3, borderwidth=2, relief='groove').grid(row=18, column=2)
        Label(info_OF_frame, text='MANGO', width=12, height=3, borderwidth=2, relief='groove').grid(row=21, column=2)
        Label(info_OF_frame, text='RASPBERRY', width=12, height=3, borderwidth=2, relief='groove').grid(row=24,
                                                                                                        column=2)
        Label(info_OF_frame, text='STRAWBERRY', width=12, height=3, borderwidth=2, relief='groove').grid(row=27,
                                                                                                         column=2)
        Label(info_OF_frame, text='ORANGE', width=12, height=3, borderwidth=2, relief='groove').grid(row=30, column=2)
        Label(info_OF_frame, text='COCONUT', width=12, height=3, borderwidth=2, relief='groove').grid(row=33, column=2)
        Label(info_OF_frame, text='WATERMELON', width=12, height=3, borderwidth=2, relief='groove').grid(row=36,
                                                                                                         column=2)
        Label(info_OF_frame, text='SWEET_MELON', width=12, height=3, borderwidth=2, relief='groove').grid(row=39,
                                                                                                          column=2)
        Label(info_OF_frame, text='BLACKBERRY', width=12, height=3, borderwidth=2, relief='groove').grid(row=42,
                                                                                                         column=2)
        Label(info_OF_frame, text='PEACH', width=12, height=3, borderwidth=2, relief='groove').grid(row=45, column=2)

        Label(info_OF_frame, text='Veg Section', font=('Times New Roman', 16)).grid(row=2, column=14)
        Label(info_OF_frame, text='CUCUMBER', width=12, height=3, borderwidth=2, relief='groove').grid(row=5, column=14)
        Label(info_OF_frame, text='POTATO', width=12, height=3, borderwidth=2, relief='groove').grid(row=9, column=14)
        Label(info_OF_frame, text='CORN', width=12, height=3, borderwidth=2, relief='groove').grid(row=12, column=14)
        Label(info_OF_frame, text='ONION', width=12, height=3, borderwidth=2, relief='groove').grid(row=15, column=14)
        Label(info_OF_frame, text='PEA', width=12, height=3, borderwidth=2, relief='groove').grid(row=18, column=14)
        Label(info_OF_frame, text='PUMPKIN', width=12, height=3, borderwidth=2, relief='groove').grid(row=21, column=14)
        Label(info_OF_frame, text='TOMATO', width=12, height=3, borderwidth=2, relief='groove').grid(row=24, column=14)
        Label(info_OF_frame, text='MUSHROOM', width=12, height=3, borderwidth=2, relief='groove').grid(row=27,
                                                                                                       column=14)
        Label(info_OF_frame, text='CARROT', width=12, height=3, borderwidth=2, relief='groove').grid(row=30, column=14)
        Label(info_OF_frame, text='BROCCOLI', width=12, height=3, borderwidth=2, relief='groove').grid(row=33,
                                                                                                       column=14)
        Label(info_OF_frame, text='BEET', width=12, height=3, borderwidth=2, relief='groove').grid(row=36, column=14)
        Label(info_OF_frame, text='CHILLI', width=12, height=3, borderwidth=2, relief='groove').grid(row=39, column=14)
        Label(info_OF_frame, text='OLIVES', width=12, height=3, borderwidth=2, relief='groove').grid(row=42, column=14)
        Label(info_OF_frame, text='PARSLEY', width=12, height=3, borderwidth=2, relief='groove').grid(row=45, column=14)

        Label(info_OF_frame, text='Bakery Section', font=('Times New Roman', 16)).grid(row=2, column=24)
        Label(info_OF_frame, text='WHITEBREAD', width=12, height=3, borderwidth=2, relief='groove').grid(row=5,
                                                                                                         column=24)
        Label(info_OF_frame, text='BROWNBREAD', width=12, height=3, borderwidth=2, relief='groove').grid(row=9,
                                                                                                         column=24)
        Label(info_OF_frame, text='BURGERBREAD', width=12, height=3, borderwidth=2, relief='groove').grid(row=12,
                                                                                                          column=24)
        Label(info_OF_frame, text='WHITETOAST', width=12, height=3, borderwidth=2, relief='groove').grid(row=15,
                                                                                                         column=24)
        Label(info_OF_frame, text='TORTILLA', width=12, height=3, borderwidth=2, relief='groove').grid(row=18,
                                                                                                       column=24)
        Label(info_OF_frame, text='BAGEL', width=12, height=3, borderwidth=2, relief='groove').grid(row=21, column=24)
        Label(info_OF_frame, text='CUPCAKE', width=12, height=3, borderwidth=2, relief='groove').grid(row=24, column=24)
        Label(info_OF_frame, text='CAKE', width=12, height=3, borderwidth=2, relief='groove').grid(row=27, column=24)
        Label(info_OF_frame, text='CROISSANT', width=12, height=3, borderwidth=2, relief='groove').grid(row=30,
                                                                                                        column=24)
        Label(info_OF_frame, text='PANCAKE', width=12, height=3, borderwidth=2, relief='groove').grid(row=33, column=24)
        Label(info_OF_frame, text='WAFFLE', width=12, height=3, borderwidth=2, relief='groove').grid(row=36, column=24)
        Label(info_OF_frame, text='PRETZEL', width=12, height=3, borderwidth=2, relief='groove').grid(row=39, column=24)
        Label(info_OF_frame, text='DONUTS', width=12, height=3, borderwidth=2, relief='groove').grid(row=42, column=24)
        Label(info_OF_frame, text='COOKIES', width=12, height=3, borderwidth=2, relief='groove').grid(row=45, column=24)

        Label(info_OF_frame, text='Drinks Section', font=('Times New Roman', 16)).grid(row=2, column=34)
        Label(info_OF_frame, text='WATER', width=12, height=3, borderwidth=2, relief='groove').grid(row=5, column=34)
        Label(info_OF_frame, text='MILK', width=12, height=3, borderwidth=2, relief='groove').grid(row=9, column=34)
        Label(info_OF_frame, text='OAT MILK', width=12, height=3, borderwidth=2, relief='groove').grid(row=12,
                                                                                                       column=34)
        Label(info_OF_frame, text='COCA COLA', width=12, height=3, borderwidth=2, relief='groove').grid(row=15,
                                                                                                        column=34)
        Label(info_OF_frame, text='SOY MILK', width=12, height=3, borderwidth=2, relief='groove').grid(row=18,
                                                                                                       column=34)
        Label(info_OF_frame, text='APPLE JUICE', width=12, height=3, borderwidth=2, relief='groove').grid(row=21,
                                                                                                          column=34)
        Label(info_OF_frame, text='PEPSI', width=12, height=3, borderwidth=2, relief='groove').grid(row=24, column=34)
        Label(info_OF_frame, text='REDBULL', width=12, height=3, borderwidth=2, relief='groove').grid(row=27, column=34)
        Label(info_OF_frame, text='CODE-RED', width=12, height=3, borderwidth=2, relief='groove').grid(row=30,
                                                                                                       column=34)
        Label(info_OF_frame, text='ORANGE JUICE', width=12, height=3, borderwidth=2, relief='groove').grid(row=33,
                                                                                                           column=34)
        Label(info_OF_frame, text='LEMONADE', width=12, height=3, borderwidth=2, relief='groove').grid(row=36,
                                                                                                       column=34)
        Label(info_OF_frame, text='DIET PEPSI', width=12, height=3, borderwidth=2, relief='groove').grid(row=39,
                                                                                                         column=34)
        Label(info_OF_frame, text='PEPSI MAX', width=12, height=3, borderwidth=2, relief='groove').grid(row=42,
                                                                                                        column=34)
        Label(info_OF_frame, text='TEA', width=12, height=3, borderwidth=2, relief='groove').grid(row=45, column=34)

        # ============[variable for fruit]==========#
        APPLE = IntVar()
        PINEAPPLE = IntVar()
        BANANA = IntVar()
        BLUEBERRY = IntVar()
        GRAPE = IntVar()
        MANGO = IntVar()
        RASPBERRY = IntVar()
        STRAWBERRY = IntVar()
        ORANGE = IntVar()
        COCONUT = IntVar()
        WATERMELON = IntVar()
        SWEET_MELON = IntVar()
        BLACKBERRY = IntVar()
        PEACH = IntVar()
        # ============[variable for Veg]==========#
        CUCUMBER = IntVar()
        POTATO = IntVar()
        CORN = IntVar()
        ONION = IntVar()
        PEA = IntVar()
        PUMPKIN = IntVar()
        TOMATO = IntVar()
        MUSHROOM = IntVar()
        CARROT = IntVar()
        BROCCOLI = IntVar()
        BEET = IntVar()
        CHILLI = IntVar()
        OLIVES = IntVar()
        PARSLEY = IntVar()
        # ============[variable for Bakery]==========#
        WHITEBREAD = IntVar()
        BROWNBREAD = IntVar()
        BURGERBREAD = IntVar()
        WHITETOAST = IntVar()
        TORTILLA = IntVar()
        BAGEL = IntVar()
        CUPCAKE = IntVar()
        CAKE = IntVar()
        CROISSANT = IntVar()
        PANCAKE = IntVar()
        WAFFLE = IntVar()
        PRETZEL = IntVar()
        DONUTS = IntVar()
        COOKIES = IntVar()
        # ============[variable for Drinks]==========#
        WATER = IntVar()
        MILK = IntVar()
        OATMILK = IntVar()
        COCACOLA = IntVar()
        SOYMILK = IntVar()
        APPLEJUICE = IntVar()
        PEPSI = IntVar()
        REDBULL = IntVar()
        CODERED = IntVar()
        ORANGEJUICE = IntVar()
        LEMONADE = IntVar()
        DIETPEPSI = IntVar()
        PEPSIMAX = IntVar()
        TEA = IntVar()

        # ============[spinbox for fruit]==========#

        apple_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=APPLE)
        apple_spinbox.grid(row=5, column=4)
        list_for_ALL.append(apple_spinbox)

        pineapple_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=PINEAPPLE)
        pineapple_spinbox.grid(row=9, column=4)
        list_for_ALL.append(pineapple_spinbox)

        banana_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=BANANA)
        banana_spinbox.grid(row=12, column=4)
        list_for_ALL.append(banana_spinbox)

        blueberry_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=BLUEBERRY)
        blueberry_spinbox.grid(row=15, column=4)
        list_for_ALL.append(blueberry_spinbox)

        grape_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=GRAPE)
        grape_spinbox.grid(row=18, column=4)
        list_for_ALL.append(grape_spinbox)

        mango_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=MANGO)
        mango_spinbox.grid(row=21, column=4)
        list_for_ALL.append(mango_spinbox)

        raspberry_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=RASPBERRY)
        raspberry_spinbox.grid(row=24, column=4)
        list_for_ALL.append(raspberry_spinbox)

        strawberry_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=STRAWBERRY)
        strawberry_spinbox.grid(row=27, column=4)
        list_for_ALL.append(strawberry_spinbox)

        orange_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=ORANGE)
        orange_spinbox.grid(row=30, column=4)
        list_for_ALL.append(orange_spinbox)

        coconut_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=COCONUT)
        coconut_spinbox.grid(row=33, column=4)
        list_for_ALL.append(coconut_spinbox)

        watermelon_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=WATERMELON)
        watermelon_spinbox.grid(row=36, column=4)
        list_for_ALL.append(watermelon_spinbox)

        sweetmelon_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=SWEET_MELON)
        sweetmelon_spinbox.grid(row=39, column=4)
        list_for_ALL.append(sweetmelon_spinbox)

        blackberry_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=BLACKBERRY)
        blackberry_spinbox.grid(row=42, column=4)
        list_for_ALL.append(blackberry_spinbox)

        peach_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=7, justify=CENTER, textvariable=PEACH)
        peach_spinbox.grid(row=45, column=4)
        list_for_ALL.append(peach_spinbox)

        # ============[spinbox for Veg]==========#

        cucumber_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CUCUMBER)
        cucumber_spinbox.grid(row=5, column=16)
        list_for_ALL.append(cucumber_spinbox)

        potato_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=POTATO)
        potato_spinbox.grid(row=9, column=16)
        list_for_ALL.append(potato_spinbox)

        corn_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CORN)
        corn_spinbox.grid(row=12, column=16)
        list_for_ALL.append(corn_spinbox)

        onion_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=ONION)
        onion_spinbox.grid(row=15, column=16)
        list_for_ALL.append(onion_spinbox)

        pea_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PEA)
        pea_spinbox.grid(row=18, column=16)
        list_for_ALL.append(pea_spinbox)

        pumpkin_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PUMPKIN)
        pumpkin_spinbox.grid(row=21, column=16)
        list_for_ALL.append(pumpkin_spinbox)

        tomato_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=TOMATO)
        tomato_spinbox.grid(row=24, column=16)
        list_for_ALL.append(tomato_spinbox)

        mushroom_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=MUSHROOM)
        mushroom_spinbox.grid(row=27, column=16)
        list_for_ALL.append(mushroom_spinbox)

        carrot_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CARROT)
        carrot_spinbox.grid(row=30, column=16)
        list_for_ALL.append(carrot_spinbox)

        broccoli_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=BROCCOLI)
        broccoli_spinbox.grid(row=33, column=16)
        list_for_ALL.append(broccoli_spinbox)

        beet_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=BEET)
        beet_spinbox.grid(row=36, column=16)
        list_for_ALL.append(beet_spinbox)

        chilli_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CHILLI)
        chilli_spinbox.grid(row=39, column=16)
        list_for_ALL.append(chilli_spinbox)

        olives_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=OLIVES)
        olives_spinbox.grid(row=42, column=16)
        list_for_ALL.append(olives_spinbox)

        parsley_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PARSLEY)
        parsley_spinbox.grid(row=45, column=16)
        list_for_ALL.append(parsley_spinbox)

        # ============[spinbox for Bakery]==========#

        whitebread_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=WHITEBREAD)
        whitebread_spinbox.grid(row=5, column=26)
        list_for_ALL.append(whitebread_spinbox)

        brownbread_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=BROWNBREAD)
        brownbread_spinbox.grid(row=9, column=26)
        list_for_ALL.append(brownbread_spinbox)

        burgerbread_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER,
                                      textvariable=BURGERBREAD)
        burgerbread_spinbox.grid(row=12, column=26)
        list_for_ALL.append(burgerbread_spinbox)

        whitetoast_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=WHITETOAST)
        whitetoast_spinbox.grid(row=15, column=26)
        list_for_ALL.append(whitetoast_spinbox)

        tortilla_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=TORTILLA)
        tortilla_spinbox.grid(row=18, column=26)
        list_for_ALL.append(tortilla_spinbox)

        bagel_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=BAGEL)
        bagel_spinbox.grid(row=21, column=26)
        list_for_ALL.append(bagel_spinbox)

        cupcake_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CUPCAKE)
        cupcake_spinbox.grid(row=24, column=26)
        list_for_ALL.append(cupcake_spinbox)

        cake_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CAKE)
        cake_spinbox.grid(row=27, column=26)
        list_for_ALL.append(cake_spinbox)

        croissant_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CROISSANT)
        croissant_spinbox.grid(row=30, column=26)
        list_for_ALL.append(croissant_spinbox)

        pancake_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PANCAKE)
        pancake_spinbox.grid(row=33, column=26)
        list_for_ALL.append(pancake_spinbox)

        waffle_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=WAFFLE)
        waffle_spinbox.grid(row=36, column=26)
        list_for_ALL.append(waffle_spinbox)

        pretzel_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PRETZEL)
        pretzel_spinbox.grid(row=39, column=26)
        list_for_ALL.append(pretzel_spinbox)

        donuts_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=DONUTS)
        donuts_spinbox.grid(row=42, column=26)
        list_for_ALL.append(donuts_spinbox)

        cookies_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=COOKIES)
        cookies_spinbox.grid(row=45, column=26)
        list_for_ALL.append(cookies_spinbox)

        # ============[spinbox for Drinks]==========#

        water_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=WATER)
        water_spinbox.grid(row=5, column=36)
        list_for_ALL.append(water_spinbox)

        milk_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=MILK)
        milk_spinbox.grid(row=9, column=36)
        list_for_ALL.append(milk_spinbox)

        oatmilk_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=OATMILK)
        oatmilk_spinbox.grid(row=12, column=36)
        list_for_ALL.append(oatmilk_spinbox)

        cocacola_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=COCACOLA)
        cocacola_spinbox.grid(row=15, column=36)
        list_for_ALL.append(cocacola_spinbox)

        soymilk_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=SOYMILK)
        soymilk_spinbox.grid(row=18, column=36)
        list_for_ALL.append(soymilk_spinbox)

        applejuice_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=APPLEJUICE)
        applejuice_spinbox.grid(row=21, column=36)
        list_for_ALL.append(applejuice_spinbox)

        pepsi_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PEPSI)
        pepsi_spinbox.grid(row=24, column=36)
        list_for_ALL.append(pepsi_spinbox)

        redbull_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=REDBULL)
        redbull_spinbox.grid(row=27, column=36)
        list_for_ALL.append(redbull_spinbox)

        codered_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=CODERED)
        codered_spinbox.grid(row=30, column=36)
        list_for_ALL.append(codered_spinbox)

        orangejuice_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER,
                                      textvariable=ORANGEJUICE)
        orangejuice_spinbox.grid(row=33, column=36)
        list_for_ALL.append(orangejuice_spinbox)

        lemonade_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=LEMONADE)
        lemonade_spinbox.grid(row=36, column=36)
        list_for_ALL.append(lemonade_spinbox)

        dietpepsi_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=DIETPEPSI)
        dietpepsi_spinbox.grid(row=39, column=36)
        list_for_ALL.append(dietpepsi_spinbox)

        pepsimax_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=PEPSIMAX)
        pepsimax_spinbox.grid(row=42, column=36)
        list_for_ALL.append(pepsi_spinbox)

        tea_spinbox = Spinbox(info_OF_frame, from_=0, to=100, width=10, justify=CENTER, textvariable=TEA)
        tea_spinbox.grid(row=45, column=36)
        list_for_ALL.append(tea_spinbox)


class Third_Page(tk.Frame):
    def __init__(self, Frame1, The_controller_pages):
        tk.Frame.__init__(self, Frame1)
        self.config(background='#2D3B5E')
        Label(self, text='IAU SUPERMARKET', fg='white', bg='#8896AD', font=('Times New Roman', 20)).pack(fill=X)
        # =============[TOTAL]========#
        global Put_The_Total, Put_The_Date

        Put_The_Total = Entry(self, justify='center', font=15, width=20)
        Put_The_Total.place(x=650, y=250)
        Label(self, text='Total Price:', fg='white', bg='#2D3B5E',
              font=('Times New Roman', 15, 'bold')).place(x=545, y=250)

        Put_The_Date = Entry(self, justify='center', font=15, width=20)
        Put_The_Date.place(x=650, y=301)
        Label(self, text='Date:', fg='white', bg='#2D3B5E',
              font=('Times New Roman', 15, 'bold')).place(x=600, y=301)

        # [Back_button]:
        back_btn = Button(self, text='BACK', width=30, height=5,
                          font=('Times New Roman', 10, 'bold'), bd=2, relief=GROOVE,
                          command=lambda: The_controller_pages.get_page('Secondry_page'))
        back_btn.place(x=650, y=350)

        # [Button for exit]:

        EXIT_Button2 = Button(self, text='EXIT', width=7, height=3, font=('Times New Roman', 10, 'bold'),
                              bd=2,
                              relief=RIDGE, command=self.quit)
        EXIT_Button2.pack(padx=20, pady=20)


class forth_Page(tk.Frame):
    def __init__(self, Frame1, The_controller_pages):
        tk.Frame.__init__(self, Frame1)
        self.config(background='#2D3B5E')
        Label(self, text='IAU SUPERMARKET', fg='white', bg='#8896AD', font=('Times New Roman', 20)).pack(fill=X)
        # ==========[Username]===========

        UserName_Ent = Entry(self, justify='center', font=15, width=20)
        Label(self, text='Enter your username:', fg='white', bg='#2D3B5E',
              font=('Times New Roman', 15, 'bold')).place(x=460, y=250)
        UserName_Ent.place(x=630, y=250)

        # Button:

        UserName_btn = Button(self, text='SIGN IN', width=30, height=2, highlightthickness=1,
                              highlightbackground='black', command=lambda: signup())
        UserName_btn.place(x=640, y=350)

        # Back_buttoun:

        Back_to_LOCAL_FRAME = Button(self, text='Back', width=30, height=2, highlightthickness=1,
                                     highlightbackground='black',
                                     command=lambda: The_controller_pages.get_page('Local_page'))
        Back_to_LOCAL_FRAME.place(x=640, y=450)

        # ==========[Password]===========

        Password_Ent = Entry(self, justify='center', font=15, width=20)
        Label(self, text='Enter your Password:', fg='white', bg='#2D3B5E',
              font=('Times New Roman', 15, 'bold')).place(x=460, y=300)
        Password_Ent.place(x=630, y=300)
        global cursor

        conn = sqlite3.connect('super_market_database.bd')
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL)
                ''')

        def signup():
            username = UserName_Ent.get()
            password = Password_Ent.get()
            if username != '' and password != '':
                cursor.execute('SELECT username FROM users WHERE username=?', [username])
                if cursor.fetchone() is not None:
                    messagebox.showerror('Error', 'Username already exists')
                else:
                    encoded_password = password.encode('utf-8')
                    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                    cursor.execute('INSERT INTO users VALUES (?,?)', [username, hashed_password])
                    messagebox.showinfo('Success', 'Account has been created')
            else:
                messagebox.showerror('Error', 'Enter all data')


class The_maneging_window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.the_father_frame = tk.Frame()
        self.the_father_frame.grid_columnconfigure(0, weight=1)
        self.the_father_frame.grid_rowconfigure(0, weight=1)
        self.the_father_frame.pack(expand=True, fill='both')

        self.pages = {}
        for p in (Local_page, Secondry_page,
                  Third_Page, forth_Page):
            page_name = p.__name__
            frame = p(Frame1=self.the_father_frame,
                      The_controller_pages=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky='nesw')
        self.get_page(
            'Local_page')

    def get_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()


if __name__ == '__main__':
    The_window = The_maneging_window()
    The_window.geometry('1920x1080')
    The_window.iconbitmap(r'C:\Users\bd009\PycharmProjects\Supermarket_Project\iconn.ico')
    The_window.mainloop()
