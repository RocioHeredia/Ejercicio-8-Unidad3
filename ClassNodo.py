from ClassPersonal import Personal
class Nodo:
    __dato = Personal
    __sig = object

    def __init__(self, personal):
        self.__dato = personal
        self.__sig = None

    def get_siguiente(self):
        return self.__sig

    def set_siguiente(self, siguiente):
        self.__sig = siguiente

    def set_dato(self, dato):
        self.__dato = dato

    def get_dato(self):
        return self.__dato
