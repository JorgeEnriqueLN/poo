import csv
import numpy as np
from claseMiembro import *

class GestorM:
    __listaM: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int   

    def __init__(self) -> None:
        self.__listaM=np.empty([0], dtype=Miembro)  
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1

    def agregar_miembro(self, unmiembro):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaM.resize(self.__dimension)
        self.__listaM[self.__cantidad] = unmiembro
        self.__cantidad += 1    
        
    def cargarMiembros (self):
        archivo = open ('Miembros.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        
        for fila in reader:
            unmiembro= Miembro(int(fila[0]),
                              fila[1],
                              fila[2])
            self.agregar_miembro(unmiembro)
        archivo.close()



    def min_vistos(self,GV):
        correoelectronico=input("Ingrese el correo electrónico\n")
        i=0
        for miem in self.__listaM:
            
            if miem.get_correo == correoelectronico:
                print(f"{GV.vistos (miem.get_id_miembro())}")
                print(f"El miembro {miem.get_ayn()} visualizó {GV.get_minutos} \n")
                i+=1
        if miem.get_correo != correoelectronico:
            print("Sin visualizaciones\n") 
            

           
            