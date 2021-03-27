num = int(input("Ingrese el número en base 10: "))
base = int(input("Ingrese la base a la que se le llevara: "))
num_trans = ""
num_inv = ""
resto = 0

if num > 0:
    if base > 1:

        while (num != 0):

            if(num%base == 0):

                num_trans += str(0)

            elif(num%base != 0):

                num_trans += str(num%base)

            num = num // base
    
    else:
        print("Solo ingrese una base mayor a 1")
else:
    print("Solo ingrese un número mayor a 0")

a = len(num_trans)
while (a != 0):

    num_inv += num_trans[a-1:a]
    a = a - 1

print("El resultado de llevar el número " + str(num) + "a la base " + str(base) + "es:\n" + str(num_inv))