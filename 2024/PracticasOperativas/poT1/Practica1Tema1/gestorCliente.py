import csv
from claseCliente import Cliente


class GestorC:
    __listaCliente: list

    def __init__(self):
        self.__listaCliente=[]


    def cargaCliente (self):
        archivo = open ('ClientesAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        band=False
        for fila in reader:
            if not band:
                band=True
            else:    
                cliente = Cliente(fila[0],fila[1],int(fila[2]),int(fila[3]),int(fila[4]))
                self.__listaCliente.append(cliente)

        archivo.close()    

    def mostrarDatosGestor (self):
        for fila in self.__listaCliente:
            Cliente.mostrar()    