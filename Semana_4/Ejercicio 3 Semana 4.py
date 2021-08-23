#3. Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de puertas y la placa. 
#Crear el constructor del coche, así como los métodos que considere necesarios. Crear una clase PruebaCoche que instancie varios coches, cambiándole el color a 
# algunos de ellos y mostrándolo por pantalla.

#Rene Orlando Monterrosa Santos
#SMTS585018

#Creando la clase
class Coche:

#Creando el constructor 
 def __init__(self,color,marca,modelo,puertas,placa):
  self.color = color
  self.marca = marca
  self.modelo = modelo
  self.puertas = puertas
  self.placa = placa

#Creando los metodos
 def Arrancar(self):
  print("El carro " + self.marca + " arranco")

 def Detener(self):
  print("El carro color " + self.color + " se detuvo")

 def Estacionar(self):
  print("El carro de " + self.puertas + " puertas se parqueo")
  
 def Retroceder(self):
  print("El carro con placa " + self.placa + " se descompuso")

carro1 = Coche(input("Ingrese el color del vehiculo: "),input("Ingrese la marca del vehiculo: "),input("Ingrese el modelo del vehiculo: "),
input("Ingrese las puertas del vehiculo: "),input("Ingrese la placa del vehiculo: "))

#Ejemplo de otro objeto instanciado
#carro2 = Coche(input("Ingrese el color del vehiculo: "),input("Ingrese la marca del vehiculo: "),input("Ingrese el modelo del vehiculo: "),
#input("Ingrese las puertas del vehiculo: "),input("Ingrese la placa del vehiculo: "))

#Usando los metodos para el objeto 1
carro1.Arrancar()
carro1.Detener()
carro1.Estacionar()
carro1.Retroceder()

#Usando metodos para el objeto 2
#carro2.Arrancar()
#carro2.Detener()
#carro2.Estacionar()
#carro2.Retroceder()