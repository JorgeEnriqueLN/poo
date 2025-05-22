from datetime import datetime
import csv
import numpy as np
from atencion import Atencion

class ManejadorAtencion:
    __cantidad: int
    __dimension: int
    __arreA: np.ndarray
    __incremento = 1

      
    def __init__(self, dimension=50, incremento=1):
        self.__arreC= np.empty (dimension, dtype=Atencion)
        self.__cantidad = 0
        self.__dimension = dimension

 
    def agregarAtencion(self, unaAtencion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreA.resize(self.__dimension)
        self.__arreA[self.__cantidad]=unaAtencion
        self.__cantidad += 1
        
    def cargarAtencion(self):
        with open(r'C:\\Users\\novo2\\OneDrive\\Escritorio\\lcc\2-Segundo\\Poo\\U_2\\poo\\Ejercicios\\Ejercicio_6_U2\\atenciones.csv', encoding='utf-8') as archivoAtencion:
            reader = csv.reader(archivoAtencion, delimiter=';')
            next(reader)
            for fila in reader:
                dni = int(fila[0])
                fecha = datetime.strptime(fila[1], '%d/%m/%Y').date()
                nombre = fila[2]
                
                atencion = Atencion(dni, fecha, nombre)
                self.agregarAtencion(atencion)


    def atencionesRealizadas(self, fecha:datetime):
        i=0
        suma=0
        while (i<self.__cantidad):
            if self.__arreA[i].getFecha() == fecha:
                print(f"Atencion realizada: {self.__arreA[i]}")
                suma+=self.__arreA[i].getImporte()
            i+=1
        print(f"el total es: {suma}")
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreA[i])

   
        