# import Funciones_matematicas

from Funciones_matematicas import *

# Funciones_matematicas.sumar(5,7)
OP = input("Ingrese la operación que quiere realizar"
            +"\nOpciones"
            +"\nSuma"
            +"\nResta"
            +"\nMultplicar"
            +"\nDividir\n")

valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor: "))

if OP == "Suma":
    
    sumar(valor_1, valor_2)

elif OP == "Resta":
    
    restar(valor_1, valor_2)

elif OP == "Multiplicar":

    multiplicar(valor_1, valor_2)

elif OP == "Dividir":

    dividir(valor_1, valor_2)

else:
    print("Error esa opción no esta contemplada")    