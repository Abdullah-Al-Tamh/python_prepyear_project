import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create a button to switch to window 1
        self.button1 = tk.Button(self)
        self.button1["text"] = "Switch to Window 1"
        self.button1["command"] = self.show_window1
        self.button1.pack(side="top")

        # create a button to switch to window 2
        self.button2 = tk.Button(self)
        self.button2["text"] = "Switch to Window 2"
        self.button2["command"] = self.show_window2
        self.button2.pack(side="top")

    def show_window1(self):
        # hide the main window and show window 1
        self.master.withdraw()
        self.window1 = tk.Toplevel(self.master)
        self.window1.protocol("WM_DELETE_WINDOW", self.on_window1_close)
        self.label1 = tk.Label(self.window1, text="This is Window 1")
        self.label1.pack(side="top")

    def show_window2(self):
        # hide the main window and show window 2
        self.master.withdraw()
        self.window2 = tk.Toplevel(self.master)
        self.window2.protocol("WM_DELETE_WINDOW", self.on_window2_close)
        self.label2 = tk.Label(self.window2, text="This is Window 2")
        self.label2.pack(side="top")

    def on_window1_close(self):
        # show the main window and destroy window 1
        self.window1.destroy()
        self.master.deiconify()

    def on_window2_close(self):
        # show the main window and destroy window 2
        self.window2.destroy()
        self.master.deiconify()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
