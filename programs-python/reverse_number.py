N = int(input("Ingrese el número a invertir: "))
resto = 0
NInver = 0

while (N != 0):
    
    resto = N % 10
    NInver = NInver*10 + resto
    N = N // 10

print("El número invertido es: " + str(NInver))