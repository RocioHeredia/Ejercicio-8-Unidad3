from zope.interface import Interface
class ITesorero(Interface):

    def gastosSueldosPorEmpleado(self, dni):
        pass

class IDirector (Interface):

    def modificarBasico(self, dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass
