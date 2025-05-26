from clasePlan import *
class PlanTelevision(Plan):
    def __init__(self, nombre, duracion, cobertura, precio, cant_nacionales, cant_internacionales):
        super().__init__(nombre, duracion, cobertura, precio)
        self.__cant_nacionales = cant_nacionales
        self.__cant_internacionales = cant_internacionales

    def calcular_importe(self):
        importe_final = super().getprecio()
        if self.__cant_internacionales > 10:
            importe_final *= 1.15
        return importe_final
    
