from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="MindBlown.gif")
Label(miFrame, image=miImagen).place(x=100,y=100)
# miLabel=Label(miFrame, text="Hola Joan hdprra", fg="blue", font=("JetBrains Mono", 18))
# miLabel.place(x=100, y=200)

root.mainloop()