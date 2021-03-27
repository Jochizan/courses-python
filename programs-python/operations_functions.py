def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):

    try:
        return num1 / num2
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"

try:
    op1 = int(input("Ingrese el primer número: "))
    op2 = int(input("Ingrese el segundo número: "))

except ValueError:
    print("Solo ingrese un número")
    exit()

operación = input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

if operación == "suma":
    print(suma(op1, op2))

elif operación == "resta":
    print(resta(op1, op2))

elif operación == "multiplica":
    print(multiplica(op1, op2))

elif operación == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. A continuación el termino de ejecución del programa ")