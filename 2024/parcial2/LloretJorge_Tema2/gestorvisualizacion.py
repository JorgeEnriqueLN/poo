import csv
from claseVisualizacion import *

class GestorV:
    __listaV:list

    def __init__(self):
        self.__listaV=[]
       

    def carga (self):
        archivo = open ('Visualizaciones.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)    
        for fila in reader:
            visualiz = Visualizacion(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
            self.__listaV.append(visualiz)


    def vistos(self,id_miembro):
       
        i=0
        while i< len(self.__listaV):
            if self.__listaV[i].get_id_miembro() == id_miembro:
                return self.__listaV[i].__get_minutos
            i+=1
        
       