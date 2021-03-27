class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculo):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito    )

# miMoto = Moto("Honda","CBR")

# miMoto.caballito()

# miMoto.estado()

class quad(Vehiculo):
    Salto = ""
    def Salto(self):
        self.Salto = "Saltando"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.Salto   )
    
# msquad = quad("Reys", "FRG")

# msquad.Salto()

# msquad.estado()

class furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

# mifurgoneta = furgoneta("Renault", "Kangoo")

# mifurgoneta.arrancar()

# mifurgoneta.estado()

print(mifurgoneta.carga(True))

class VElectricos(Vehiculo):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia = 100
    
    def cargaEnergia(self):
        self.cargando=True

class BicicletaElectrica(VElectricos, Vehiculo):
    pass

# miBici = BicicletaElectrica("Orbea", "HJ1500")