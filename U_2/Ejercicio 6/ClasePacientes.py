class Paciente:
    __dni: int
    __nombre: str
    __unidad: str
    def __init__(self, dni: int, nombre: str, unidad: str):
        self.__dni = dni
        self.__nombre = nombre
        self.__unidad = unidad
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_unidad(self):
        return self.__unidad
    def __str__(self):
        return f"DNI: {self.__dni}\nNombre: {self.__nombre}\nUnidad: {self.__unidad}"
    
    def __lt__(self, otro):
        return (self.__unidad, self.__nombre) < (otro.__unidad, otro.__nombre)
