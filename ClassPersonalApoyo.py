from ClassPersonal import Personal
porcentaje_por_categoria = 0.1
class PersonaApoyo(Personal):

    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria, carrera_dicta=None, cargo=None, catedra=None, area_investigacion=None,
                 tipo_investigacion=None):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra, categoria, area_investigacion, tipo_investigacion)
        self.__categoria = int(categoria)

    def mostrar(self):
        cadena = super().mostrar()
        cadena += f'Categoria:{self.__categoria}\n'
        return cadena

    def modificar_porcentaje_por_categoria(self, nuevo_porcentaje):
        global porcentaje_por_categoria
        porcentaje_por_categoria = nuevo_porcentaje

    def calcular_sueldo(self):
        sueldo = super().calcular_sueldo()
        if 1 <= int(self.__categoria) <= 10:
            porcentaje_por_categoria_actualizado = porcentaje_por_categoria
        elif 11 <= int(self.__categoria) <= 20:
            porcentaje_por_categoria_actualizado = porcentaje_por_categoria * 2
        elif 21 <= int(self.__categoria) <= 22:
            porcentaje_por_categoria_actualizado = porcentaje_por_categoria * 3
        sueldo_total = sueldo + (float(super().get_sueldo_basico()) * porcentaje_por_categoria_actualizado)
        return sueldo_total

    def diccionario(self):
        personal_dic = super().diccionario()
        personal_dic["categoria"] = self.__categoria
        return personal_dic
