class Jugador:
    def __init__(self, nombre:str):
        self.__nombre = nombre
        self.__r_correctas = 0
        self.__r_incorrectas = 0
        self.__progreso = self.__r_incorrectas + self.__r_correctas


    def add_correcta(self):
        self.__r_correctas += 1

    def add_incorrrecta(self):
        self.__r_incorrectas += 1

    def get_progreso(self):
        return self.__progreso

    def get_respuestas(self):
        return self.__r_correctas, self.__r_incorrectas