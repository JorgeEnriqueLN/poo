from ClaseAtenciones import Atencion
import csv
import numpy as np

class GestorAtencion:
    __arregloAtenciones: np.ndarray
    __cantidad: int
    __incremento: int
    __dimension: int
    def __init__(self):
        self.__arregloAtenciones = np.empty(0, dtype=Atencion)
        self.__cantidad= 0
        self.__incremento= 1
        self.__dimension= 0
    def agregar_atencion(self, unaAtencion: Atencion):
        if(self.__cantidad == self.__dimension):
            self.__dimension+= self.__incremento
            self.__arregloAtenciones = np.resize(self.__arregloAtenciones, self.__dimension)
        self.__arregloAtenciones[self.__cantidad]= unaAtencion
        self.__cantidad+=1
    def cargar_atencion(self):
        archivo = open("Ejercicio 6/atenciones.csv", mode='r')
        reader= csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unaAtencion= Atencion(int(fila[0]),
                                  fila[1],
                                  float(fila[2]))
            self.agregar_atencion(unaAtencion)
        archivo.close()
    def mostrar_atencion(self):
        for atencion in self.__arregloAtenciones:
            print(atencion)
    def buscar_importe_total(self, fecha_buscada):
        acum= 0
        for atencion in self.__arregloAtenciones:
            fecha= atencion.get_fecha()
            if(fecha == fecha_buscada):
                acum += atencion.get_importe_atencion()
        return acum
    def obtener_atenciones_por_dni(self, dni):
        cont=0
        for atencion in self.__arregloAtenciones:
            if(dni == atencion.get_dni()):
                cont+=1
        return cont
    def buscar_atenciones_pacientes(self, dni):
        i=0
        bandera=False
        while(i<len(self.__arregloAtenciones) and dni != self.__arregloAtenciones[i].get_dni()):
            i+=1
        if(i<len(self.__arregloAtenciones)):
            bandera= False
        else:
            bandera= True
        return bandera