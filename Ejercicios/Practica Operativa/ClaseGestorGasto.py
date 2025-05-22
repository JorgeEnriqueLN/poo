#Ormeño Agustin / E010-270
from ClaseGastos import Gasto
import csv

class GestorGasto:
    __listaGastos: list
    def __init__(self):
        self.__listaGastos= []
    def agregar_gasto(self, unGasto: Gasto):
        self.__listaGastos.append(unGasto)
    def cargar_gasto(self):
        archivo= open("gastosAbril2025.csv", mode='r')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unGasto = Gasto(fila[0],
                            fila[1],
                            float(fila[2]),
                            fila[3])
            self.agregar_gasto(unGasto)
        archivo.close()
    def mostrar_gasto(self):
        for gasto in self.__listaGastos:
            print(gasto)
    def obtener_gastos_por_patente(self, patente, importe_mensual_patente):
        print("Gastos\nFecha Importe Descripción")
        acum=0
        for gasto in self.__listaGastos:
            if(patente == gasto.get_patente()):
                fecha = gasto.get_fecha()
                importe_gasto= gasto.get_importe_gasto()
                descripcion = gasto.get_descripcion()
                print(f"{fecha} {importe_gasto} {descripcion}")
                acum+=importe_gasto
        total= acum + importe_mensual_patente
        print(f"Total de Gastos (incluye Patente): {total}")

    def buscar_fecha(self, fecha):
        acum =0
        for gasto in self.__listaGastos:
            if(fecha == gasto.get_fecha()):
                importe_gasto = gasto.get_importe_gasto()
                acum+= importe_gasto
        print(f"Total general a pagar para ese dia: {acum}")

    def listar_ordenado(self, fecha, gestorMovilidad):
        self.__listaGastos.sort()
        acum =0
        for gasto in self.__listaGastos:
            if(fecha == gasto.get_fecha()):
                patente = gasto.get_patente()
                importe_gasto = gasto.get_importe_gasto()
                total= gestorMovilidad.listar_ordenado(patente, importe_gasto)
                acum+= total
        print("El total a pagar es: ",acum)
        