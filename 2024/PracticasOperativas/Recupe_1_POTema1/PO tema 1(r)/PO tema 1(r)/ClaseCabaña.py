class cabaña:
    __numero: int
    __habitaciones: int
    __camas_grandes: int
    __camas_chicas: int
    __importe_dia: float

    def __init__(self, numero: int, habitaciones: int, camas_grandes: int, camas_chicas: int, importe_dia:float):
        self.__numero = numero
        self.__habitaciones = habitaciones
        self.__camas_grandes = camas_grandes
        self.__camas_chicas = camas_chicas
        self.__importe_dia = importe_dia

    def get_numero(self):
        return self.__numero
    
    def get_habitaciones(self):
        return self.__habitaciones
    
    def get_camas_grandes(self):
        return self.__camas_grandes
    
    def get_camas_chicas(self):
        return self.__camas_chicas
    
    def get_importe_dia(self):
        return self.__importe_dia

    def __lt__(self, otro):
        return self.__numero < otro.__numero

    def __ge__(self, cantidad):
        capacidad= (self.__camas_grandes * 2) + self.__camas_chicas
        return capacidad>=cantidad
    
    def __str__(self):
        return f"Cabaña {self.__numero} tiene {self.__habitaciones} habitaciones, {self.__camas_grandes} camas grandes y {self.__camas_chicas} camas chicas, y un importe diario de {self.__importe_dia}$"