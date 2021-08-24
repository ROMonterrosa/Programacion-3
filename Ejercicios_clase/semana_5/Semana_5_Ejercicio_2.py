'''
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DUI. 
Construye los siguientes métodos para la clase:

Un constructor.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
    
 def __init__(self,nombre,edad,dui):
  self.nombre = nombre
  self.edad = edad
  self.dui = dui
    
 def mayor_edad(self):
    
  if self.edad >=18:
   print("La persona " + self.nombre + " es mayor de edad")

  else:
   print("La persona " + self.nombre + " es menor de edad")
            
persona1 = Persona("Carlos",int(input("Ingrese su edad: ")),1090909)
persona2 = Persona("Jose",int(input("Ingrese su edad: ")),12012012)

persona1.mayor_edad()
persona2.mayor_edad()        
