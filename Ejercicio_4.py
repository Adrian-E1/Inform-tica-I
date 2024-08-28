N = int(input("Ingresar un número: "))
suma = 0
cont = 1
while cont <= N:
    if cont % 2 != 0:
        suma += cont
    cont += 1
print(f"La suma es: {suma}")    