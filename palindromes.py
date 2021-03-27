s = input('Ingrese una palabra a evaluar: ')
s = s.replace(' ', '')
s = s.lower()
tmp = s[::-1]
if tmp == s:
    print("Es palindromo")
else:
    print("No es palindromo")
