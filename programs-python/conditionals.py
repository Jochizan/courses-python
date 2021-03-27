print("Ingrese el valor de las notas del alumno")

nota_1 = int(input("Ingrese la nota 1: "))
nota_2 = int(input("Ingrese la nota 2: "))
nota_3 = int(input("Ingrese la nota 3: "))
nota_4 = int(input("Ingrese la nota 4: "))

if (nota_1 > 0) & (nota_2 > 0) & (nota_3 > 0) & (nota_4 > 0) & (nota_1 <= 20) & (nota_2 <= 20) & (nota_3 <= 20) & (nota_4 <= 20) :

     promedio = (nota_1 + nota_2 + nota_3 + nota_4)/4
     print("El promedio de notas es: " + str(promedio))
     if promedio > 10:
         print("¡Felicidades aprobaste!")
     else:
         print("Suerte para el siguiente consolidado...")
else:
     print("Error al ingreso de notas no puede haber negativas o mayores a 20")