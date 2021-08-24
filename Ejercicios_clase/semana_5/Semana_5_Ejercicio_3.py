'''
Crea una clase persona. Sus atributos deben ser su nombre y su edad.
Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
'''

class Persona:
    
 def __init__(self,nombre,edad):
  self.nombre = nombre
  self.edad = edad
    
 def cumple(self):
  
  edad = self.edad + 1 
  print("¡Felidades! ahora tienes: " + str(edad)) 
              
persona1 = Persona("Carlos",int(input("Ingrese su edad: ")))
#persona2 = Persona("Jose",int(input("Ingrese su edad: ")))
                   
persona1.cumple()
#persona2.cumple()