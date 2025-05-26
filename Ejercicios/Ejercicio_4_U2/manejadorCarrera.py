import numpy as np
import csv
from Carrera import Carrera

class ManejadorC:
    __cantidad: int
    __dimension: int
    __incremento=1
    __arreC: np.ndarray


    def __init__(self, dimension=10, incremento=1):
        self.__arreC= np.empty (dimension, dtype=Carrera)
        self.__cantidad = 0
        self.__dimension = dimension

 
    def agregarCarrera(self, unaCarrera):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreC.resize(self.__dimension)
        self.__arreC[self.__cantidad]=unaCarrera
        self.__cantidad += 1

    def getunaCarrera(self, indice):
        return self.__arreC[indice]
    



    def cargarCarrera(self):
        with open(r'C:\Users\novo2\OneDrive\Escritorio\lcc\2-Segundo\Poo\U_2\poo\Ejercicios\Ejercicio_4_U2\Carreras.csv', encoding='utf-8') as archivoCarrera:
            reader = csv.reader(archivoCarrera, delimiter=';')
            next(reader)  # salta la primera línea (encabezado)

            for fila in reader:
                # fila debería ser una lista como: ['0', 'Nombre', 'Titulo', 'x', 'y', '5']
                unaCarrera = Carrera(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5]))
                self.agregarCarrera(unaCarrera)

    # def cargarCarrera(self):
    #     saltear=True
    #     with open(r'C:\Users\novo2\OneDrive\Escritorio\lcc\2-Segundo\Poo\U_2\poo\Ejercicios\Ejercicio_4_U2\Carreras.csv') as archivoCarrera:
    #         reader = csv.reader(archivoCarrera, delimiter=';')
    #         for Car in archivoCarrera:
    #             if not saltear:
    #                 saltear=True
    #             else:
    #                 unaCarrera=Carrera(int(Car[0]),Car[1],Car[2],Car[3],Car[4],int(Car[5]))
    #                 self.agregarCarrera(unaCarrera)
    #         archivoCarrera.close()

    def buscarCarrera(self, carrera):
        i=0
        facultad=-1
        encontrado =False

        while (i<self.__cantidad and not encontrado):
            
            if (self.__arreC[i].getNombre()==carrera):
                encontrado=True
                facultad= int (self.__arreC[i].getCodigoFacultad())
                print("")
            else:
                i+=1
                
        return facultad
    
    def cantidad(self, idtraido):
        cont=0
        for i in range(self.__cantidad):
            if (self.__arreC[i].getCodigoFacultad()==idtraido):
                cont +=1
        return cont
    
    def listarOrdenado(self,aux):
        for i in range(self.__cantidad):
            if (self.__arreC[i].getCodigoFacultad()==aux):
                print(f"Nombre {self.__arreC[i].getNombre()}, duracion {self.__arreC[i].getDuracion()}")

    def ordenar(self):
        self.__arreC.sort()