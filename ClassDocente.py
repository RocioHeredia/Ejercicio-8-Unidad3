from ClassPersonal import Personal
porcentaje_por_cargo = 0.1 #valor inicial del porcentaje
class Docente(Personal):

    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra, categoria=None, area_investigacion=None,
                 tipo_investigacion=None):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra, categoria, area_investigacion, tipo_investigacion)
        self.__carrera_dicta = str(carrera_dicta)
        self.__cargo = str(cargo)
        self.__catedra = str(catedra)

    def mostrar(self):
        cadena = super().mostrar()
        cadena += f'Carrera que Dicta:{self.__carrera_dicta}\n'
        cadena += f'Cargo:{self.__cargo}\n'
        cadena += f'Catedra:{self.__catedra}\n'
        return cadena

    def get_carrera(self):
        return self.__carrera_dicta

    def modificar_porcentaje_por_cargo(self, nuevo_porcentaje):
        global porcentaje_por_cargo
        porcentaje_por_cargo = nuevo_porcentaje

    def calcular_sueldo(self):
        sueldo = super().calcular_sueldo()
        if str(self.__cargo) == 'simple':
            porcentaje_por_cargo_actualizado = porcentaje_por_cargo
        elif str(self.__cargo) == 'semiexclusivo':
            porcentaje_por_cargo_actualizado = porcentaje_por_cargo * 2
        elif str(self.__cargo) == 'exclusivo':
            porcentaje_por_cargo_actualizado = porcentaje_por_cargo * 5
        sueldo_total = sueldo + (float(super().get_sueldo_basico()) * porcentaje_por_cargo_actualizado)

        return sueldo_total

    def diccionario(self):
        personal_dic = super().diccionario()
        personal_dic["carrera"] = self.__carrera_dicta
        personal_dic["cargo"] = self.__cargo
        personal_dic["catedra"] = self.__catedra
        return personal_dic
