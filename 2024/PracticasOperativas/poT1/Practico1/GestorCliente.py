import csv
from claseCliente import Cliente
from claseMovimiento import Movimiento
from GestorMovimiento import GestorM

class GestorC:
    __listaClientes:list

    def __init__(self):    
        self.__listaClientes=[]

    def agregarCliente(self,uncliente):
        self.__listaClientes.append(uncliente)


    def cargaCliente(self):        
        archivo= open('ClientesAbril2024.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarCliente(Cliente(fila[0],fila[1],fila[2],int(fila[3]),int(fila[4])))

        archivo.close()


    def actualizarSaldo(self):

        i=0
        encontrado=False
        documento=input('Ingresar dni para actualizar saldo: ')
        
        for i in len(self.__listaClientes):
            if documento==self.__listaClientes[].():
                if 'C'== GestorM.__listaMoviminto[]
                creditos_totales = sum(Movimiento.get)
                pagos_totales = sum(Movimiento.lista)
                saldo_actual = creditos_totales - pagos_totales

              
                encontrado=True
            else:
                i+=1
        if encontrado is False:
            print('')