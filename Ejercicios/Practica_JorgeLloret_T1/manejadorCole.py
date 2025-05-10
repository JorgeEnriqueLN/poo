import csv
import numpy as np
from Colectivo import Colectivo


class ManejadorCole:
    __cantidad: int
    __dimension: int
    __incremento=1
    __arreC: np.ndarray


    def __init__(self, dimension=10, incremento=1, cantidad=0):
        self.__arreC= np.empty (dimension, dtype=Colectivo)
        self.__cantidad = cantidad
        self.__dimension = dimension

 
    def agregarColectivo(self, unColectivo):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreC.resize(self.__dimension)
        self.__arreC[self.__cantidad]=unColectivo
        self.__cantidad += 1

    def getunColectivo(self, indice):
        return self.__arreC[indice]
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreC[i])


    def cargarColectivo(self):
        with open(r'/home/jorge/Escritorio/POO/Ejercicios/Practica_JorgeLloret_T1/colectivos.csv', encoding='utf-8') as archivoColectivo:
            reader = csv.reader(archivoColectivo, delimiter=';')
            next(reader)  # salta la primera línea (encabezado)

            for fila in reader:
                #unColectivo = Colectivo(fila[0], fila[1], int(fila[2]),int(fila[3]), int(fila[4]), int(fila[5]))
                unColectivo = Colectivo(fila[0], fila[1], int(fila[2]),int(fila[3]), int(fila[4]))
                self.agregarColectivo(unColectivo)


    def buscarChofer(self, chofer):
        i=0
        cho=-1
        encontrado =False

        while (i<self.__cantidad and not encontrado):
            
            if (self.__arreC[i].getDni()==int(chofer)):
                encontrado=True
                cho= self.__arreC[i].getPatente()
               
            else:
                i+=1
                
        return cho