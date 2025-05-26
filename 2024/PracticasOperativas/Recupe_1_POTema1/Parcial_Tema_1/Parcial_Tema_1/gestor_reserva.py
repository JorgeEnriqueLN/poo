import csv
from clase_reserva import reserva

class gestor_re:
    __lista:list
    def __init__(self):
        self.__lista=[]
        self.recuperar()
    def agregar(self,re):
        self.__lista.append(re)
    def recuperar(self):
        with open('Reservas.csv','r',newline='') as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregar(reserva(*fila))
    def reserva(self,num_cab):
        bandera=False
        i=0
        while i< len(self.__lista):
            if self.__lista[i].get_num() == num_cab:
                bandera=True
            i+=1
        return bandera
    def listado_reservas(self,GC):
        fecha=input("Ingrese Fecha de inicio de hospedaje\n")
        i=0
        print(f"Reservas Para la fecha:{fecha}\nN° de Cabaña    Importe Diario  Cantidad dias   Seña            Importe a Cobrar")
        while i < len(self.__lista):
            if self.__lista[i].get_fecha()==fecha:
                texto="{}\t\t{}\t{}\t\t{}\t{}"
                imp_diario = GC.importe_diario(self.__lista[i].get_num()) 
                print(texto.format(self.__lista[i].get_num(),imp_diario,self.__lista[i].get_dias(),self.__lista[i].get_seña(),(self.__lista[i].get_dias() * imp_diario - self.__lista[i].get_seña()))) 
            i+=1