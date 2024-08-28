n = int(input("Ingresar un número entre 0 y 20: "))
fact = 1
for a in range(1, n+1):
    fact *= a
print (f"El fatorial de {n} es: {fact}")