import csv
from Facultad import Facultad
import numpy as np
class ManejadorF:
    __cantidad: int
    __dimension: int
    __incremento = 1
    __ArreF :np.array


    def _init_(self, dimension, incremento=1):
        self.__ArreF = np.empty(dimension, dtype=Facultad)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarFacultad(self, unaFacultad):
        if self._cantidad==self._dimension:
            self._dimension+=self._incremento
            self._ArreF.resize(self._dimension)
        self._ArreF[self._cantidad]=unaFacultad
        self.__cantidad += 1
    def cargarFacultades(self):
        saltear = False
        with open("Facultades.csv") as archivoFacultad:
            reader = csv.read(archivoFacultad, delimiter = ";")
        for Fac in archivoFacultad:
            if not saltear:
                saltear = True
            else:
                unaFacultad=Facultad(int(Fac[0]),Fac[1],Fac[2],Fac[3],Fac[4])
                self.agregarFacultad(unaFacultad)
        archivoFacultad.close()
    def MostrarFac(self):
        pass
    def BuscarFacu(self,nomFac):
        pass