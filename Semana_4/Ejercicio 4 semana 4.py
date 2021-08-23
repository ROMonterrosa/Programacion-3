#4. Genere el carné de un alumno sabiendo que está compuesto por la primera letra del nombre, la primera letra del apellido y el año actual

#Rene Orlando Monterrosa Santos
#SMTS585018

#Importo libreria para la año actual
from datetime import datetime
now = datetime.now()

#Creando la clase
class Carnet:

#Creando el constructor 
 def __init__(self,nombre,apellido,anio):
  self.nombre = nombre
  self.apellido = apellido
  self.anio = now.year

#Creo el metodo para generar el carnet que toma la primer letra y la pone en mayuscula, también toma el año actual
 def Generar_Carnet(self):
  print("Su carnet es: " + self.nombre[0].upper() + self.apellido[0].upper() + str(self.anio))

#Creo el objeto 
estudiante1 = Carnet(input("Ingrese su primer nombre: "),input("Ingrese su primer apellido: "),now.year)
estudiante2 = Carnet(input("Ingrese su primer nombre: "),input("Ingrese su primer apellido: "),now.year)
estudiante3 = Carnet(input("Ingrese su primer nombre: "),input("Ingrese su primer apellido: "),now.year)

#Mando a llamar el objeto con el metodo creado
estudiante1.Generar_Carnet()
estudiante2.Generar_Carnet()
estudiante3.Generar_Carnet()
