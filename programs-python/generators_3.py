def devuelve_ciudades(*ciudades):
    
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento

ciudad_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print("Madrid", "Barcelona", "Bilbao", "Valencia")

print(ciudad_devueltas)

for letter in ciudad_devueltas:
    print(letter)

# print(next(ciudad_devueltas))

# print(next(ciudad_devueltas))

# print(next(ciudad_devueltas))
