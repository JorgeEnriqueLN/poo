from abc import ABC, abstractmethod
import csv

class Plan (ABC):
    def __init__(self, nombre, duracion, cobertura, precio):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__cobertura = cobertura
        self.__precio = precio

    @abstractmethod
    def calcular_importe(self):
        pass

    def mostrar_datos(self):
        return (f"----------------------\nNombre de la compañía: {self.__nombre} \n"
                f"Duración: {self.__duracion} meses \n"
                f"Cobertura geográfica: {self.__cobertura}\n "
                f"Importe final: {self.calcular_importe()}")
    
    def getprecio(self):
        return self.__precio
    def getcobertura(self):
        return self.__cobertura
