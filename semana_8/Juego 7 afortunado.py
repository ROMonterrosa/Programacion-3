import tkinter as tk
import random

window = tk.Tk()
window.title("7 AFORTUNADO")
window.geometry("300x200")

def generar():
    numr1=random.randint(1,9)
    numr2=random.randint(1,9)
    numr3=random.randint(1,9)
    num1["text"]=numr1
    num2["text"]=numr2
    num3["text"]=numr3

    if numr3==7 and numr2==7 and numr1==7:
        result["text"]="Felicidades has ganado"
    else:
        result["text"]="Sigue intentando"

lblIntruccion=tk.Label(window,text="Genera 3 numeros aleatorios y si todos son 7 ganas")
lblIntruccion.pack()

btnGenerar=tk.Button(window, text="Generar", command=generar)
btnGenerar.pack()

num1=tk.Label(window, text="")
num1.pack()
num2=tk.Label(window, text="")
num2.pack()
num3=tk.Label(window, text="")
num3.pack()
result=tk.Label(window,text="")
result.pack()

window.mainloop()
