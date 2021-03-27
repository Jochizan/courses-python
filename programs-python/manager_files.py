from io import open

archivo_texto=open("archivo.txt", "r+") # lectura y escritura

# archivo_texto.write("\n Siempre es una buena ocasión para estudiar Python")

# archivo_texto.close()

# lineas_texto = archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto)

# texto = archivo_texto.readlines()

# archivo_texto.close()

# print(texto)

# frase = "Estupendo día para estudiar python\nel viernes\nsiempre es una buena ocasión para estudiar Python"

# archivo_texto.write(frase)

# archivo_texto.close()

# archivo_texto.seek(11)

# archivo_texto.seek(len(archivo_texto.readline()))   

# print(archivo_texto.read())

# archivo_texto.write("Comienzo del texto")

# print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();

lista_texto[1]=" Esta linea ha sido incluida del esxterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

# with io.open("file_dir", "modo"):

# print(archivo_texto.read())

print(archivo_texto.closed)