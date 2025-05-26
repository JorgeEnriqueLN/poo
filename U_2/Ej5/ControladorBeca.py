import numpy as np
from Beca import *
import os
import csv
class ControladorBeca:
    __becas : np.ndarray
    __dimension: int
    __cantidad : int
    def __init__(self,dimension):
        self.__becas = np.empty(dimension, dtype=Beca)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def getBecas(self):
        return self.__becas
    
    # def cargarArchivo(self):
        
    #     ruta_actual = os.path.dirname(os.path.abspath(__file__))
    #     ruta_csv = os.path.join(ruta_actual, "Carreras.csv")
    #     archivo = open(ruta_csv,"r")
    #     reader = csv.reader(archivo,delimiter=';')
    #     next(reader)
    
    #     for fila in reader:
    #         carrera = Carrera(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
    #         self.agregar(carrera)
    #     archivo.close()
    # def agregar(self,carrera):
    #     if self.__cantidad < self.__dimension:
    #         self.__carreras[self.__cantidad] = carrera
    #         self.__cantidad += 1
    #     else:
    #         print("No hay mas espacio")
    def agregar(self,beca):
        if self.__cantidad < self.__dimension:
            self.__becas[self.__cantidad] = beca
            self.__cantidad += 1
        else:
            print("No hay mas espacio")
    def cargar(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_csv = os.path.join(ruta_actual, "becas.csv")
        archivo = open(ruta_csv,"r")
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            idBeca = str(fila[0])
            tipo = str(fila[1])
            importe = str(fila[2])
            self.agregar(Beca(idBeca, tipo, importe))

        longitud = len(self.__becas)
        for i in range(longitud):
            print(self.__becas[i].getIdBeca(),self.__becas[i].getTipo(),self.__becas[i].getImporte())
    
    def buscarNombre(self,nombre):
        bandera = False
        long = len(self.__becas)
        i = 0

        while 1 < long and not bandera:
            if(self.__becas[i].getTipo() == nombre):
                bandera = True
            else:
                i += 1
        if(bandera == True):
            return self.__becas[i].getIdBeca()
        else:
            print("Beca no encontrada")  