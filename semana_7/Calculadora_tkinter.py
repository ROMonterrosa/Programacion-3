import tkinter as tk
from tkinter import StringVar, Text, getint, ttk

def sumar():
 numero1 = int(dato1.get()) 
 numero2 = int(dato2.get())
 total = numero1 + numero2
 print("La suma es: " + str(total))

def restar():
 numero1 = int(dato1.get()) 
 numero2 = int(dato2.get())
 total = numero1 - numero2
 print("La resta es: " + str(total))

def multiplicar():
 numero1 = int(dato1.get()) 
 numero2 = int(dato2.get())
 if numero2 == 0:
   print("La multipliacacion es: 0")
 else:
  total = numero1 * numero2
  print("La multiplicacion es: " + str(total))

def dividir():
 numero1 = int(dato1.get()) 
 numero2 = int(dato2.get())
 if numero2 == 0:
   print("Ingrese un numero valido")
 else:
  total = numero1 / numero2
  print("La division es: " + str(total))

app = tk.Tk()
app.geometry("300x200")
app.title("Mi primer calculadora")

label1 = tk.Label(app, text="Escribe el primer numero")
label1.pack()
dato1 = tk.IntVar()
numero1 = tk.Entry(app,width=13,textvariable=dato1)
numero1.pack()

label2 = tk.Label(app, text="Escribe el segundo numero")
label2.pack()
dato2 = tk.IntVar()
numero2 = tk.Entry(app,width=13,textvariable=dato2)
numero2.pack()

button1 = tk.Button(app,text="Suma",width=13,height=1,command=sumar)
button1.pack()
button2 = tk.Button(app,text="Resta",width=13,height=1,command=restar)
button2.pack()
button3 = tk.Button(app,text="Multiplicacion",width=13,height=1,command=multiplicar)
button3.pack()
button4 = tk.Button(app,text="Division",width=13,height=1,command=dividir)
button4.pack()

app.mainloop()