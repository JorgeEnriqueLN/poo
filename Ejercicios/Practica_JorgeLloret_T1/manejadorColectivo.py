import csv
import numpy as np
from Colectivo import Colectivo


class ManejadorCole:
    __cantidad: int
    __dimension: int
    __arreC: np.ndarray


    def __init__(self, dimension=0, cantidad=0):
        self.__arreC= np.empty (dimension, dtype=Colectivo)
        self.__cantidad = cantidad
        self.__dimension = dimension

 
    def agregarColectivo(self, unColectivo):
        if self.__cantidad<self.__dimension:
            self.__arreC[self.__cantidad]=unColectivo
            self.__cantidad += 1
    # def agregarColectivo(self, unColectivo, cant):
    #     if self.__cantidad==cant:
    #         cant+=self.__incremento
    #         self.__arreC.resize()
    #     self.__arreC[self.__cantidad]=unColectivo
        

    def getunColectivo(self, indice):
        return self.__arreC[indice-1]
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreC[i])


    def cargarColectivo(self):
        with open(r'C:\\Users\\novo2\\OneDrive\\Escritorio\\lcc\2-Segundo\\Poo\\U_2\\poo\\Ejercicios\\Practica_JorgeLloret_T1\\colectivos.csv', encoding='utf-8') as archivoColectivo:
            reader = csv.reader(archivoColectivo, delimiter=';')
            next(reader)  # salta la primera línea (encabezado)

            for fila in reader:
                #unColectivo = Colectivo(fila[0], fila[1], int(fila[2]),int(fila[3]), int(fila[4]), int(fila[5]))
                unColectivo = Colectivo(fila[0], fila[1], int(fila[2]),int(fila[3]), int(fila[4]))
                self.agregarColectivo(unColectivo)


    def buscarChofer(self, chofer):
        i=0
        patente=-1
        encontrado =False

        while (i<self.__cantidad and not encontrado):
            
            if (self.__arreC[i].getDni()==int(chofer)):
                encontrado=True
                patente= self.__arreC[i].getPatente()
               
            else:
                i+=1
                
        return patente
    

    def obtenerColectivos(self, mt):
        for i in range (self.__cantidad):
            patente = self.__arreC[i].getPatente()
            combustible = int(self.__arreC[i].getCombustible())
            
            mt.mostrarDatos(patente, combustible)
