import csv
from Tramo import Tramo


class ManejadorTramo:
    __tramo:list

    def __init__(self):
        self.__tramo=[]

    def agregarTramo(self, tr):
        self.__tramo.append(tr)

    def cargarTramo(self):
        with open(r'C:\\Users\\novo2\\OneDrive\\Escritorio\\lcc\2-Segundo\\Poo\\U_2\\poo\\Ejercicios\\Practica_JorgeLloret_T1\\tramos.csv', encoding='utf8') as archivo:
            reader=csv.reader(archivo, delimiter=';')
            next (reader)
            for fila in reader:
                unTram = Tramo(fila[0], fila[1], int(fila[2]), fila[3])
                self.agregarTramo(unTram)
            
       
        
    def GetNombreEnListaTramos(self, id):
        return self.__tramo[id].getNombre()
    

    def mostrarTramos(self, patente):
        suma=0
        for i in range(len(self.__tramo)):
            if (patente==self.__tramo[i].getPatente()):
                print(f"Patente: {self.__tramo[i].getPatente()}")
                print(f"Desde: {self.__tramo[i].getOrigen()}")
                print(f"Hasta: {self.__tramo[i].getDestino()}")
                print(f"Distancia: {self.__tramo[i].getDistancia()}")
                suma+=self.__tramo[i].getDistancia()
        return print(f'Cantidad total de km: {suma} ')
        

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

    def mostrarDatos(self, patente, combustible):
        promedio=0
        km=0
        for i in range(len(self.__tramo)):
            
            if (self.__tramo[i].getPatente()==patente):
                
                km += int(self.__tramo[i].getDistancia())

        promedio = int(km*combustible/100)
        print (f"Patente del colectivo: {patente} - kilometros recorridos {km} - El combustible promedio: {promedio}")

    def listarDistancia(self, distancia):
        for i in self.__tramo:
            if i > distancia :
                print(f"Origen: {i.getOrigen()} km: {i.getDistancia()}")
