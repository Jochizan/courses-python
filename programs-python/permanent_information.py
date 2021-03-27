import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado un persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    Personas = []

    def __init__(self):
        ListaPersonas = open("ficheroExterno", "ab+")
        ListaPersonas.seek(0)

        try:
            self.Personas = pickle.load(ListaPersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.Personas))) 

        except:
            print("El fichero está vacío")
        
        finally:
            ListaPersonas.close()
            del(ListaPersonas)

    def agregarPersonas(self, p):
        self.Personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.Personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        ListaPersonas=open("ficheroExterno", "wb")
        pickle.dump(self.Personas, ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.Personas:
            print(p)

# miLista = ListaPersonas()
# p = Persona("Sandra", "Femenino", 29)
# miLista.agregarPersonas(p)
# p = Persona("Antonio", "Masculino", 39)
# miLista.agregarPersonas(p)
# p = Persona("Ana", "Femenino", 19)
# miLista.agregarPersonas(p)
miLista = ListaPersonas()
# miLista.mostrarPersonas() 
persona = Persona("Julia", "Femenino", 29)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()