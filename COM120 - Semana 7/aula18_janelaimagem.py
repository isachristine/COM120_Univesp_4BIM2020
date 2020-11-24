from tkinter import Tk, PhotoImage, Label

root = Tk()
photo = PhotoImage(file="caderno.gif").subsample(2)
hello = Label(master=root, image=photo, width=300, height=180)
hello.pack()
root.mainloop()
