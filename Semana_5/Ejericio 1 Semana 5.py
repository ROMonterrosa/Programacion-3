#Desarrolle el siguiente ejercicio en parejas y ambos deben pegar su código en canvas.

#Rene Orlando Monterrosa Santos
#SMTS585018

#Crear una clase en Python que se llame Bicicleta, debe tener las siguientes variables o propiedades: modelo, precio, números de velocidades. Debe tener los métodos: Acelerar, 
#Frenar y Consultar Velocidad.

#Consideraciones especiales sobre la clase.

#Al método Acelerar hay que pasarle por parámetros kilómetros y a la propiedad velocidad sumarle esos kilómetros.
#El método Frenar debe restar la velocidad en 1
#El método Consultar Velocidad debe imprimir la velocidad

#Creando la clase

class bicicleta:

#Creando el constructor
 def __init__(self,modelo,precio,velocidades):
  self.modelo = modelo
  self.precio = precio
  self.velocidades = velocidades

#Creando los metodos

 def acelerar(self,kilometros):
  return kilometros + self.velocidades

 def frenar(self):   
  return self.velocidades - 1
  
 def consultar_velocidad(self):
  print("La velocidad actual es: " + str(self.velocidades))

#Crear el objeto pasandole parametros por medio de consola

bicicleta1 = bicicleta(input("Ingrese el modelo: "),float(input("Ingrese el precio: ")),int(input("Ingrese las velocidades: ")))

#Mando a llamar el objeto con la instancia

print("Se han recorrido " + str(bicicleta1.acelerar(int(input("Ingrese los kilometros recorridos: ")))) + " kilometros")
print("Se ha bajado la velocidad a: " + str(bicicleta1.frenar()))
bicicleta1.consultar_velocidad()

