def devuelve_ciudades(*ciudades):
    
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudad_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudad_devueltas))

print(next(ciudad_devueltas))
