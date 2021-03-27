class gato():

    def __init__(self):
        self.__masa = 5 
        self.__largo = float(1)
        self.__ancho = 0.5
        self.__hambre = False
        self.__sueño = False
        self.__ganas_de_jugar = False
        self.__correr = False
        self.__saltar = False
        self.__arañar = False
        self.__maullar = False
        self.__comiendo = False
        self.__jugando = False
        self.__durmiendo = False
        self.__vivo = True
        self.__necesidades = False
    
    def Actividades(self, comer):
        self.__comiendo = comer

        if(self.__comiendo == True):
            return "El gato esta comiendo"
        
        else:
            return "El gato no esta comiendo"

    def Saltando(self, saltar):
        self.__saltar = saltar

        if(self.__saltar == True):
            return "El gato está saltando"

        else:
            return "El gato no esta saltando"

migato = gato()

comer = "si" == str(input("Ingrese 'si' o 'no' quiere que el gato coma: "))
saltar = "si" == str(input("Ingrese 'si' o 'no' quiere que el gato salte: "))

print(migato.Actividades(comer), "\n", migato.Saltando(saltar))
