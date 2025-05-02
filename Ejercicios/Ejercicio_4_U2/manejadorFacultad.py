import numpy as np
import csv
from Facultad import Facultad

class ManejadorF:
    __cantidad: int
    __dimension: int
    __incremento= 1
    __arreF: np.ndarray


    def __init__(self, dimension=10, incremento=1):
        self.__arreF= np.empty (dimension, dtype=Facultad)
        self.__cantidad = 0
        self.__dimension = dimension

  
    def agregarFacultad(self, unaFacultad):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreF.resize(self.__dimension)
        self.__arreF[self.__cantidad]=unaFacultad
        self.__cantidad += 1

    def getunaFacultad(self, indice):
        return self.__arreF[indice]
    
    def cargarFacultad(self):
        with open(r'C:\Users\novo2\OneDrive\Escritorio\lcc\2-Segundo\Poo\U_2\poo\Ejercicios\Ejercicio_4_U2\Facultades.csv', encoding='utf-8') as archivoFacultades:
            reader = csv.reader(archivoFacultades, delimiter=';')
            next(reader)  # salta la primera línea (encabezado)

            for fila in reader:
                # fila debería ser una lista como: ['0', 'Nombre', 'Titulo', 'x', 'y', '5']
                unaFacultad = Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
                self.agregarFacultad(unaFacultad)

    
    # def cargarFacultad(self):
    #     saltear=True
    #     with open('Facultades.csv') as archivoFacultades:
    #         reader = csv.read(archivoFacultades, delimiter=";")
    #         for Fac in archivoFacultades:
    #             if not saltear:
    #                 saltear=True
    #             else:
    #                 unaFacultad=Facultad(int(Fac[0]),Fac[1],Fac[2],Fac[3],Fac[4])
    #                 self.agregarFacultad(unaFacultad)
    #         archivoFacultades.close()

    def mostrarFac(self, mc):
        for i in range(self.__cantidad):
            print(f"En la {self.__arreF[i].getNombre()} hay: {mc.cantidad(self.__arreF[i].getId())} carreras")

    def buscarFacultad(self, id):
        
        i=0
        encontrado =False

        while (i<self.__cantidad and not encontrado):
            
            if (int(self.__arreF[i].getId())==int(id)):
                encontrado=True
                facultad= self.__arreF[i].getNombre()
                print("")
            else:
                i+=1
                
        return facultad
    
    def buscarFacultadPorNombre(self, nombre):
        i=0
        encontrado=False
        aux=-1

        while (i<self.__cantidad and not encontrado):
            if (self.__arreF[i].getNombre()==nombre):
                aux= int(self.__arreF[i].getId())
                encontrado=True
            else:
                i+=1
        return aux
    


