from ClassMovimientos import Movimiento
from csv import reader
import numpy as np

class GestorMovimientos:
    __movimientos: np.array
    
    def __init__(self):
        self.__movimientos = np.array([], dtype=Movimiento)
        
    #retornar el arreglo numpy como una copia
    def get_movimientosCopia(self): return np.copy(self.__movimientos)
    
    def get_movimientos(self): return  self.__movimientos

    def agregarMovimiento(self,nuevoMovimiento):
        self.__movimientos = np.append(self.__movimientos,nuevoMovimiento)
    
    def leerMovimientos_desde_csv(self,nombre_archivo):
        with open(nombre_archivo, newline='') as archivo_csv:
            lector_csv = reader(archivo_csv,delimiter=';')
            for fila in lector_csv:
                numTarjeta,fecha,descripcion,tipo,importe = fila
                nuevoMovimiento = Movimiento(int(numTarjeta), fecha, descripcion, tipo, float(importe))
                self.agregarMovimiento(nuevoMovimiento)
    
    def verificarMovimientos(self,tarjetaIngresada,clientes):
        realizoMovimientos = False
        for movimiento in self.__movimientos:
            if movimiento.get_numTarjeta() == tarjetaIngresada:
                realizoMovimientos = True
        
        # verifico si no tuvo movimientos y si nos los tuvo entonces muestro los datos
        if realizoMovimientos == False:
            print("La tarjeta del cliente ingresado no realizo movimientos")
            for cliente in clientes:
                if cliente.get_numTarjeta() == tarjetaIngresada:
                    print(f"Apellido y Nombre:{cliente.get_apellido()} {cliente.get_nombre()}")
    
    def ordenarPorTarjeta(self):
        self.__movimientos = np.sort(self.__movimientos)