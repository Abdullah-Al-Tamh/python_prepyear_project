import tkinter as tk


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # You can display the components of page1 here
        label = tk.Label(self, text="Page 1")
        label.pack(pady=10, padx=10)
        self.config(background='red')
        options = ['1', '2', '3']

        button = tk.Button(self, text="Go to Page 2",
                           command=lambda: controller.get_page("SecondPage"))
        button.pack()




class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame()
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.pack(fill='both', expand=True)

        self.pages = {}
        

        self.get_page('FirstPage')

    def get_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()





if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()