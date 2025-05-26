class nodo:
    __equipo: object
    __sig: object
    def __init__(self, equipo):
        self.__equipo=equipo
        self.__sig=None
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    def getSiguiente(self):
        return self.__sig
    def getEquipo(self):
        return self.__equipo
    def setEquipo(self, equipo):
        self.__equipo=equipo