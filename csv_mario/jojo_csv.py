import os.path

fichero = "jojo_stands.csv"
stats = ["FUERZA", "VELOCIDAD", "ALCANCE", "STAMINA", "PRECISIÓN", "POTENCIAL"]
posible_stat = ["A", "B", "C", "D", "E", "-", "?"]

if os.path.exists(fichero):
    pass
else:
    open(fichero, "x")

def addrow(fichero):
    datos_array = createdatos()
    if not verificarexistencia(datos_array):
        datos = ""
        for i in range(len(datos_array) - 1):
            datos += datos_array[i] + ","
        datos += datos_array[-1]
        with open(fichero, "a") as f:
            f.write(datos)
            f.write("\n")
    else:
        print(f"{datos_array[0]} ya existe.")

def createdatos():
    datos_array = []
    nombre_stand = input("Introduce el nombre del stand: ")
    datos_array.append(nombre_stand)
    i = 0
    while i < len(stats):
        stat = input(f"Introduce {stats[i]} de {nombre_stand}: ").upper()
        try:
            if stat not in posible_stat or int(stat):
                print("La stat debe ser una letra de la A a la E o '-' o '?' si no se aplica.")
        except ValueError:
            datos_array.append(stat.upper())
            i += 1
    return datos_array

def verificarexistencia(datos):
    existe = False
    with open(fichero, "r") as f:
        linea = f.readline()
        while linea:
            if linea.split(",")[0] == datos[0]:
                existe = True
            linea = f.readline()
    return existe

def sacar_sobresalientes(fichero):
    stat = input("Introduzca la stat para ver los stands que tienen una 'A' en ella: ").upper()
    with open(fichero, "r") as f:
        linea = f.readline()
        while linea:
            try:
                if linea.split(",")[stats.index(stat) + 1] == "A":
                    print(linea.split(",")[0])
                linea = f.readline()
            except ValueError:
                stat = input("Stat no válida. Vuelva a introducirla: ").upper()
sacar_sobresalientes(fichero)

def menu():
    print("1. Añadir fila\n2. Sacar las filas con una stat a elegir en 'A'")
    opcion = int(input("Introduzca la opción que desea"))
    if opcion == 1:
        createdatos()
    else:
        sacar_sobresalientes(fichero)

print(stats)