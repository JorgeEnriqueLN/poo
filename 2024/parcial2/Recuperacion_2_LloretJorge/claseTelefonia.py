from clasePlan import *
class PlanTelefonia(Plan):
    def __init__(self, nombre, duracion, cobertura, precio, tipo_llamadas, minutos):
        super().__init__(nombre, duracion, cobertura, precio)
        self.__tipo_llamadas = tipo_llamadas
        self.__minutos = minutos

    def calcular_importe(self):
        importe_final = super().getprecio()
        if "internacional" in self.__tipo_llamadas:
            importe_final *= 1.20
        if "larga distancia" in self.__tipo_llamadas:
            importe_final *= 1.20
        if "locales" in self.__tipo_llamadas:
            importe_final *= 0.925
        return importe_final
    