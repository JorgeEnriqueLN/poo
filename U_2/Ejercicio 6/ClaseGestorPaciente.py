from ClasePacientes import Paciente
import csv

class GestorPaciente:
    __listaPacientes: list
    def __init__(self):
        self.__listaPacientes = []
    def agregar_pacientes(self, unPaciente: Paciente):
        self.__listaPacientes.append(unPaciente)
    def cargar_pacientes(self):
        archivo = open("Ejercicio 6/pacientes.csv", mode='r')
        reader= csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unPaciente = Paciente(int(fila[0]),
                                  fila[1],
                                  fila[2])
            self.agregar_pacientes(unPaciente)
        archivo.close()
    def mostrar_pacientes(self):
        for paciente in self.__listaPacientes:
            print(paciente)
        
    def buscar_dni(self, dni, gestorAtencion):
        i=0
        while(i<len(self.__listaPacientes) and dni != self.__listaPacientes[i].get_dni()):
            i+=1
        
        if(i<len(self.__listaPacientes)):
            nombre= self.__listaPacientes[i].get_nombre()
            cont=gestorAtencion.obtener_atenciones_por_dni(dni)
            print(f"El nombre del paciente es: {nombre}\nLa cantidad de consultas que tuvo fue: {cont}")
        else:
            print("El DNI que buscas no existe")
    def listar_pacientes(self, gestorAtencion):
        print("LISTADO DE PACIENTES QUE NO TUVIERON ATENCIONES")
        for paciente in self.__listaPacientes:
            dni= paciente.get_dni()
            bandera = gestorAtencion.buscar_atenciones_pacientes(dni)
            if(bandera is not False):
                nombre= paciente.get_nombre()
                print(f"Apellido y nombre: {nombre}")

    def ordenar(self):
        self.__listaPacientes.sort()
    def ordenar_por_unidad(self):
        self.ordenar()
        siguienteUnidad= None
        for paciente in self.__listaPacientes:
            unidadActual = paciente.get_unidad()
            if(unidadActual != siguienteUnidad):
                siguienteUnidad = unidadActual
                print("-" *50)
                print(f"Unidad: {paciente.get_unidad()}")
            print(f"Apellido y Nombre: {paciente.get_nombre()}")
        
