import csv
from clasePedido import Pedido
from claseMoto import Moto
from GestorMoto import GestorMoto

class GestorPedido:
    __listaP:list

    def __init__(self):
        self.__listaP = []

    def cargarPedidos(self):
        archivo = open ('datosPedidos.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            pedido = Pedido(*fila)
            self.__listaP.append(pedido)
        print ("Pedidos cargados")
        archivo.close()

    def nuevoPedido(self):
        patente = input("Ingrese patente")
        if GestorMoto.verificar_patente(self, patente):
            print ("Patente encontrada")
            idPedido = input("Ingrese id del pedido")
            tiempoEntrega = input("Ingrese tiempo de espera")
            tiempoReal = 0
            precio = input ("Precio")

        pedido = Pedido(patente,idPedido,tiempoEntrega,tiempoReal,precio)
        self.__listaP.append(pedido)

    def modificar_tiempoReal (self):
        patente = input ("Patente a consultar?")
        idPedido = input ("Identificador del pedido")
        for pedido in self.__listaP:
            if (pedido._Pedido__idPedido == idPedido) and (pedido._Pedido__patente == patente):
                pedido._Periodo__tiempoReal = input("Modifique el tiempo real")
                #break esto tal vez se deba colocar

    def promedio_conductor(self):
        sumaTotalTiempo = 0
        i = 0
        patente = input ("ingrese patente del conductor para calcular promedio")
        for moto in self.__listaP:
            if moto._Pedido__patente == patente:
                GestorMoto.mostrarDatos()            
                sumaTotalTiempo += moto._Pedido__tiempoReal
                i += 1
        promedio = sumaTotalTiempo/i
        print (f"El promedio es: {promedio}")

    def ordenar(self):
        """Metodo para ordenar la lista de pedidos en orden ascendente en base a patente"""
        #print(self.__listaPedidos) #Antes de ordenar
        self.__listaP=sorted(self.__listaP)
        #print(self.__listaPedidos) #Despues de ordenar    