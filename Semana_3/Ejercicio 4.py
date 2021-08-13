#4
#Crear  un  programa  en Pythonque  solicite  usuario  y  contraseña,  si  el  usuario ingresa  en  ambas 
#credenciales  la  cadena  UGB  permitirle  el  ingreso  al  sistema, caso contrario mostrar mensaje de advertencia.

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if (user == "UGB" and password == "UGB"):
    print("¡Bienvenido!")
else:
    print("Se ha producido un error en su intento de inicio de sesión.")

#Deteniendo el codigo
input("")