from ClassPersonal import Personal

class Investigador(Personal):

    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion, carrera_dicta=None, cargo=None, catedra=None, categoria=None):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra, categoria, area_investigacion, tipo_investigacion)
        self.__area_investigacion = str(area_investigacion)
        self.__tipo_investigacion = str(tipo_investigacion)

    def mostrar(self):
        cadena = super().mostrar()
        cadena += f'Area de Investigacion:{self.__area_investigacion}\n'
        cadena += f'Tipo de Investigacion:{self.__tipo_investigacion}\n'
        return cadena

    def get_area(self):
        return self.__area_investigacion

    def calcular_sueldo(self):
        sueldo_total = super().calcular_sueldo()
        return sueldo_total

    def diccionario(self):
        personal_dic = super().diccionario()
        personal_dic["area_investigacion"] = self.__area_investigacion
        personal_dic["tipo_investigacion"] = self.__tipo_investigacion
        return personal_dic