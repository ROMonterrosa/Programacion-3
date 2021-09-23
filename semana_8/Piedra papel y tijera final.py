import tkinter as tk
import random

#Creo la clase 
class Aplicacion:

#Defino el metodo constructor, titulo, tamaño, etc    
    def __init__(self):        
     self.ventana = tk.Tk() 
     self.ventana.title("Piedra papel y tijera")
     self.ventana.geometry("250x200") 

#Creo los label y los posiciono
     self.label2 = tk.Label(self.ventana,text="Piedra",height=2,padx=2)
     self.label2.grid(column=0,row=0,padx=2)
     self.label3 = tk.Label(self.ventana,text="Papel",height=2)
     self.label3.grid(column=0,row=1)
     self.label4 = tk.Label(self.ventana,text="Tijera",height=2)
     self.label4.grid(column=0,row=2)

#Almaceno el dato
     self.dato1 = tk.IntVar()

#Creo los radiobutton
     self.radiobuton1 = tk.Radiobutton(self.ventana,variable=self.dato1,value=1,width=18)
     self.radiobuton1.grid(column=1,row=0) 
     self.radiobuton2 = tk.Radiobutton(self.ventana,variable=self.dato1,value=2)
     self.radiobuton2.grid(column=1,row=1)
     self.radiobuton3 = tk.Radiobutton(self.ventana,variable=self.dato1,value=3)
     self.radiobuton3.grid(column=1,row=2)

#Creo el label para almacenar el resultado
     self.result = tk.Label(self.ventana,text="Resultado",height=3)
     self.result.grid(column=1,row=3)

#Creo el boton
     self.boton1 = tk.Button(self.ventana, text="Jugar",command=self.jugar)
     self.boton1.grid(column=1,row=4) 
 
     self.ventana.mainloop()

#Creo el metodo donde se elige un numero random entre 1 y 3, luego se evalua segun la selección del jugador
    def jugar(self):
     numr1=random.randint(1,3)
    
     if self.dato1.get() == 1 and numr1 == 1:
      self.result["text"]="Empate"
     elif self.dato1.get() == 2 and numr1 == 2:
      self.result["text"]="Empate"
     elif self.dato1.get() == 3 and numr1 == 3:
      self.result["text"]="Empate"
     elif self.dato1.get() == 1 and numr1 == 2:
      self.result["text"]="Perdiste, sigue intentando"
     elif self.dato1.get() == 1 and numr1 == 3:
      self.result["text"]="Felicidades, has ganado"
     elif self.dato1.get() == 2 and numr1 == 1:
      self.result["text"]="Felicidades, has ganado"
     elif self.dato1.get() == 2 and numr1 == 3:
      self.result["text"]="Perdiste, sigue intentando"
     elif self.dato1.get() == 3 and numr1 == 1:
      self.result["text"]="Perdiste, sigue intentando"
     elif self.dato1.get() == 3 and numr1 == 2:
      self.result["text"]="Felicidades, has ganado"

#Creando el objeto y llamando el programa
aplicacion1 = Aplicacion()