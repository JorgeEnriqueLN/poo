import csv
from Tramo import Tramo


class ManejadorTramo:
    __tramo:list

    def __init__(self):
        self.__tramo=[]

    def agregarTramo(self, tr):
        self.__tramo.append(tr)

    def cargarTramo(self):
        with open(r'/home/jorge/Escritorio/POO/Ejercicios/Practica_JorgeLloret_T1/tramos.csv', encoding='utf8') as archivo:
            reader=csv.reader(archivo, delimiter=';')
            next (reader)
            for fila in reader:
                unTram = Tramo(fila[0], fila[1], int(fila[2]), fila[3])
                self.agregarTramo(unTram)
            
       
        
    def GetNombreEnListaTramos(self, id):
        return self.__tramo[id].getNombre()
    

    def mostrarTramos(self, patente):
        
        for i in range(len(self.__tramo)):
            if (patente==self.__tramo[i].getPatente()):
                print(f"Patente: {self.__tramo[i].getPatente()}")
                print(f"Desde: {self.__tramo[i].getOrigen()}")
                print(f"Hasta: {self.__tramo[i].getDestino()}")
                print(f"Distancia: {self.__tramo[i].getDistancia()}")
         

    def buscarTramo(self, pat):
        i=0
        dato=-1
        encontrado =False

        while (i<self.__cantidad and not encontrado):
            
            if (self.__tramo[i].getPatente()==pat):
                encontrado=True
                dato= self.__tramo[i].getPatente()
               
            else:
                i+=1
                
        return dato
    
    def mostrarListaTramos(self):
        for i in self.__tramo:
        #     print(f"Patente: {self.__tramo[i].getPatente()}")
        #     print(f"Desde: {self.__tramo[i].getOrigen()}")
        #     print(f"Hasta: {self.__tramo[i].getDestino()}")
        #     print(f"Distancia: {self.__tramo[i].getDistancia()}")
        # print("------------------------------------------------")
            print(i)