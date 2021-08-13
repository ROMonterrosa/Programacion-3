#1
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
#muestre por pantalla<NOMBRE> tiene <n> letras, donde<NOMBRE>es el nombre de usuario en mayúsculas y <n>es el número 
#de letras que tienen el nombre.

def cadena(nombre):
    
    print("El nombre " + str(nombre.upper()) + " tiene " + str(len(nombre)) + " letras")
    
cadena(input("Cual es su nombre: "))

#Deteniendo el codigo
input("")