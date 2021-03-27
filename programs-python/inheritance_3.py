class coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class moto():

    def desplazamiento(self):
        print("Me desplazo utlizando dos ruedas")

class camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = coche()

desplazamientoVehiculo(miVehiculo)