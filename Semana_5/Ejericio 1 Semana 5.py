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

 #revisar que operacion es la que necesita en el codigo
 def acelerar(self,kilometros):
  return kilometros + self.velocidades

 def frenar(self):   
  return self.velocidades - 1
  
 def consultar_velocidad(self):
  print("La velocidad actual es: " + str(self.velocidades))


bicicleta1 = bicicleta(input("Ingrese el modelo: "),float(input("Ingrese el precio: ")),int(input("Ingrese las velocidades: ")))

#Prueba de codigo
#print("Se ha recorrido a velocidad: " + bicicleta1.velocidades + " los siguientes kilometros: " + str(bicicleta1.acelerar(input("Ingrese los kilometros recorridos: "))))

print("Se ha recorrido a velocidad: " + str(bicicleta1.acelerar(int(input("Ingrese los kilometros recorridos: ")))))
print("Se ha bajado la velocidad a: " + str(bicicleta1.frenar()))
str(bicicleta1.consultar_velocidad())

