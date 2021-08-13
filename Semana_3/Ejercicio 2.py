#2
#Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
#En otra variable, almacena el resultado de la suma de esos dos números y  luego mostrarese  resultado  en  pantalla.
#A  continuación,  el  programa  debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar 
#en una nueva variable. Por último, mostraren pantalla el resultado de la multiplicación de este nuevo número por 
#el resultado de la suma anterior.

print("Ingrese dos numeros")
primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))

resultado = primer_numero + segundo_numero
print("La suma  de ambos numeros es: " + str(resultado))

tercer_numero = int(input("Ingrese otro numero: "))
resultado_dos = resultado * tercer_numero

print("La multiplicacion del tercer numero con la suma de los dos primeros numeros es " + str(resultado_dos))

input("")