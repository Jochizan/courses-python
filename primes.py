def primes(n):
    if n == 1:
        return False
    m = int(n / 2)
    for i in range(2, m):
        if n % i == 0:
            return False
    return True

num = int(input('Ingrese el número a evaluar: '))
ok = primes(num)

if ok:
    print('Es primo')
else:
    print('No es primo')
