class Personal:

    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta='', cargo='', catedra='',
                 categoria='', area_investigacion='', tipo_investigacion=''):
        self.__cuil = int(cuil)
        self.__apellido = str(apellido)
        self.__nombre = str(nombre)
        self.__sueldo_basico = float(sueldo_basico)
        self.__antiguedad = int(antiguedad)

    def mostrar(self):
        cadena = f'Cuil:{self.__cuil}\n'
        cadena += f'Apellido:{self.__apellido}\n'
        cadena += f'Nombre:{self.__nombre}\n'
        cadena += f'sueldo basico:{self.__sueldo_basico}\n'
        cadena += f'antiguedad:{self.__antiguedad}\n'
        return cadena

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_sueldo_basico(self):
        return self.__sueldo_basico

    def get_antiguedad(self):
        return self.__antiguedad

    def get_cuil(self):
        return self.__cuil

    def set_sueldo_basico(self, nuevo_sueldo):
        self.__sueldo_basico = nuevo_sueldo

    def calcular_sueldo(self):
        porcentaje_anios = self.__antiguedad * 0.01
        sueldo = self.__sueldo_basico + (self.__sueldo_basico * porcentaje_anios)
        return sueldo

    def diccionario(self):
        return {
            "cuil": self.__cuil,
            "apellido": self.__apellido,
            "nombre": self.__nombre,
            "sueldo_basico": self.__sueldo_basico,
            "antiguedad": self.__antiguedad
        }
