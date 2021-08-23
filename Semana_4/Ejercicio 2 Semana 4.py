#2. Escribir una clase en python llamada rectangulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.

#Rene Orlando Monterrosa Santos
#SMTS585018

#Creando la clase
class Rectangulo:
 
#Realizando el constructor
 def __init__(self,altura,base):
  self.altura = altura
  self.base = base

#Realizando el metodo
 def area(self):
  return self.altura * self.base

#creando el objeto 
rectangulo = Rectangulo(int(input("Ingrese la altura: ")),int(input("Ingrese la base: ")))

#Mostrando los resultados
print("El area del Rectangulo es: " + str(rectangulo.area()))
