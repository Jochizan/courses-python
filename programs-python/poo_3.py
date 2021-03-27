class Coche():

    def __init__(self):
        
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancar):
        self.__enmarcha = arrancar

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
            
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo.\nNo podemos Arrancar"

        else:
            return "el coche esta parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "Y un largo de ",
        self.__largoChasis)   
        
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        self.gasolina = str(input("Ingrese si esta 'ok' la gasolina o no: "))

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):

            return True

        else:
            return False

micoche = Coche()

#print("El largo del coche es: ", micoche.largoChasis)
#print("El coche tiene ", micoche.ruedas, " ruedas")
print(micoche.arrancar(True))

micoche.estado()

#print(micoche.chequeo_interno())

print("------------------------A continuación creamos el segundo objeto-------------------")

micoche2 = Coche()
#print("El largo del coche es: ", micoche.largoChasis)
#print("El coche tiene ", micoche.ruedas, " ruedas")
print(micoche2.arrancar(False))

micoche2.estado()
