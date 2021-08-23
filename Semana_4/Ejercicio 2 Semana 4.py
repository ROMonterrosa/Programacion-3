#2. Escribir una clase en python llamada rectangulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.

class Rectangulo:
 PI =3.14

 def __init__(self,altura,base):
  self.altura = altura
  self.base = base

 def area(self):
  return self.altura * self.base

rectangulo = Rectangulo(int(input("Ingrese la altura: ")),int(input("Ingrese la base: ")))
print("El area del Rectangulo es: " + str(rectangulo.area()))
