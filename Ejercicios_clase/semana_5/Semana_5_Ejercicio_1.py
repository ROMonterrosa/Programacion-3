'''
Crear una clase que use constructor y otros métodos y que calcule el promedio de notas 
de tres notas de un alumno. Se debe mostrar:
alumno nombrealumno usted aprobó o reprobó según sea el caso
'''

class notas:
 def __init__(self,nombre,nota1,nota2,nota3):
    self.nombre = nombre
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3
    
 def promedio(self):
    promedio = round((self.nota1+self.nota2+self.nota3)/3,2)
    if promedio >= 7:
        print("El alumno " + self.nombre + " aprobo con: " + str(promedio) + " de nota")
    else:
         print("El alumno " + self.nombre + " reprobo con: " + str(promedio) + " de nota")

alumno1 = notas("Carlos",5,7,9)
alumno2 = notas("Jose",3,9,8)

alumno1.promedio()
alumno2.promedio()
