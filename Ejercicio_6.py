a = int(input("Ingrese un número entero: "))
n = int(input("Ingrese cantidad de sumas: "))
i = 1
suma = 0
while i <= n:
    suma += (1/a)**i
    i += 1
print(f"La sumatoria con n={n} y a={a} es: {suma}")