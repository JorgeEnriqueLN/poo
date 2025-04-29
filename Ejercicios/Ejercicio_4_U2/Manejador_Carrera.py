import csv
from Carrera import Carrera 
import numpy as np
class ManejadorC:
    __cantidad: int
    __dimension: int
    __incremento = 1
    __ArreC :np.array

    def _init_(self, dimension, incremento=1):
        self.__ArreC = np.empty(dimension, dtype=Carrera)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarCarrera(self, unaCarrera):
        if self._cantidad==self._dimension:
            self._dimension+=self._incremento
            self._ArreC.resize(self._dimension)
        self._ArreC[self._cantidad]=unaCarrera
        self.__cantidad += 1
    def cargar_Carrera(self):
        saltear = False
        with open("Carreras.csv") as archivoCarrera:
            reader = csv.reader(archivoCarrera, delimiter= ';') 
            for carr in archivoCarrera:
                if not saltear:
                 saltear= True
                else:
                    unacarr= Carrera (int(carr[0]), carr[1], carr[2], carr[3], carr[4], int(carr[5]))
                    self.agregarCarrera(unacarr)
        archivoCarrera.close()
        
    def BuscarCarera(self,nombre):
        pass