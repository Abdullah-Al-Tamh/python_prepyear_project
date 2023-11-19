import tkinter as tk

def show_frame1():
    # hide frame 2 and show frame 1
    frame2.pack_forget()
    frame1.pack()

def show_frame2():
    # hide frame 1 and show frame 2
    frame1.pack_forget()
    frame2.pack()

# create the main window
root = tk.Tk()

# create the frames for each button
frame1 = tk.Frame(root)
label1 = tk.Label(frame1, text="This is Frame 1")
label1.pack(side="top")

frame2 = tk.Frame(root)
label2 = tk.Label(frame2, text="This is Frame 2")
label2.pack(side="top")

# create the switchable buttons
button1 = tk.Button(root, text="Switch to Frame 1", command=show_frame1)
button1.pack(side="top")

button2 = tk.Button(root, text="Switch to Frame 2", command=show_frame2)
button2.pack(side="top")

# start the main event loop
root.mainloop()