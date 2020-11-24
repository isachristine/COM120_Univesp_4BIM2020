from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='caderno.gif').subsample(2)
image = Label(master=root, image=photo)
image.pack(side=TOP)
hello = Label(master=root, text='Olá Mundo!', font=("Arial", 20))
hello.pack(side=BOTTOM)
root.mainloop()
