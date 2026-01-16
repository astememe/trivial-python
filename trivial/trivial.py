from os import path

jugadores = "jugadores.csv"
jugadores_list = []
trivial = "trivial.py"

if not path.exists(jugadores):
    open(jugadores, "x")
else:
    pass
if not path.exists(trivial):
    open(trivial, "x")
else:
    pass


def recuperarJugadores():
    with open(jugadores, "r") as fichero:
        jugador = fichero.readline()
        while jugador:
            jugador = jugador.strip("\n")
            jugadores_list.append(jugador.split(","))
            jugador = fichero.readline()


def registrarJugador():
    nombre = input("Introduce el nombre de usuario deseado: ")
    if not verificarExistencia(nombre):
        with open(jugadores, "a") as fichero:
            fichero.write(f"{nombre},0,0,0\n")
            jugadores_list.append([nombre, "0", "0", "0"])
    else:
        print("El jugador ya está registrado")
    iniciarSesion()


def verificarExistencia(nombre:str):
    encontrado = False
    with open(jugadores, "r") as fichero:
        jugador = fichero.readline()
        while jugador:
            if jugador.split(",")[0] == nombre:
                encontrado = True
            jugador = fichero.readline()
    return encontrado


def iniciarSesion():
    nombre = input("Inicia sesión escribiendo el nombre de usuario: ")
    posicion = 0
    for i in range(len(jugadores_list)):
        if nombre in jugadores_list[i]:
            posicion = i
    jugar(posicion)

def menu():
    print("BIENVENIDO\nEscoja una opción:\n1. Iniciar Sesión\n2. Registrarse\n3. Salir")
    valido = False
    opcion = int(input("Escoja opción: "))
    while not valido:
        try:
            if opcion != 1 and opcion != 2 and opcion != 3:
                raise ValueError("Opción no válida.")
            else:
                valido = True
        except ValueError as e:
            print(e)
            opcion = int(input("Introduzca de nuevo la opción: "))
    if opcion == 1:
        iniciarSesion()
    elif opcion == 2:
        registrarJugador()
    else:
        pass


recuperarJugadores()
def jugar(posicion:int):
    print(posicion)
    print(jugadores_list[posicion])

menu()