from claseElectricas import Electrica
from clasePesadas import Pesada
import csv

class gestorEquipo:
    __listaEquipos = list

    def __init__(self) -> None:
        self.__listaEquipos = []

        try:
            archivo = open('equipos.csv')
            reader = csv.reader(archivo, delimiter=";")
        except FileNotFoundError:
            print("No se encontro el archivo")
        else:
            for fila in reader:
                tipo = fila[0]
                marca = fila[1]
                modelo = fila[2]
                anio = fila[3]
                combustible = fila[4]
                potencia = fila[5]
                capacidadcarga = fila[6]
                alquilerdiario = fila[7]
                diasalquiler = fila [8]
                if tipo == "M":
                    tipomaquina = fila[9]
                    peso = int(fila[10])
                    objeto = Pesada(tipo, marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler, tipomaquina, peso)
                elif tipo == "E":
                    fuente = fila[9]
                    objeto = Electrica(tipo, marca, modelo, anio, combustible, potencia, capacidadcarga, alquilerdiario, diasalquiler, fuente)
                if tipo in ["M", "E"]:
                    self.__listaEquipos.append(objeto)
        archivo.close()

    
    def mostrar_tipo(self, i):
        try:
            if isinstance (self.__listaEquipos[i-1], Pesada):
                print (f"El equipo es una herramienta pesada. \n Tipo: {self.__listaEquipos[i-1].gettipo()} (Pesada)\n Marca: {self.__listaEquipos[i-1].getmarca()}")
            elif isinstance (self.__listaEquipos[i-1], Electrica):
                print (f"El equipo es una herramienta electrica. \n Tipo: {self.__listaEquipos[i-1].gettipo()} (Eléctrica)\n Marca: {self.__listaEquipos[i-1].getmarca()}")

        except IndexError:
            print(f"El indice ingresado esta fuera de rango, ingresa un indice entre 0 y {(len(self.__listaEquipos))-1}")


    def cantidad_por_anio (self, anio):
        cont = 0
        for equi in self.__listaEquipos:
            if ((int(equi.getanioDeFabricacion())== int(anio))and (isinstance (equi, Electrica))):
                cont += 1

        print (f"En el año {anio} se fabricaron {cont} herramientas eléctrica")

    def cantidad_