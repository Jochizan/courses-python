def GenerarPares(limite):

    num = 1

    while num<limite:

        yield num*2

        num = num + 1

devuelvePares = GenerarPares(10)

print(next(devuelvePares))

print("Aquí podría habe más código...")

print(next(devuelvePares))

print("Aquí podría haber más código...")

print(next(devuelvePares))