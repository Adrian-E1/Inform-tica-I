n = int(input("Ingresar un número del 1 al 9: "))
x = int(input("Ingresar un número del 1 al 9: "))
a = 0
for a in range (1, 10):
    print(f"{a}^{x} es: {a**x}")
    a += 1