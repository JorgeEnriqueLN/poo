#Ormeño Agustin / E010-270
from ClaseMovilidad import Movilidad
import numpy as np
import csv

class GestorMovilidad:
    __arregloMovilidades: np.ndarray
    __incremento: int
    __cantidad: int
    __dimension: int
    def __init__(self):
        self.__cantidad = 0
        self.__incremento = 5
        self.__dimension = 4
        self.__arregloMovilidades = np.empty(self.__dimension, dtype= Movilidad)
    def agregar_movilidad(self, unaMovilidad):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloMovilidades.resize(self.__dimension)
        self.__arregloMovilidades[self.__cantidad] = unaMovilidad
        self.__cantidad+=1
    def cargar_movilidad(self):
        archivo = open("movilidades.csv", mode= 'r')
        reader = csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unaMovilidad = Movilidad(fila[0],
                                     fila[1],
                                     int(fila[2]),
                                     float(fila[3]),
                                     fila[4],
                                     fila[5])
            self.agregar_movilidad(unaMovilidad)
        archivo.close()
    def mostrar_movilidad(self):
        for i in range(self.__cantidad):
            print(self.__arregloMovilidades[i])
    def buscar_patente(self, patente, gestorGasto):
        i=0
        while(i<self.__cantidad and self.__arregloMovilidades[i].get_patente() != patente):
            i+=1
        if(i<self.__cantidad):
            tipo = self.__arregloMovilidades[i].get_tipo()
            capacidad_carga = self.__arregloMovilidades[i].get_capacidad_carga()
            importe_mensual_patente = self.__arregloMovilidades[i].get_importe_mensual_patente()
            marca = self.__arregloMovilidades[i].get_marca()
            modelo = self.__arregloMovilidades[i].get_modelo()
            print(f"Patente: {patente}      Tipo: {tipo}        Capacidad de Carga: {capacidad_carga}\nImporte Mensual de Patente: {importe_mensual_patente}    Marca: {marca}  Modelo: {modelo}")
            gestorGasto.obtener_gastos_por_patente(patente, importe_mensual_patente)
        else:
            print("No se encontro la patente que buscas")
    def listar_ordenado(self, patente, importe_gasto):
        i=0
        total = 0
        while(i<self.__cantidad and patente != self.__arregloMovilidades[i].get_patente()):
            i+=1
        if(i<self.__cantidad):
            importe_patente = self.__arregloMovilidades[i].get_importe_mensual_patente()
            total = importe_gasto + importe_patente
            marca = self.__arregloMovilidades[i].get_marca()
            modelo= self.__arregloMovilidades[i].get_modelo()
            print(f"Patente: {patente}\nMarca: {marca}\nModelo: {modelo}")
        else: 
            total = 0
        return total
        