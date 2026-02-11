class Pokemon:
    def __init__(self, nombre, description, movimientos, tipos, stats):
        self.__nombre = nombre
        self.__description = description
        self.__movimientos = movimientos
        self.__tipos = tipos
        self.__stats = stats

    def __str__(self):
        return f"Descripción: {self.__description}\nMovimientos: {self.__movimientos}\nTipos: {self.__tipos}\nStats: {self.__stats}"

    def get_nombre(self):
        return self.__nombre
    def get_description(self):
        return self.__description
    def get_movimientos(self):
        return self.__movimientos
    def get_stats(self):
        return self.__stats
    def get_tipos(self):
        return self.__tipos

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_description(self, description):
        self.__description = description
    def set_movimientos(self, movimientos):
        self.__movimientos = movimientos
    def set_stats(self, stats):
        self.__stats = stats
    def set_tipos(self, tipos):
        self.__tipos = tipos