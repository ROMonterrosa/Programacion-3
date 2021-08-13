#3
#Escribí  un  programa  que  solicite  al  usuario  el  ingreso  de  una  temperatura  en escala Fahrenheit 
#(debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa 
#para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)

grados_fahrenheit = float(input("Ingrese la temperatura en fahrenheit "))

grados_celsius = round((5/9) * (grados_fahrenheit-32),2)

print(str(grados_fahrenheit) + " grados fahrenheit equivalen a " + str(grados_celsius) + " celsius")
