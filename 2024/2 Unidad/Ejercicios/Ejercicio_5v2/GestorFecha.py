import csv
from claseFechaF import Fecha

class GestorF:
    def __init__(self, listaF=[]):
        self.__listaF = listaF

    def agregarFecha(self, unafecha):
        self.__listaF.append(unafecha)    

    def cargar_fechas(self):
        archivo = open ('fechasFutbol.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            self.agregarFecha(Fecha(int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3])))
        archivo.close()