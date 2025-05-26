import numpy as np
import csv
from clase_cabaña import cabana
class gestor_cab:
    __lista:np.ndarray
    def __init__(self):
        self.__lista=np.zeros(10,dtype=object)
        self.recuperar()
    def recuperar(self):
        with open('Cabañas.csv','r',newline='') as archivo:
            reader=csv.reader(archivo,delimiter=';')
            next(reader)
            i=0
            for fila in reader:
                self.__lista[i]=cabana(*fila)
                i+=1
    def capacidad(self,GR):
        huespedes=int(input("Ingrese numero de Huespedes\n"))
        for cab in self.__lista:
            band=False
            if cab >= huespedes and GR.reserva(cab.get_num()) is False:
                print(f"La Cabaña Numero {cab.get_num()} Esta disponible para {huespedes} huespedes\n")
                band=True
        if band==False:
            print("No hay cabañas disponibles por ahora hagase culear\n")
    def importe_diario(self,num_cab):
        i=0
        while i < len(self.__lista) and self.__lista[i].get_num() != num_cab:
            i+=1
        return self.__lista[i].get_importe()