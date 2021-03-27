class Coche():

    def __init__(self):
        
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancar):
        self.__nmarcha = arrancar

        if(self.__enmarcha):
            return "El coche está en marcha"
            
        else:
            return "el coche esta parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "Y un largo de ",
        self.__largoChasis)   
        
micoche = Coche()

#print("El largo del coche es: ", micoche.largoChasis)
#print("El coche tiene ", micoche.ruedas, " ruedas")
print(micoche.arrancar(True))

micoche.estado()

print("------------------------A continuación creamos el segundo objeto-------------------")

micoche2 = Coche()
#print("El largo del coche es: ", micoche.largoChasis)
#print("El coche tiene ", micoche.ruedas, " ruedas")
print(micoche2.arrancar(False))

micoche2.__ruedas = 2

micoche2.estado()

