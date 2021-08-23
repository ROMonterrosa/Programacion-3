#1. Escribir una clase en python que convierta un número entero a número romanos.

#Rene Orlando Monterrosa Santos
#SMTS585018

#Creando la clase
class Numero:    

#Creando el constructor
    def __init__(self, normal):
      if normal < 1 or normal > 4000:
        raise ValueError("No se soportan números menores de 1 o mayores de 4000")
      self.normal = normal
      self.romano = self.convert_to_roman()

#Creando el metodo

    def convert_to_roman(self):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"]
        romano = []
        i = 12
        valor = self.normal
        while valor:
            div = valor // num[i]
            valor %= num[i]
            while div:
                romano.append(sym[i])
                div -= 1
            i -= 1

        return "".join(romano)

#Captura de valores    
minumero = Numero(int(input("Ingrese el numero que desea convertir: ")))

#Muestra de datos
print("El numero que ingreso fue: " + str(minumero.normal))
print("El numero en romano es: " + str(minumero.romano))