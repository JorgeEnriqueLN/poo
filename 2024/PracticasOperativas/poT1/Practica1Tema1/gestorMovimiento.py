import csv
import numpy as np
from claseMovimiento import Movimiento

class GestorM:
    __listaM:list

    def __init__(self):
        self.__listaM= np.array([])

    
    def cargaMovimiento(self):
        archivo = open('MovimientosAbril2024.csv')
        reader= csv.reader(archivo,delimiter=";")
        band=False
        for fila in reader:
            if not band:
                band=True
            else:    
                movimiento = Movimiento(int(fila[0]),(fila[1]),fila[2],fila[3],int(fila[4]))
                self.__listaM = np.append(self.__listaM, values=movimiento)

        archivo.close()    