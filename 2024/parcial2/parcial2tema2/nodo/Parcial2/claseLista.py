import csv
from claseNodo import nodo
from clasePesada import pesada
from claseElectrica import electrica

class lista:
    __comienzo: nodo
    __actual : nodo
    __tope : int
    __indice : int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice +=1
            dato = self.__actual.getEquipo()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def carga(self):
        with open('C:\\Users\\theal\\Desktop\\Parcial2\\equipos.csv') as archivo:
            leer=csv.reader(archivo,delimiter=';')
            next(leer)
            for fila in leer:
                if fila[0]=='M':
                    if fila[6]=='N/A':
                        x=0
                        equi=pesada(fila[1],fila[2],int(fila[3]),fila[4],fila[5],x, float(fila[7]), int(fila[8]), tipoM=fila[9], peso=int(fila[10]))
                        unnodo=nodo(equi)
                        unnodo.setSiguiente(self.__comienzo)
                        self.__comienzo=unnodo
                    else:
                        equi=pesada(fila[1],fila[2],int(fila[3]),fila[4],fila[5],int(fila[6]), float(fila[7]), int(fila[8]), tipoM=fila[9], peso=int(fila[10]))
                        unnodo=nodo(equi)
                        unnodo.setSiguiente(self.__comienzo)
                        self.__comienzo=unnodo
                else:
                    if fila[6]=='N/A':
                        x=0
                        equi=electrica(fila[1],fila[2],int(fila[3]),fila[4],fila[5],x, float(fila[7]), int(fila[8]), fila[9])
                        unnodo=nodo(equi)
                        unnodo.setSiguiente(self.__comienzo)
                        self.__comienzo=unnodo
                    else:
                        equi=electrica(fila[1],fila[2],int(fila[3]),fila[4],fila[5],int(fila[6]), float(fila[7]), int(fila[8]), fila[9])
                        unnodo=nodo(equi)
                        unnodo.setSiguiente(self.__comienzo)
                        self.__comienzo=unnodo
        archivo.close()
    def longitud(self):
        cant=0
        aux=self.__comienzo
        while aux!=None:
            cant+=1
            aux=aux.getSiguiente()
        return cant
    def pos(self):
        cant=self.longitud()
        i=int(input(f"La lista posee {cant} elementos, elegir un numero del 0 al {cant}: "))
        i=i-1
        if i<0 or i>cant-1:
            raise IndexError
        c=0
        aux=self.__comienzo
        while c!=i:
            aux=aux.getSiguiente()
            c+=1
        if(isinstance(aux.getEquipo(),pesada)):
            print(f"El equipo numero: {i+1} es maquinaria pesada\n")
        elif(isinstance(aux.getEquipo(),electrica)):
            print(f"El equipo numero: {i+1} es maquinaria electrica\n")
        else:
            print("tipo no reconocido\n")
    def cantAnio(self):
        anio=int(input("Ingrese un anio\n"))
        aux=self.__comienzo
        cant=0
        while aux!=None:
            if isinstance(aux.getEquipo(),electrica) and (aux.getEquipo().getAnio()==anio):
                cant+=1
            aux=aux.getSiguiente()
        print(f"La cantidad de equipos electricos fabricados ese anio es: {cant}\n")
    def cantCap(self):
        cap=int(input("Ingrese una capacidad\n"))
        aux=self.__comienzo
        cant=0
        while aux!=None:
            if isinstance(aux.getEquipo(),pesada) and (aux.getEquipo().getCap()==cap):
                cant+=1
            aux=aux.getSiguiente()
        print(f"La cantidad de equipos pesados con esa capacidad es: {cant}\n")
    def mostrar(self):
        actual=self.__comienzo
        while actual:
            print(actual.getEquipo().mostrar())
            actual = actual.getSiguiente()