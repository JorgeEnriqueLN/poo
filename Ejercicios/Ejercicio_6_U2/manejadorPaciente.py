import csv
from paciente import Paciente

class ManejadorPaciente:
    def __init__(self):
        self.__listaP = []

    def agregarPaciente(self, paciente):
        self.__listaP.append(paciente)

    def cargarPacientes(self):
        with open(r'C:\\Users\\novo2\\OneDrive\\Escritorio\\lcc\2-Segundo\\Poo\\U_2\\poo\\Ejercicios\\Ejercicio_6_U2\\pacientes.csv', encoding='utf8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)
            for fila in reader:
                paciente = Paciente(int(fila[0]), fila[1], fila[2])
                self.agregarPaciente(paciente)


    def mostrar_pacientes(self):
        for paciente in self.pacientes:
            print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}, Sexo: {paciente.sexo}")

    def buscarPaciente(self, dni):
        i=0
        encontrado = False
        while (i<len(self.__listaP) and not encontrado):
            if (self.__listaP[i].getDni()==dni):
                encontrado=True
                print(f"Nombre {self.__listaP[i].getNombre()}")
            else:
                i+=1
    