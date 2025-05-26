from ClaseCabaña import cabaña
import numpy as np
import csv

class GestorCabaña:
    __arregloCabaña: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self):
        self.__arregloCabaña = np.empty([0], dtype= cabaña)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
    
    def agregar_cabaña(self, unacabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloCabaña.resize(self.__dimension)
        self.__arregloCabaña[self.__cantidad] = unacabaña
        self.__cantidad += 1
    
    def cargar(self):
        archivo= open('Cabaña.csv', mode= 'r')
        #with open('Cabaña.csv', mode='r', newline='', encoding='utf-8') as archivo:
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unacabaña= cabaña(int(fila[0]),
                              int(fila[1]),
                              int(fila[2]),
                              int(fila[3]),
                              float(fila[4]))
            self.agregar_cabaña(unacabaña)
        archivo.close()
    
    def imprimir(self):
        for fila in self.__arregloCabaña:
            print(fila)
    
    def buscar_cabaña(self, cantidad, GR):
        for i in range(len(self.__arregloCabaña)):
            numeroC= self.__arregloCabaña[i].get_numero()
            if(self.__arregloCabaña[i] >= cantidad):
                print(f"La cabaña {numeroC} es apto")
                c=GR.cabañas_disponibles(numeroC)
                if(c):
                    print(f"La cabaña {numeroC} se encuentra ocupada")
                else:
                    print(f"La cabaña {numeroC} se encuentra desocupada")
            else:
                print(f"La cabaña {numeroC} no es apta")
        
    def buscar_importe_dia(self, cabaña):
        i=0
        while(i<len(self.__arregloCabaña) and cabaña!= self.__arregloCabaña[i].get_numero()):
            i+=1
        
        if(i<len(self.__arregloCabaña)):
            importe= self.__arregloCabaña[i].get_importe_dia()
            return importe
        
    def ordenar_arreglo(self):
        self.__arregloCabaña= np.sort(self.__arregloCabaña)
        
                