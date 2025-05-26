import abc
from abc import ABC

class equipo(ABC):
    __marca: str
    __modelo: str
    __anio: int
    __tipoCom: str
    __potencia: str
    __capacidad: int
    __tarifa: float
    __dias: int
    def __init__(self, mar, mod, anio, tipo, pote, cap=0, tar=0, dias=0):
        self.__marca=mar
        self.__modelo=mod
        self.__anio=anio
        self.__tipoCom=tipo
        self.__potencia=pote
        self.__capacidad=cap
        self.__tarifa=tar
        self.__dias=dias
    @abc.abstractmethod  
    def tarifa(self):
        pass
    def getAnio(self):
        return self.__anio
    def getCap(self):
        return self.__capacidad
    def getTarifa(self):
        return self.__tarifa
    def getDias(self):
        return self.__dias
    def mostrar(self):
        print(f"-------\nMarca: {self.__marca}\nModelo: {self.__modelo}\nAnio: {self.__anio}\nCombustible: {self.__tipoCom}\nPotencia: {self.__potencia}\nCapacidad: {self.__capacidad}\nTarifa: {self.tarifa()}\n")

