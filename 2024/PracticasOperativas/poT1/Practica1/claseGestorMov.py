import numpy as np
import csv
from claseMovimiento import Movimiento

class GestorMovimiento:
    __gestor:list

    def __init__(self) -> None:
        self.__gestor=np.array([])

    def carga(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter=";")
        band=False
        for fila in reader:
            if not band:
                band=True
            else:
                mov = Movimiento(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
                self.__gestor=np.append(self.__gestor, values=mov)
        
    def mostrar(self):
        for mov in self.__gestor:
            mov.mostrar()

    def actImp(self, numT):
        imp=0
        for movimiento in self.__gestor:
            if movimiento.getNumT() == numT:
                if movimiento.getTipo() == 'C':
                    imp+=movimiento.getImp()
                elif movimiento.getTipo() == 'P':
                    imp-=movimiento.getImp()
        return imp
    
    def mostrarCliente(self, nom, app, numT, saldoAnt, saldoAct):
        print(f"""\n
        Cliente: {nom}, {app}   Número de tarjeta: {numT} 
        Saldo anterior: {saldoAnt} 

        Movimientos 
        Fecha\tDescripción\tImporte\tTipo de movimiento 
        """)
        for mov in self.__gestor:
            if mov.getNumT() == numT:
                print(f"""
            {mov.getFecha()}\t{mov.getDesc()}\t{mov.getImp()}\t{mov.getTipo()}
                """)
        print(f"""
        Saldo actualizado: {saldoAct}\n
        """)
    
    def Mov(self, numT):
        for mov in self.__gestor:
            if mov.getNumT == numT:
                return True
            else:
                return False

    def ordenar(self):
        self.__gestor=np.sort(self.__gestor)