import tkinter as tk


class FirstWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='This is window 1').pack(padx=10, pady=10)
        self.pack(padx=10, pady=10)


class SecondWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text='This is window 2').pack(padx=10, pady=10)
        self.pack(padx=10, pady=10)


class MainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10, pady=10, fill='both', expand=1)
        self.index = 0

        self.frameList = [FirstWindow(mainframe), SecondWindow(mainframe)]
        self.frameList[1].forget()

        bothframe = tk.Frame(master)
        bothframe.pack(padx=10, pady=10)

        switch = tk.Button(bothframe, text='Switch', command=self.changeWindow)

    def changeWindow(self):
        self.frameList[self.index].forget()
        self.index = (self.index + 1) % len(self.frameList)
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack(padx=10, pady=10)


root = tk.Tk()
root.mainloop()
