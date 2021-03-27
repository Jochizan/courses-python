txt = input("Ingrese una letra:")

crt = "es" if txt.lower().startswith(tuple("aeiou")) else "no es"

#Use "" .startswith () y "" .endswith () en lugar de cortar la cadena a Compruebe si hay prefijos o sufijos.

#Una tupla es una colección que se ordena e inmutable. En Python las tuplas se escriben con corchetes redondos.

print("La letra {} una vocal".format(crt))