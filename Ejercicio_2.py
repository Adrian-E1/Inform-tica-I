n= int(input("Ingrese el número de notas: "))
suma = 0
contador = 0
while contador < n:
    n1= float(input("Ingrese la nota: "))
    suma += n1
    contador += 1
print(f"El promedio de las notas es {suma/n}")