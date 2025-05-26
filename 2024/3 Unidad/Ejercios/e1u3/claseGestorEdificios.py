import csv
from claseEdificio import Edificio

class GestorDeEdificios:
    __listaEdificios:list

    def __init__(self):
        self.__listaEdificios=[]

    def agregarEdificio(self,unedificio):
        self.__listaEdificios.append(unedificio)

    def cargarEdificios(self):
        archivo=open("EdificioNorte.csv")
        reader=csv.reader(archivo,delimiter=";")
        xedificio=None
        for fila in reader:
            if len(fila)==6:
                xedificio=Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
                self.agregarEdificio(xedificio)
            else:
                xedificio.agregarDepartamento(int(fila[0]),int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))
        archivo.close()

    def cantidadEdificios(self):
        print(len(self.__listaEdificios))

    def mostrarPropietarios(self,xnom):
        band = False
        i=0
        while band is False and i<len(self.__listaEdificios):
            if self.__listaEdificios[i].getNombreEdificio()==xnom:
                self.__listaEdificios[i].listarPropietariosDepartamentos()
                band=True
            else:
                i+=1
        assert band is True