from zope.interface import implementer
from ClassInterface import IDirector

@implementer(IDirector)
class Director:
    def __init__(self, lista):
        self.__listaAgentes = lista

    def modificarBasico(self, cuil, nuevoBasico):
        agente = self.__listaAgentes.buscar_por_cuil(cuil)
        if agente:
            agente.set_sueldo_basico(nuevoBasico)
        else:
            print(f'El Agente con cuil {cuil} no se encuentra en la lista.')

    def modificarPorcentajeporcargo(self, cuil, nuevoPorcentaje):
        agente = self.__listaAgentes.buscar_por_cuil(cuil)
        if agente:
            agente.modificar_porcentaje_por_cargo(nuevoPorcentaje)
        else:
            print(f'El Agente con cuil {cuil} no se encuentra en la lista.')

    def modificarPorcentajeporcategoria(self, cuil, nuevoPorcentaje):
        agente = self.__listaAgentes.buscar_por_cuil(cuil)
        if agente:
            agente.modificar_porcentaje_por_categoria(nuevoPorcentaje)
        else:
            print(f'El Agente con cuil {cuil} no se encuentra en la lista.')

    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        agente = self.__listaAgentes.buscar_por_cuil(cuil)
        if agente:
            agente.modificar_importeExtra(nuevoImporteExtra)
        else:
            print(f'El Agente con cuil {cuil} no se encuentra en la lista.')
