import csv
import numpy as np
from claseCabaña import *

# class GestorC:
#     __listaC:np.ndarray

#     def __init__(self) -> None:
#         self.__listaC=np.zeros(10, dtype=object)  
        
        
#     def cargarCabañas (self):
#         archivo = open ('Cabañas.csv')
#         reader = csv.reader(archivo, delimiter=';')
#         next(reader)
#         i=0
#         for fila in reader:
#             self.__listaC[i]=Cabaña(*fila)
#             i+=1

#--------------------------------------------
class GestorC:
    __listaC: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int   

    def __init__(self) -> None:
        self.__listaC=np.empty([0], dtype=Cabaña)  
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1

    def agregar_cabaña(self, unacabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaC.resize(self.__dimension)
        self.__listaC[self.__cantidad] = unacabaña
        self.__cantidad += 1    
        
    def cargarCabañas (self):
        archivo = open ('Cabañas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        
        for fila in reader:
            unacabaña= Cabaña(int(fila[0]),
                              int(fila[1]),
                              int(fila[2]),
                              int(fila[3]),
                              float(fila[4]))
            self.agregar_cabaña(unacabaña)
        archivo.close()

#---------------------------------------------------
        
    def capacidad(self,GR):
        huespedes=int(input("Ingrese numero de Huespedes\n"))
        for cab in self.__listaC:
            band=False
            if cab >= huespedes and GR.reserva(cab.getNumero()) is False:
                print(f"La Cabaña Numero {cab.getNumero()} Esta disponible para {huespedes} huespedes\n")
                band=True
        if band==False:
            print("No hay cabañas disponibles por ahora\n")

    def importe_diario(self,num_cab):
        i=0
        while i < len(self.__listaC) and self.__listaC[i].getNumero() != num_cab:
            i+=1
        return self.__listaC[i].get_importe()   
