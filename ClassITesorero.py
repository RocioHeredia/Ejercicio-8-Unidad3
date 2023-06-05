from ClassInterface import ITesorero
from zope.interface import implementer

@implementer(ITesorero)
class Tesorero:

    def __init__(self, lista):
        self.__listaAgentes = lista

    def gastosSueldosPorEmpleado(self, cuil):
        agente = self.__listaAgentes.buscar_por_cuil(cuil)
        if agente:
            retorna = agente.calcular_sueldo()
        else:
            retorna = None

        return retorna