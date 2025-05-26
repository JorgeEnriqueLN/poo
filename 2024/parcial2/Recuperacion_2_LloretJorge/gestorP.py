from clasePlan import *
from claseTelefonia import *
from claseTelivision import *
import csv

class GestorPlanes:
    def __init__(self):
        self.planes = []


    def agregar_planes (self, plan):
        self.planes.append(plan)

    def cargar_planes(self, archivo):
        with open(archivo, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for fila in reader:
                    tipo = fila[0]
                    if tipo == 'M':
                        plan = PlanTelefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6]))
                    elif tipo == 'T':
                        plan = PlanTelevision(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6]))
                    else:
                        print(f"Tipo desconocido: {tipo}")
                        continue
                    self.agregar_planes(plan)

    # def cargar_planes(self, archivo_csv):
    #     with open(archivo_csv, newline='') as csvfile:
    #         reader = csv.reader(csvfile, delimiter=';')
    #         next(reader)  # Saltar la primera línea (encabezados)
    #         for fila in reader:
    #             tipo_plan = fila[0]
    #             nombre_compania = fila[1]
    #             duracion_plan = int(fila[2])
    #             cobertura_geografica = fila[3]
    #             precio_base = float(fila[4])
    #             if tipo_plan == 'M':  # Plan de Telefonía
    #                 tipo_llamadas = fila[5].split(',')
    #                 minutos = int(fila[6])
    #                 plan = PlanTelefonia(nombre_compania, duracion_plan, cobertura_geografica, precio_base, tipo_llamadas, minutos)
    #             elif tipo_plan == 'T':  # Plan de Televisión
    #                 canales_nacionales = int(fila[5])
    #                 canales_internacionales = int(fila[6])
    #                 plan = PlanTelevision(nombre_compania, duracion_plan, cobertura_geografica, precio_base, canales_nacionales, canales_internacionales)
    #             else:
    #                 continue
    #             self.lista_planes.append(plan)  
        


    def mostrar_tipo_plan(self, posicion):
        try:
            plan = self.planes[posicion]
            if isinstance(plan, PlanTelefonia):
                return "Plan de Telefonía"
            elif isinstance(plan, PlanTelevision):
                return "Plan de Televisión"
        except IndexError:
            raise IndexError("Índice fuera de rango")

    def contar_planes_por_cobertura(self, cobertura_geografica):
        return sum(1 for plan in self.planes if plan.getcobertura == cobertura_geografica)

    def buscar_planes_por_canales_internacionales(self, min_canales_internacionales):
        return [plan._Plan__nombre for plan in self.planes 
                if isinstance(plan, PlanTelevision) and plan._PlanTelevision__cant_internacionales >= min_canales_internacionales]

    def mostrar_todos_los_planes(self):
        return [plan.mostrar_datos() for plan in self.planes]
    
    
