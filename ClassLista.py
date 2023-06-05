import json
from pathlib import Path
from ClassNodo import Nodo
from ClassDocente import Docente
from ClassInvestigador import Investigador
from ClassDocenteInvestigador import DocenteInvestigador
from ClassPersonalApoyo import PersonaApoyo


class ListaPersonal:
    def __init__(self):
        self.__cabeza = None

    def agregarPersonal(self, personal):
        nuevo_nodo = Nodo(personal)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
        else:
            actual = self.__cabeza
            while actual.get_siguiente() is not None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo_nodo)

    def LeerArchivoJson(self):
        with Path('personal.json').open(encoding='utf-8-sig') as fuente:
            diccionario = json.load(fuente)
        for personal_data in diccionario:
            if personal_data["tipo_personal"] == "Docente":
                personal = Docente(personal_data["cuil"],
                                   personal_data["apellido"],
                                   personal_data["nombre"],
                                   personal_data["sueldo_basico"],
                                   personal_data["antiguedad"],
                                   personal_data["carrera"],
                                   personal_data["cargo"],
                                   personal_data["catedra"])
            elif personal_data["tipo_personal"] == "Investigador":
                personal = Investigador(personal_data["cuil"],
                                        personal_data["apellido"],
                                        personal_data["nombre"],
                                        personal_data["sueldo_basico"],
                                        personal_data["antiguedad"],
                                        personal_data["area_investigacion"],
                                        personal_data["tipo_investigacion"])
            elif personal_data["tipo_personal"] == "Personal_Apoyo":
                personal = PersonaApoyo(personal_data["cuil"],
                                        personal_data["apellido"],
                                        personal_data["nombre"],
                                        personal_data["sueldo_basico"],
                                        personal_data["antiguedad"],
                                        personal_data["categoria"])

            elif personal_data["tipo_personal"] == "Docente_Investigador":
                personal = DocenteInvestigador(personal_data["cuil"],
                                               personal_data["apellido"],
                                               personal_data["nombre"],
                                               personal_data["sueldo_basico"],
                                               personal_data["antiguedad"],
                                               personal_data["carrera"],
                                               personal_data["cargo"],
                                               personal_data["catedra"],
                                               personal_data["area_investigacion"],
                                               personal_data["tipo_investigacion"],
                                               personal_data["categoria_incentivos"],
                                               personal_data["importe_extra"])
            else:
                print('NO HAY PERSONAL EN EL ARCHIVO.')
            self.agregarPersonal(personal)

    def mostrar_datos(self):
        actual = self.__cabeza
        while actual is not None:
            personal = actual.get_dato()
            print(personal.mostrar())
            actual = actual.get_siguiente()

    def insertarPersonal(self, agente, posicion):
        nuevo_nodo = Nodo(agente)
        if posicion == 0:
            nuevo_nodo.set_siguiente(self.__cabeza)
            self.__cabeza = nuevo_nodo
        else:
            aux = self.__cabeza
            cont = 0
            while aux is not None and cont < posicion - 1:
                aux = aux.get_siguiente()
                cont += 1
            nuevo_nodo.set_siguiente(aux.get_siguiente())
            aux.set_siguiente(nuevo_nodo)
            print('Agente insertado en la posicion deseada.')

    def mostrar_tipo(self, posicion):
        actual = self.__cabeza
        indice = 0

        while actual is not None and indice < posicion:
            actual = actual.get_siguiente()
            indice += 1
        if actual is None:
            print(f'La posicion {posicion} esta fuera de rango.')

        else:
            personal = actual.get_dato()

            if isinstance(personal, Docente):
                print(f'El objeto en la posicion {posicion} es un Docente.')
            elif isinstance(personal, Investigador):
                print(f'El objeto en la posicion {posicion} es un Investigador.')
            elif isinstance(personal, PersonaApoyo):
                print(f'El objeto en la posicion {posicion} es un Personal Apoyo.')
            elif isinstance(personal, DocenteInvestigador):
                print(f'El objeto en la posicion {posicion} es un Docente Investigador.')

    def ordenar_por_nombre(self):
        if self.__cabeza is None:
            return
        actual = self.__cabeza
        while actual.get_siguiente() is not None:
            siguiente = actual.get_siguiente()
            while siguiente is not None:
                if str(siguiente.get_dato().get_nombre()) < str(actual.get_dato().get_nombre()):
                    aux = actual.get_dato()
                    actual.set_dato(siguiente.get_dato())
                    siguiente.set_dato(aux)
                siguiente = siguiente.get_siguiente()
            actual = actual.get_siguiente()

    def listado_ordenado(self, nombre_carrera):
        self.ordenar_por_nombre()
        actual = self.__cabeza
        print(f'\n LISTADO ORDENADO POR NOMBRE DE LA CARRERA {nombre_carrera}:')
        while actual is not None:
            if isinstance(actual.get_dato(), DocenteInvestigador):
                if str(actual.get_dato().get_carrera()) == nombre_carrera:
                    personal = actual.get_dato().mostrar()
                    print(personal)
                else:
                    print('No hay Docentes Investigadores en esta Carrera.')
            actual = actual.get_siguiente()

    def contarDocenteInEInvestigadores(self, area):
        actual = self.__cabeza
        cont_D = 0
        cont_I = 0
        while actual is not None:
            if isinstance(actual.get_dato(), DocenteInvestigador):
                if str(actual.get_dato().get_area()) == area:
                    cont_D += 1
            if isinstance(actual.get_dato(), Investigador):
                if str(actual.get_dato().get_area()) == area:
                    cont_I += 1
            actual = actual.get_siguiente()

        print(f'Los docentes Investigadores en el area {area} son: {cont_D}')
        print(f'Los Investigadores en el area {area} son: {cont_I}')

    def ordenas_por_apellido(self):
        if self.__cabeza is None:
            return
        actual = self.__cabeza
        while actual.get_siguiente() is not None:
            siguiente = actual.get_siguiente()
            while siguiente is not None:
                if str(siguiente.get_dato().get_apellido()) < str(actual.get_dato().get_apellido()):
                    aux = actual.get_dato()
                    actual.set_dato(siguiente.get_dato())
                    siguiente.set_dato(aux)
                siguiente = siguiente.get_siguiente()
            actual = actual.get_siguiente()

    def obtener_tipo(self, agente):
        if isinstance(agente, DocenteInvestigador):
            retorna = 'Docente Investigador'
        elif isinstance(agente, Docente):
            retorna = 'Docente'
        elif isinstance(agente, Investigador):
            retorna = 'Investigador'
        elif isinstance(agente, PersonaApoyo):
            retorna = 'Persona Apoyo'
        else:
            retorna = None
        return retorna

    def generar_listado(self, ):
        self.ordenas_por_apellido()
        actual = self.__cabeza
        while actual is not None:
            agente = actual.get_dato()
            tipo_agente = self.obtener_tipo(agente)
            print(f'{agente.get_nombre()}, {agente.get_apellido()} Tipo de Agente: {tipo_agente} Sueldo: $ {agente.calcular_sueldo()}')
            actual = actual.get_siguiente()

    def listado_por_categoria(self, categoria):
        actual = self.__cabeza
        importe_total= 0
        while actual is not None:
            personal = actual.get_dato()
            if isinstance(personal, DocenteInvestigador) and str(personal.get_categoriaprog()) == categoria:
                nombre = personal.get_nombre()
                apellido = personal.get_apellido()
                importe_extra = personal.get_importeextra()
                print(f'Apellido:{apellido}  Nombre:{nombre}  Importe Extra: ${importe_extra}')
                importe_total += importe_extra
            actual = actual.get_siguiente()
        print(f'Total a solicitar al Ministerio en concepto de importe extra: ${importe_total}')

    def buscar_por_cuil(self, cuil):
        actual = self.__cabeza
        while actual is not None:
            agente = actual.get_dato()
            if isinstance(agente, DocenteInvestigador) and str(agente.get_cuil()) == cuil:
                retorna = agente
            elif isinstance(agente, Docente) and str(agente.get_cuil()) == cuil:
                retorna = agente
            elif isinstance(agente, PersonaApoyo) and str(agente.get_cuil()) == cuil:
                retorna = agente
            elif isinstance(agente, Investigador) and str(agente.get_cuil()) == cuil:
                retorna = agente

            actual = actual.get_siguiente()
        return retorna

    def GuardarEnArchivoJson(self):
        personal_lista = []
        actual = self.__cabeza
        while actual is not None:
            personal = actual.get_dato()
            personal_dic = personal.diccionario()
            if isinstance(personal, DocenteInvestigador):
                personal_dic = {"tipo_personal": "Docente_Investigador", **personal_dic}
            elif isinstance(personal, Investigador):
                personal_dic = {"tipo_personal": "Investigador", **personal_dic}
            elif isinstance(personal, Docente):
                personal_dic = {"tipo_personal": "Docente", **personal_dic}
            elif isinstance(personal, PersonaApoyo):
                personal_dic = {"tipo_personal": "Personal_Apoyo", **personal_dic}

            personal_lista.append(personal_dic)
            actual = actual.get_siguiente()
        with Path('personal.json').open('w', encoding='utf-8-sig') as archivo:
            json.dump(personal_lista, archivo, indent=4)
            archivo.close()


