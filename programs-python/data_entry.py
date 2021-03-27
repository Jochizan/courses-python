nombre = input("Introduzca su nombre: ")
num_int = int(input("Ingrese un número entero: "))
num_float = float(input("Ingrese un número flotante: "))
num_compless = complex(input("Ingrese un número complejo: "))

print("String: ", nombre)
print("Entero: ", num_int)
print("Flotante: ", num_float)
print("Complejo: ", num_compless)
num_compless = num_compless + 1

print(str(num_compless))