from ClaseReserva import reserva
import csv
from typing import List
import numpy as np

class GestorReservas:
    __listareservas: List[reserva]

    def __init__(self):
        self.__listareservas = []
    
    def agregar_reserva(self, unaReserva):
        self.__listareservas.append(unaReserva)
    
    def cargar(self):
        archivo= open('Reserva.csv', mode= 'r')
        #with open('Reserva.csv', mode='r', newline='', encoding='utf-8') as archivo:
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unaReserva= reserva(int(fila[0]),
                                fila[1],
                                int(fila[2]),
                                fila[3],
                                int(fila[4]),
                                int(fila[5]),
                                float(fila[6]))
            self.agregar_reserva(unaReserva)
        archivo.close()
    
    def imprimir(self):
        for r in self.__listareservas:
            print(r)
        
    def cabañas_disponibles(self, numero):
        i=0
        while(i<len(self.__listareservas) and numero!= self.__listareservas[i].get_numero_cabaña()):
            i+=1
        
        if(i<len(self.__listareservas)):
            return True
        else:
            return False
    
    def listado(self, fecha, GC):
        for i in range(len(self.__listareservas)):
            if(fecha==self.__listareservas[i].get_fecha_inicio()):
                cabaña= self.__listareservas[i].get_numero_cabaña()
                importe_dia= float(GC.buscar_importe_dia(cabaña))
                cant_dias= self.__listareservas[i].get_cantidad_dias()
                seña= self.__listareservas[i].get_importe_seña()
                total= (cant_dias * importe_dia) - seña
                print(f"""
N° de cabaña     Importe diario      Cantidad días       Seña        Importe a cobrar
{cabaña}                {importe_dia}       {cant_dias}         {seña}      {total}""")
                
    def ordenar_lista(self):
        self.__listareservas= sorted(self.__listareservas)
        print(type(self.__listareservas))
