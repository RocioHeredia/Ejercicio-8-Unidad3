from ClassDocente import Docente
from ClassInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra,
                 area_investigacion, tipo_investigacion, categoria_prog, importe_extra):
        Docente.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        self.__categoria_prog = str(categoria_prog)
        self.__importe_extra = float(importe_extra)

    def mostrar(self):
        cadena = super().mostrar()
        cadena += f'Categoria del Programa:{self.__categoria_prog}\n'
        cadena += f'Importe Extra por docencia:{self.__importe_extra}\n'
        return cadena

    def get_carrera(self):
        cadena = super().get_carrera()
        return cadena

    def get_area(self):
        cadena = super().get_area()
        return cadena

    def get_importeextra(self):
        return self.__importe_extra

    def get_categoriaprog(self):
        return self.__categoria_prog

    def modificar_porcentaje_por_categoria(self, nuevoImporteExtra):
        self.__importe_extra = nuevoImporteExtra

    def calcular_sueldo(self):
        sueldo_docente = Docente.calcular_sueldo(self)
        sueldo_total = sueldo_docente + self.__importe_extra
        return sueldo_total

    def diccionario(self):
        personal_dic = super().diccionario()
        personal_dic["categoria_incentivos"] = self.__categoria_prog
        personal_dic["importe_extra"] = self.__importe_extra
        return personal_dic
