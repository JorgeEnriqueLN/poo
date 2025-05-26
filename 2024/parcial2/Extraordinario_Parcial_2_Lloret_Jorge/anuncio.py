from abc import ABC, abstractmethod


class Anuncio(ABC):
   
    def __init__(self, titulo, duracion, fecha_creacion, costo, formato):
        self.__titulo = titulo
        self.__duracion = int(duracion)
        self.__fecha_creacion = fecha_creacion
        self.__costo = float(costo)
        self.__formato = formato
    
    @abstractmethod
    def calcular_costo_total(self):
        pass
    
    def mostrar_info(self):
        print(f'Título: {self.__titulo} \t\t Duración: {self.__duracion} \t\t Costo Total: {self.calcular_costo_total()}')

    def getcosto (self):
        return self.__costo
    
    def getduracion (self):
        return self.__duracion
    
    def gettitulo (self):
        return self.__titulo
    
    def getformato (self):
        return self.__formato
    