import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create a button to switch to frame 1
        self.button1 = tk.Button(self)
        self.button1["text"] = "Switch to Frame 1"
        self.button1["command"] = self.show_frame1
        self.button1.pack(side="top")

        # create a button to switch to frame 2
        self.button2 = tk.Button(self)
        self.button2["text"] = "Switch to Frame 2"
        self.button2["command"] = self.show_frame2
        self.button2.pack(side="top")

        # create frame 1
        self.frame1 = tk.Frame(self)
        self.label1 = tk.Label(self.frame1, text="This is Frame 1")
        self.label1.pack(side="top")

        # create frame 2
        self.frame2 = tk.Frame(self)
        self.label2= tk.Label(self.frame2, text="This is Frame 2")
        self.label2.pack(side="top")

    def show_frame1(self):
        # hide frame 2 and show frame 1
        self.frame2.pack_forget()
        self.frame1.pack()

    def show_frame2(self):
        # hide frame 1 and show frame 2
        self.frame1.pack_forget()
        self.frame2.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()