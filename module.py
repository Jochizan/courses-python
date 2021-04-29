from math import log10, log
from hello import suma

def gradosKelvin(grados):
    return grados + 273

def gradosFahrenheit(grados):
    grados = grados * 1.8
    grados = grados + 32
    return grados

# print(gradosFahrenheit(0))
# print(gradosFahrenheit(10))
# print(gradosFahrenheit(20))
# print(gradosFahrenheit(32))
# print(gradosFahrenheit(48))
# print(gradosFahrenheit(100))
# print(gradosFahrenheit(20000))

# print(log(10))
# print(log10(10))

valor = int(input('Dame el primer valor: '))
valor2 = int(input('Dame el segundo valor: '))
valor = suma(valor, valor2)

print(valor)