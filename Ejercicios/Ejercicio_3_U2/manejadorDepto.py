import csv
from Departamento import Departamento
from Accidente import Accidente

class ManejadorD:
    __deptos:list

    def __init__(self):
        self.__deptos=[]

    def agregarDeptos(self, depto):
        self.__deptos.append(depto)

    def cargarDeptos(self):
        with open(r'C:\Users\novo2\OneDrive\Escritorio\lcc\2-Segundo\Poo\U_2\poo\Ejercicios\Ejercicio_3_U2\Departamentos.csv', encoding='utf8') as archivo:
            reader=csv.reader(archivo, delimiter=';')
            next (reader)

            for fila in reader:
                numDepa= fila [0]
                nomDepa= fila [1]
                unDepto= Departamento(numDepa, nomDepa) 
                self.agregarDeptos(unDepto)
       
        
    def GetNombreEnListaDepartamentos(self, id):
        return self.__deptos[id].getNombre()
   