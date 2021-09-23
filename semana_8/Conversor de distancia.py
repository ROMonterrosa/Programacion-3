import tkinter as tk
from tkinter import Message, StringVar, Text, getint, ttk
#1. desarrolla una app que permita convertir de kilómetros, millas, centímetros, pulgadas, metros. aqui tienes una idea de la interfaz:

#Creando el metodo constructor
class Aplicacion:    
    def __init__(self):        
     self.ventana = tk.Tk() 
     self.ventana.title("Conversor de distancia")
     self.ventana.geometry("375x100")  
#Creando el label 1
     self.label1 = tk.Label(self.ventana, text="Entrada")        
     self.label1.grid(column=0, row=0)      
#Creando un combobox 1
     medidas1 = ["Kilometros", "Millas", "Centimetros", "Pulgadas","Metros"]
     self.opcion1 = StringVar()
     self.combo1 = ttk.Combobox(self.ventana,state="readonly",width=15,textvariable=self.opcion1)
     self.combo1["values"] = medidas1
     self.combo1.grid(column=1,row=0)
           
#Creando el label 2
     self.label2 = tk.Label(self.ventana, text="Salida")        
     self.label2.grid(column=2, row=0)  
#Creando un combobox 2
     medidas2 = ["Kilometros", "Millas", "Centimetros", "Pulgadas","Metros"]
     self.opcion2 = StringVar()
     self.combo2 = ttk.Combobox(self.ventana,state="readonly",width=15, textvariable=self.opcion2)
     self.combo2["values"] = medidas2
     self.combo2.grid(column=3,row=0)
     
#Creando el label 3      
     self.label3 = tk.Label(self.ventana,text="Valor")
     self.label3.grid(column=0,row=2)
#Creando el entry con el dato que almacena el valor
     self.dato1 = tk.DoubleVar()        
     self.entry1 = tk.Entry(self.ventana, width=18, textvariable=self.dato1)        
     self.entry1.grid(column=1, row=2)    

#Creando el label 4
     self.label4 = tk.Label(self.ventana,text="Resultado")
     self.label4.grid(column=2,row=2)

#Creando el entry con el dato para poder pasar el resultado
     self.dato2 = tk.DoubleVar()        
     self.entry2 = tk.Entry(self.ventana, width=18,textvariable=self.dato2)        
     self.entry2.grid(column=3, row=2)

#Creando el boton 1
     self.boton1 = tk.Button(self.ventana, text="Limpiar",command=self.clear)
     self.boton1.grid(column=2, row=3)
#Creando el boton 2
     self.boton2 = tk.Button(self.ventana, text="Convertir",command=self.operacion)
     self.boton2.grid(column=0, row=3)

#terminando el metodo constructor para mostrar la app
     self.ventana.mainloop()

#Metodo para borrar el entry 2   
    def clear(self):       
     self.entry2.delete(0, 'end')
     print(self.combo1)

#Metodo que calcula todas las posibles combinaciones de combobox
    def operacion(self):
     if self.combo1.get() == "Kilometros" and self.combo2.get() == "Kilometros":
       self.dato2.set(self.dato1.get())
     elif self.combo1.get() == "Kilometros" and self.combo2.get() == "Millas":
       valor = self.dato1.get() * 0.621371
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Kilometros" and self.combo2.get() == "Centimetros":
       valor = self.dato1.get() * 100000
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Kilometros" and self.combo2.get() == "Pulgadas":
       valor = self.dato1.get() * 39370.079
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Kilometros" and self.combo2.get() == "Metros":
       valor = self.dato1.get() * 1000
       self.dato2.set(str(valor))

     elif self.combo1.get() == "Millas" and self.combo2.get() == "Millas":
       self.dato2.set(self.dato1.get())
     elif self.combo1.get() == "Millas" and self.combo2.get() == "Kilometros":
       valor = self.dato1.get() * 1.60934
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Millas" and self.combo2.get() == "Centimetros":
       valor = self.dato1.get() * 160934
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Millas" and self.combo2.get() == "Pulgadas":
       valor = self.dato1.get() * 63360
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Millas" and self.combo2.get() == "Metros":
       valor = self.dato1.get() * 1609.34
       self.dato2.set(str(valor))

     elif self.combo1.get() == "Centimetros" and self.combo2.get() == "Centimetros":
       self.dato2.set(self.dato1.get())
     elif self.combo1.get() == "Centimetros" and self.combo2.get() == "Kilometros":
       valor = self.dato1.get() * 0.00001
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Centimetros" and self.combo2.get() == "Millas":
       valor = self.dato1.get() * 0.000006
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Centimetros" and self.combo2.get() == "Pulgadas":
       valor = self.dato1.get() * 0.393701
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Centimetros" and self.combo2.get() == "Metros":
       valor = self.dato1.get() * 0.01
       self.dato2.set(str(valor))

     elif self.combo1.get() == "Pulgadas" and self.combo2.get() == "Pulgadas":
       self.dato2.set(self.dato1.get())
     elif self.combo1.get() == "Pulgadas" and self.combo2.get() == "Kilometros":
       valor = self.dato1.get() * 0.0000254
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Pulgadas" and self.combo2.get() == "Millas":
       valor = self.dato1.get() * 0.000015783
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Pulgadas" and self.combo2.get() == "Centimetros":
       valor = self.dato1.get() * 2.54
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Pulgadas" and self.combo2.get() == "Metros":
       valor = self.dato1.get() * 0.0254
       self.dato2.set(str(valor))

     elif self.combo1.get() == "Metros" and self.combo2.get() == "Metros":
       self.dato2.set(self.dato1.get())
     elif self.combo1.get() == "Metros" and self.combo2.get() == "Kilometros":
       valor = self.dato1.get() * 0.001
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Metros" and self.combo2.get() == "Millas":
       valor = self.dato1.get() * 0.000621371
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Metros" and self.combo2.get() == "Centimetros":
       valor = self.dato1.get() * 100
       self.dato2.set(str(valor))
     elif self.combo1.get() == "Metros" and self.combo2.get() == "Pulgadas":
       valor = self.dato1.get() * 39.3701
       self.dato2.set(str(valor))
     else:
      pass

#Creando el objeto y llamando el programa
aplicacion1 = Aplicacion()