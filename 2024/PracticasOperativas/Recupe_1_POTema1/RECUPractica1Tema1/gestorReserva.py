import csv
from claseReserva import *

class GestorR:
    __listaR:list

    def __init__(self):
        self.__listaR=[]
       

    def carga (self):
        archivo = open ('Reservas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)    
        for fila in reader:
            reserva = Reserva(int(fila[0]),fila[1],int(fila[2]),fila[3],int(fila[4]),int(fila[5]),float(fila[6]))
            self.__listaR.append(reserva)

    def reserva(self,num_cab):
        bandera=False
        i=0
        while i< len(self.__listaR):
            if self.__listaR[i].getNumCabaña() == num_cab:
                bandera=True
            i+=1
        return bandera        
    
    def listado_reservas(self,GC):
        fecha=input("Ingrese Fecha de inicio de hospedaje\n")
        i=0
        print(f"Reservas Para la fecha:{fecha}\nN° de Cabaña    Importe Diario  Cantidad dias   Seña            Importe a Cobrar")
        while i < len(self.__listaR):
            if self.__listaR[i].getFecha()==fecha:
                texto="{}\t\t{}\t{}\t\t{}\t{}"
                imp_diario = GC.importe_diario(self.__listaR[i].getNumCabaña()) 
                print(texto.format(self.__listaR[i].getNumCabaña(),imp_diario,self.__listaR[i].getDias(),self.__listaR[i].getImporteSeña(),(self.__listaR[i].getDias() * imp_diario - self.__listaR[i].getImporteSeña()))) 
            i+=1