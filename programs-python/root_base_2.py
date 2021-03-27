import math

def cálculoRaíz(num1):

    if num1 < 0:
        raise ValueError ("El número no puede ser negativo")

    else:
        return math.sqrt(num1)

op1 = int(input("Introduce un número: "))

try:
    print(cálculoRaíz(op1))

except ValueError as ErrorDeNumeroNegativo:

    print(ErrorDeNumeroNegativo)

print("Programa terminado")