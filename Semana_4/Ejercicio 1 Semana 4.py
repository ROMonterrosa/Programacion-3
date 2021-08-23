#1. Escribir una clase en python que convierta un número entero a número romanos.

'''class Conversion:

 def num2roman(num):
  
  num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
  roman = ''

  while num > 0:
       for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

  return roman
 
print(Conversion.num2roman(10))

 def numero_romano(entero):
  numeros = [1000,900,500,400,100,90,50,40,10,9,5,1]
  numerales = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

  numeral = ""
  i = 0

  while entero > 0:
      for _ in range(entero// numeros[i]):
          numeral += numerales[i]
          entero-= numeros[i]
      i += 1
  return numeral

numero = Conversion()
numero.numero_romano(10)

print(numero.numero_romano)
'''