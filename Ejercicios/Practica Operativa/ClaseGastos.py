"""El archivo “movilidades.csv”, que contiene los datos de cada una de las movilidades, a saber:
patente, tipo (‘C’-Camión, ‘A’-Camioneta), capacidad de carga, importe mensual patente, marca
(‘Fiat’, ‘Ford’, ‘Peugeot’, etc.), modelo (‘Fiorino’, ‘F100’, etc.).
El archivo “gastosAbril2025.csv”, que contiene los datos de los gastos realizados para las
movilidades de la empresa, registra: patente, fecha, importe del gasto, descripción."""

class Gasto:
    __patente: str
    __fecha: str
    __importe_gasto: float
    __descripcion: str
    def __init__(self, patente: str, fecha: str, importe_gasto: float, descripcion: str):
        self.__patente = patente
        self.__fecha = fecha
        self.__importe_gasto = importe_gasto
        self.__descripcion = descripcion
    def get_patente(self):
        return self.__patente
    def get_fecha(self):
        return self.__fecha
    def get_importe_gasto(self):
        return self.__importe_gasto
    def get_descripcion(self):
        return self.__descripcion
    def __str__(self):
        return f"Patente: {self.__patente}\nFecha: {self.__fecha}\nImporte del Gasto: {self.__importe_gasto}\nDescripcion: {self.__descripcion}"
    def __lt__(self, otro):
        return (self.__fecha, self.__patente) < (otro.__fecha, otro.__patente)