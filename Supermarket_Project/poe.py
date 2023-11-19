class Secondry_page(tk.Frame):
    def __init__(self, Frame1, The_controller_pages):
        tk.Frame.__init__(self, Frame1)
        self.The_controller_pages = The_controller_pages
        self.config(background='red')
        Label(self, text='IAU SUPERMARKET', fg='red', bg='red', font=('Times New Roman', 20)).pack(fill=X)

        # create a frame to hold the buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.config(background='black')
        buttons_frame.configure(width=260, height=1080)
        buttons_frame.pack(side=LEFT)

        # create a frame to hold the content
        content_frame = tk.Frame(self, bg='white')
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # create the fruit section button
        FRUITS_SECTION_butt = Button(buttons_frame, text='FRUITS SECTION', width=30, height=5,
                                     font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                                     command=lambda: self.show_fruit_section(content_frame))
        FRUITS_SECTION_butt.place(x=20, y=50)

        # create the vegetables section button
        VEGETABLES_SECTION_butt = Button(buttons_frame, text='VEGETABLES SECTION', width=30, height=5,
                                        font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                                        command=lambda: self.show_vegetables_section(content_frame))
        VEGETABLES_SECTION_butt.place(x=20, y=120)

        # create the dairy section button
        DAIRY_SECTION_butt = Button(buttons_frame, text='DAIRY SECTION', width=30, height=5,
                                    font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                                    command=lambda: self.show_dairy_section(content_frame))
        DAIRY_SECTION_butt.place(x=20, y=190)

        # create the exit button
        EXIT_Button = Button(buttons_frame, text='EXIT', width=7, height=3, font=('Times New Roman', 10, 'bold'), bd=1,
                             relief=GROOVE, command=self.quit)
        EXIT_Button.place(x=20, y=720)

        # create the back button
        back_btn = Button(buttons_frame, text='BACK', width=7, height=3, font=('Times New Roman', 9, 'bold'), bd=1,
                          relief=GROOVE, command=lambda: The_controller_pages.get_page('Local_page'))
        back_btn.place(x=190, y=720)

    def show_continued:

        # create the dairy section button
        DAIRY_SECTION_butt = Button(buttons_frame, text='DAIRY SECTION', width=30, height=5,
                                    font=('Times New Roman', 10, 'bold'), bd=1, relief=GROOVE,
                                    command=lambda: self.show_dairy_section(content_frame))
        DAIRY_SECTION_butt.place(x=20, y=190)

        # create the exit button
        EXIT_Button = Button(buttons_frame, text='EXIT', width=7, height=3, font=('Times New Roman', 10, 'bold'), bd=1,
                             relief=GROOVE, command=self.quit)
        EXIT_Button.place(x=20, y=720)

        # create the back button
        back_btn = Button(buttons_frame, text='BACK', width=7, height=3, font=('Times New Roman', 9, 'bold'), bd=1,
                          relief=GROOVE, command=lambda: The_controller_pages.get_page('Local_page'))
        back_btn.place(x=190, y=720)

    def show_fruit_section(self, content_frame):
        # clear all widgets from the content frame
        for widget in content_frame.winfo_children():
            widget.destroy()

        # create a label to display the fruit section
        Label(content_frame, text='Fruit Section', font=('Times New Roman', 20)).pack()

        # createContinuing from where we left off in the previous answer, here's an example of how you can add multiple frames with multiple buttons: