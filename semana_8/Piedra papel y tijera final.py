import tkinter as tk
import random
from tkinter.constants import CENTER
from typing import Text

class Aplicacion:    
    def __init__(self):        
     self.ventana = tk.Tk() 
     self.ventana.title("Piedra papel y tijera")
     self.ventana.geometry("200x200") 

     self.label4 = tk.Label(self.ventana,text="Piedra",height=2)
     self.label4.grid(column=0,row=0,padx = 5)
     self.label4 = tk.Label(self.ventana,text="Papel",height=2)
     self.label4.grid(column=0,row=1,padx = 5)
     self.label4 = tk.Label(self.ventana,text="Tijera",height=2)
     self.label4.grid(column=0,row=2,padx = 5)

     self.dato1 = tk.IntVar()

     self.radiobuton1 = tk.Radiobutton(self.ventana,variable=self.dato1,value=1,width=15)
     self.radiobuton1.grid(column=1,row=0) 
     self.radiobuton2 = tk.Radiobutton(self.ventana,variable=self.dato1,value=2)
     self.radiobuton2.grid(column=1,row=1)
     self.radiobuton3 = tk.Radiobutton(self.ventana,variable=self.dato1,value=3)
     self.radiobuton3.grid(column=1,row=2)

     self.result = tk.Label(self.ventana,text="Resultado",height=3,anchor="center")
     self.result.grid(column=1,row=3)
     self.boton1 = tk.Button(self.ventana, text="Jugar",command=self.jugar,anchor="center")
     self.boton1.grid(column=1,row=7) 
 
     self.ventana.mainloop()


    def jugar(self):
     numr1=random.randint(1,3)
    
     if self.dato1.get() == 1 and numr1 == 1:
      self.result["text"]="Empate"
     elif self.dato1.get() == 2 and numr1 == 2:
      self.result["text"]="Empate"
     elif self.dato1.get() == 3 and numr1 == 3:
      self.result["text"]="Empate"
     elif self.dato1.get() == 1 and numr1 == 2:
      self.result["text"]="Has perdido, sigue intentando"
     elif self.dato1.get() == 1 and numr1 == 3:
      self.result["text"]="Felicidades has ganado"
     elif self.dato1.get() == 2 and numr1 == 1:
      self.result["text"]="Felicidades has ganado"
     elif self.dato1.get() == 2 and numr1 == 3:
      self.result["text"]="Has perdido, sigue intentando"
     elif self.dato1.get() == 3 and numr1 == 1:
      self.result["text"]="Has perdido, sigue intentando"
     elif self.dato1.get() == 3 and numr1 == 2:
      self.result["text"]="Felicidades has ganado"

    def retrieve(self):
     print(self.dato1.get())

#Creando el objeto y llamando el programa
aplicacion1 = Aplicacion()