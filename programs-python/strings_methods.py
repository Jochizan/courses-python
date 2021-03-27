nombreUsuario = input("Introduve tu nombre de usuario:")

while(nombreUsuario.isdigit() == True):

    print("Ingrese su nombre por favor")
    nombreUsuario = input("\nIntroduzca su nombre: ")


print("El nombre es: ", nombreUsuario.capitalize())

edad = input("Introduce su edad: ")

while(edad.isdigit()==False):

    print("Por favor, introduce un valor númerico")

    edad = input("\nIngrese su edad en números: ")

if (int(edad)<18):

    print("No puedes pasar")

else:
    
    print("Puedes pasar")
