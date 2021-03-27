import pickle
# from SerializarObjeto import Vehiculo

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:

    print(c.estado())