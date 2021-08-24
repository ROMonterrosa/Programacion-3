'''
Crear una clase que represente un empleado. 
Definir como atributos su nombre y su sueldo. 
En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y 
por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
'''

class Empleado:
    
 def __init__(self,nombre,salario):
  self.nombre = nombre
  self.salario = salario
      
 def pagar(self):
    
  if self.salario >=3000:
   print("La persona " + self.nombre + " debe pagar impuestos")
  else:
   print("La persona " + self.nombre + " no debe pagar impuestos")

persona1 = Empleado(input("Ingrese su nombre: "),int(input("Ingrese su salario:")))
persona2 = Empleado(input("Ingrese su nombre: "),int(input("Ingrese su salario:")))

persona1.pagar()
persona2.pagar()