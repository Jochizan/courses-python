import pickle

fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

print(lista)

# Codigo para crear la lista en código binario:

# lista_nombres = ["Pedro", "Ana", "María", "Isabel"]

# fichero_binario = open("Lista_nombres", "wb")

# pickle.dump(lista_nombres, fichero_binario)

# fichero_binario.close()

# del (fichero_binario)