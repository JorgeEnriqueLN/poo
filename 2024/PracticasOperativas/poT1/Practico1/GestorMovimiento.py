import csv
import numpy as np
from claseMovimiento import Movimiento

class GestorM:
    __listaMoviminto:list

    def __init__(self):    
        self.__listaMoviminto=[]

    def agregarMovimiento(self,unmovi):
        self.__listaMoviminto.append(unmovi)


    def cargarMovimiento(self):
        
        archivo= open('MovimientosAbril2024.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarMovimiento(Movimiento(int(fila[0]),int(fila[1]),fila[2],fila[3],int(fila[4])))

        archivo.close()

    def getMovimiento (self):
        for i in self.__listaMovimiento[i]:
            