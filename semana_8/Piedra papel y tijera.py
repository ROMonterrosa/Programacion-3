from tkinter import *
import random

root = Tk()
root.title("Piedra papel o tijera")
root.geometry("300x200")
frame = Frame(root)
frame.pack()

Var1 = IntVar()
Var2 = IntVar()

lbl2 = Label(frame,text = "Elige una opción",textvariable=Var2.get())
lbl2.pack(padx=5,pady=5)

RBttn = Radiobutton(frame, text = "Piedra", variable = Var1, value = 1)
RBttn.pack(padx = 5, pady = 5)
RBttn2 = Radiobutton(frame, text = "Papel", variable = Var1,value = 2)
RBttn2.pack(padx = 5, pady = 5)
RBttn = Radiobutton(frame, text = "Tijera", variable = Var1, value = 3)
RBttn.pack(padx = 5, pady = 5)
result = Label(frame,text="")
result.pack()

def jugar():
 numr1=random.randint(1,3)
 if Var1.get() == 1 and numr1 == 1:
    result["text"]="Empate"
 elif Var1.get() == 2 and numr1 == 2:
    result["text"]="Empate"
 elif Var1.get() == 3 and numr1 == 3:
    result["text"]="Empate"
 elif Var1.get() == 1 and numr1 == 2:
    result["text"]="Sigue intentando"
 elif Var1.get() == 1 and numr1 == 3:
    result["text"]="Felicidades has ganado"
 elif Var1.get() == 2 and numr1 == 1:
    result["text"]="Felicidades has ganado"
 elif Var1.get() == 2 and numr1 == 3:
    result["text"]="Sigue intentando"
 elif Var1.get() == 3 and numr1 == 1:
    result["text"]="Sigue intentando"
 elif Var1.get() == 3 and numr1 == 2:
    result["text"]="Felicidades has ganado"

Button = Button(frame, text = "Submit", command = jugar)
Button.pack()
root.mainloop()