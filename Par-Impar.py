#Par o Impar

x = int(input("Ingrese un numero entre 1 y 1000: "))

if (x >= 1 and x < 1001):
    if (x % 2 == 0):
        print(x, "es un numero par")
    else:
        print(x, "es un numero impar")
else:
    print(x, "no es un numero entre 1 y 1000")