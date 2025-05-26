import csv
from claseEquipo import Equipo

class GestorE:
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def agregarEquipo(self, unequipo):
        self.__listaE.append(unequipo)   

    def cargar_equipo(self):
        archivo = open ('equipos2024.csv')
        reader = csv.reader(archivo,delimiter=',')
        print ("Carga correcta")
        for fila in reader:
            self.agregarEquipo(Equipo(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4]),int(fila[5])))
        archivo.close()

    def obterIdPorNombre (self):
        """metodo que devuelve id del equipo comparando con el nombre ingresado"""
        nomEquipo = input ("Ingrese el nombre del equipo")
        i = 0
        band = False
        while band is False and i<len(self.__listaE):
            if self.__listaE[i].getNombre() == nomEquipo:
                idObtendo = self.__listaE[i].getIdEquipo()
                band = True

            i += 1

        if band: 
            return idObtendo
        else:
            return -1
        
