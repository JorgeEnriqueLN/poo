class Atencion:
    __dni: int
    __fecha: str
    __importe_atencion: float
    def __init__(self, dni: int, fecha: str, importe_atencion: float):
        self.__dni = dni
        self.__fecha = fecha
        self.__importe_atencion = importe_atencion
    def get_dni(self):
        return self.__dni
    def get_fecha(self):
        return self.__fecha
    def get_importe_atencion(self):
        return self.__importe_atencion
    def __str__(self):
        return f"DNI: {self.__dni}\nFecha: {self.__fecha}\nImporte de atencion: {self.__importe_atencion}"
    