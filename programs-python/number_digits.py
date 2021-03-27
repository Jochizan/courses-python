N = int(input("Ingrese el número: "))
n = 0

while(N != 0):
    n = n + 1
    N = N//10

print("La cantida de cifras del número es: " + str(n))