
listaperros = []
listagatos = []
contperros = 0
contgatos = 0

bienvenida = "Bienvenidos al sistema de la clinica veterinaria UdeA"
print(f"{bienvenida:>90}")

while True:
    menu = int(input("""Ingrese: \n
                     \r1- Ingresar nuevo cliente
                     \r2- Ver cantidad de pacientes
                     \r3- Mostrar promedio de edades
                     \r4- Cantidad de pacientes criticos y graves
                     \r5- Ver paciente
                     \r6- Ver todos los pacientes
                     \r7- Salir \n"""))
    if menu == 1:
        mas = []
        mas.append(input("Nombre de la mascota:\n"))
        tipo = int(input("Ingrese: \n0 - Si es perro\n1 - Si es gato\n"))
        if tipo == 0:
            mas.append("Perro")
        else:
            mas.append("Gato")
        mas.append(float(input("Edad de la mascota: ")))
        estado = (int(input("Ingrese: \no- Si es grave\n1 - Si es critico\n")))
        if estado ==0:
            mas.append("Grave")
        else:
            mas.append("Critico")
        if tipo == 0:
            contperros += 1
            codigo = "Canino{:03d}".format(contperros)
            mas.append(codigo)
            listaperros.append(mas)
        elif tipo == 1:
            contgatos += 1
            codigo = "Felinos{:03d}".format(contgatos)
            mas.append(codigo)
            listagatos.append(mas)
        else:
            print("Ingrese el valor correcto, es 1 o 0")
            continue
    elif menu == 2:
        cantidad = int(input("Ingrese para ver: \n1 - Cantidad de perros \n2 - Cantidad de gatos \n3 - Cantidad total de animales\n"))
        if cantidad == 1:
            print=("\nHay %d perros en el sistema \n" % len(listaperros))
        elif cantidad == 2:
            print("\nHay %d gatos en el sistema \n" % len(listagatos))
        elif cantidad == 3:
            print("\nHay %d animales en el sistema \n" % (len(listaperros) + len(listagatos)))
        else:
            print("Ingrese valor correcto, es 0, 1 o 2")
            continue
    elif menu == 3:
        ages = []
        for i in listagatos:
            ages.append(i[2])
        for i in listaperros:
            ages.append(i[2])
        print(f"El promedio de edades es : {sum(ages)/len(ages): .2f}")
    elif menu == 4:
        cantidadgraves = 0
        cantidadcriticos = 0
        for i in listagatos:
            if i[3] == "Grave":
                cantidadgraves += 1
            elif i[3] == "Critico":
                cantidadcriticos += 1
        for i in listaperros:
            if i[3] == "Grave":
                cantidadgraves += 1
            else:
                cantidadcriticos += 1
        print(f"Hay {cantidadgraves} de pacientes graves y {cantidadcriticos} de pacientes criticos en el sistema")
    elif menu ==5:
        cod = (input("Ingrese codigo del animal que desea buscar")).capitalize
        if cod.startswith("Fe"):
            for i in listagatos:
                if i[4] == cod:
                    print(f"Nombre: {i[0]} \nTipo: {i[1]} \nEdad: {i[2]} \nEstado: {i[3]} \nCodigo: {i[4]}")
        elif cod.startswith("Ca"):
            for i in listaperros:
                if i[4] == cod:
                    print(f"Nombre: {i[0]} \nTipo: {i[1]} \nEdad: {i[2]} \nEstado: {i[3]} \nCodigo: {i[4]}")
    elif menu == 6:
        listatotal= listaperros+listagatos
        print("--------------------")
        for i in listatotal:
            print(f"Nombre: {i[0]} \nTipo: {i[1]} \nEdad: {i[2]} \nEstado: {i[3]} \nCodigo: {i[4]}")
    elif menu == 7:
        fallos = 0
        while fallos < 3:
            submenu = input("\n1 - Aceptar✅ \n2 - Rechazar❌")
            if submenu == 1:
                break
            elif submenu == 2:
                break
            else:
                fallos += 1
                print("Ingrese la opción correcta...\n")
        if submenu == 1:
            break
        if submenu == 2 or submenu != 1:
            continue
