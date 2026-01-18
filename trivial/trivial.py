from os import path


preguntas = "preguntas.csv"
jugadores = "jugadores.csv"
jugadores_list = []
trivial = "trivial.py"
respuestas = ["a", "b", "c", "d"]
posiciones = [1, 2, 3, 4]

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
    fichero.close()


def registrarJugador():
    nombre = input("Introduce el nombre de usuario deseado: ")
    if not verificarExistencia(nombre):
        with open(jugadores, "a") as fichero:
            fichero.write(f"{nombre},0,0,0\n")
            jugadores_list.append([nombre, "0", "0", "0"])
    else:
        print("El jugador ya está registrado")
    iniciarSesion()
    fichero.close()


def verificarExistencia(nombre:str):
    encontrado = False
    with open(jugadores, "r", encoding="utf8") as fichero:
        jugador = fichero.readline()
        while jugador:
            if jugador.split(",")[0] == nombre:
                encontrado = True
            jugador = fichero.readline()
    fichero.close()
    return encontrado


def iniciarSesion():
    nombre = input("Inicia sesión escribiendo el nombre de usuario: ")
    if nombre == "ranking":
        if len(jugadores_list) != 0:
            verRanking()
        else:
            print("No hay jugadores que mostrar")
    else:
        if not verificarExistencia(nombre):
            print("El jugador no está registrado.")
        else:
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

def guardarDatos():
    with open(jugadores, "w", encoding="utf8") as old_jugadores:
        for jugador in jugadores_list:
            old_jugadores.write(f"{jugador[0]},{jugador[1]},{jugador[2]},{jugador[3]}\n")

def verRanking():
    ranking = sorted(jugadores_list, key=lambda jugador: int(jugador[2]), reverse=True)
    for jugador in ranking:
        print(f"{ranking.index(jugador) + 1}. {jugador[0]} ({jugador[2]} aciertos)")



def jugar(posicion:int):
    with open(preguntas, "r", encoding="utf8") as preguntas_list:
        for i in range(int(jugadores_list[posicion][1])):
            preguntas_list.readline()
        pregunta = preguntas_list.readline().strip("\n").split(",")
        respuesta = 0
        while pregunta[0] and respuesta != jugadores_list[posicion][0]:
            print(pregunta[0])
            for j in range(1, 5):
                print(f"{respuestas[j-1]}. {pregunta[j]}")
            respuesta = input("Introduzca la letra de la respuesta correcta: ").lower()
            while respuesta not in respuestas and respuesta != jugadores_list[posicion][0]:
                respuesta = input("Letra no válida. Inténtelo de nuevo: ")
            if respuesta in respuestas:
                if pregunta[respuestas.index(respuesta) + 1] == pregunta[len(pregunta)-1]:
                    print("Respuesta correcta!")
                    jugadores_list[posicion][2] = str(int(jugadores_list[posicion][2]) + 1)
                else:
                    print("Respuesta incorrecta!")
                    jugadores_list[posicion][3] = str(int(jugadores_list[posicion][3]) + 1)
                jugadores_list[posicion][1] = str(int(jugadores_list[posicion][1]) + 1)
            pregunta = preguntas_list.readline().strip("\n").split(",")
    preguntas_list.close()
    print(f"Tuviste {jugadores_list[posicion][2]} aciertos y {jugadores_list[posicion][3]} errores.")

recuperarJugadores()
menu()
guardarDatos()
