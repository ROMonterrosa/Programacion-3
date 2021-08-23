#3. Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de puertas y la placa. 
#Crear el constructor del coche, así como los métodos que considere necesarios. Crear una clase PruebaCoche que instancie varios coches, cambiándole el color a 
# algunos de ellos y mostrándolo por pantalla.

class Coche:
 
 def __init__(self,color,marca,modelo,puertas,placa):
  self.color = color
  self.marca = marca
  self.modelo = modelo
  self.puertas = puertas
  self.placa = placa

 def Modelo_Marca(self):
  print(self.marca + self.modelo)

carro1 = Coche(input("Ingrese el color del vehiculo: "),"Tucson","Hyundai","4","0517958-5")

print("PruebaCoche: " + str(carro1))

'''carro10 = Coche(input("Ingrese el color del vehiculo: "),input("Ingrese la marca del vehiculo: "),input("Ingrese el modelo del vehiculo: "),
input("Ingrese la cantidad de puertas del vehiculo: "),input("Ingrese la placa del vehiculo: "))

print("Las caracteristicas del carro son las siguienes: " + str(carro1))

 class MyClass:
variable = "blah"
def function(self):
print("Este mensaje está dentro de una clase.")


#instanciamos o creamos dos objetos de la clase
myobjectx = MyClass()
myobjecty = MyClass()

#le cambiamos valor a la variable global del objeto y
myobjecty.variable = "yackity"

# Entonces se imprimen ambos valores
print(myobjectx.variable) # imprime "blah"
print(myobjecty.variable) # imprime "yackity"
'''