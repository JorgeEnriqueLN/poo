import numpy as np
import csv
import os
from Beneficiario import *

class ControladorBeneficiario:
    __beneficiario : np.ndarray
    __dimension: int
    __cantidad : int
    def __init__(self,dimension):
        self.__beneficiarios = np.empty(dimension, dtype=Beneficiario)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def agregar(self,beca):
        if self.__cantidad < self.__dimension:
            self.__beneficiarios[self.__cantidad] = beca
            self.__cantidad += 1
        else:
            print("No hay mas espacio")
    def cargar(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_csv = os.path.join(ruta_actual, "beneficiarios.csv")
        archivo = open(ruta_csv,"r")
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            self.agregar(Beneficiario(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7]))

        longitud = len(self.__beneficiarios)
        for i in range(longitud):
            print(self.__beneficiarios[i].getDni(),self.__beneficiarios[i].getNombre(),self.__beneficiarios[i].getApellido(),
                  self.__beneficiarios[i].getCarrera(),self.__beneficiarios[i].getSiglaFacultad(),self.__beneficiarios[i].getAnioCursa(),
                  self.__beneficiarios[i].getPromedio(),self.__beneficiarios[i].getIdBeca())
    
    #Copiar el codigo del item c del ejercicio 4 
    def importePagarPorTipoBeca(self,idBeca,nombreBeca,lbecas):
        long = len(self.__beneficiarios)
        importe = 0
        
        print("Beneficiarios de la beca ",nombreBeca)
        while 1 < long:
            if(self.__beneficiarios[i].getIdBeca() == idBeca):
                importe += lbecas[].getImporte()
                print()
            else:
                i += 1