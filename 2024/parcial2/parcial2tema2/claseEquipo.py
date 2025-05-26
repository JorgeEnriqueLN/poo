from abc import ABC, abstractmethod

class Equipo (ABC):
    def __init__(self, tipo, marca, modelo, anioDeFabricacion, tipoDeCombustible, potencia, capacidadDeCarga, tarifaAlquilerDiario, cantidadDiasAlquiler) -> None:
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__anioDeFabricacion = anioDeFabricacion
        self.__tipoDeCombustible = tipoDeCombustible
        self.__potencia = potencia
        self.__capacidadDeCarga = capacidadDeCarga
        self.__tarifaAlquilerDiario = tarifaAlquilerDiario
        self.__cantidadDiasAlquiler = cantidadDiasAlquiler
    @abstractmethod    

    def calcular_precio (self):
        pass

    def gettipo (self):
       return self.__tipo
    def getmarca(self):
      return self.__marca
    def getmodelo(self):
      return self.__modelo
    def getanioDeFabricacion(self):
      return self.__anioDeFabricacion
    def gettipoDeCombustible(self):
      return self.__tipoDeCombustible
    def getpotencia(self):
      return self.__potencia
    def getcapacidadDeCarga(self):
      return self.__capacidadDeCarga
    def gettarifaAlquilerDiario(self):
      return self.__tarifaAlquilerDiario
    def getcantidadDiasAlquiler(self):
      return self.__cantidadDiasAlquiler
    
    # def getmarca(self):
    #   pass
    # def getmodelo(self):
    #   pass
    # def getañoDeFabricacion(self):
    #   pass
    # def gettipoDeCombustible(self):
    #   pass
    # def getpotencia(self):
    #   pass
    # def getcapacidadDeCarga(self):
    #   pass
    # def gettarifaAlquilerDiario(self):
    #   pass
    # def getcantidadDiasAlquiler(self):
    #   pass
   