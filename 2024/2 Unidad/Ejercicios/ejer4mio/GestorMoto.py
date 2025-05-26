import csv
from claseMoto import Moto
from clasePedido import Pedido

class GestorMoto:
    __listaM:list

    def __init__(self):
        self.__listaM = []

    def agregarMoto(self,unamoto):
        """Metodo para agregar moto al gestor"""
        self.__listaM.append(unamoto)

    def cargarArchivoMoto(self):
        archivo = open ('datosMoto.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            self.agregarMoto(Moto(fila[0],fila[1],fila[2],fila[3]))
           # self.__listaM.append(moto)
        print ("Motos cargadas correctamente")
        archivo.close()

    def valdidar_patente(self, patente):
        for moto in self.__listaM:
            if patente == moto._Moto__patente():
                return patente
        print("Patente no encontrada")

    # def mostrarDatos(self, patente):
    #      for moto in self.__listaM:
    #         if moto._Moto__patente == patente:
    #             print("Datos del conducator")
    #             print(f"Patente: {Moto.__patente}, Marca: {Moto.__marca}, Nombre y Apellido: {Moto.__nya}, Kilometraje: {Moto.__kilometraje}")

    def mostrarDatos(self,patente):
        """Devuelve los datos del conductor con determinada patente de moto"""
        i=0
        encontrado=False
        listaDatos=[]
        while encontrado is False and i<len(self.__listaM):
            if self.__listaM[i].getPatente()==patente:
                encontrado=True
                listaDatos.append(self.__listaM[i].getConductor())
                listaDatos.append(self.__listaM[i].getMarca())
                listaDatos.append(self.__listaM[i].getKilometraje())
            else:
                i+=1
        if encontrado is False:
            return -1
        else:
            return listaDatos

    def patentesRegistradas(self):
        """Este metodo devuelve una lista con las patentes de todas las motos"""
        listaPatentes=[]
        for i in self.__listaM:
            listaPatentes.append(i.getPatente())
        return listaPatentes    
    
    