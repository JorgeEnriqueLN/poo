class Paciente():
    __dni=int
    __nombre=str
    __unidad=str

    def __init__(self, dni:int, nombre:str, unidad:str):
        self.__dni=dni
        self.__nombre=nombre
        self.__unidad=unidad

    def __str__(self):
        return f'DNI: {self.__dni} Nombre: {self.__nombre} Unidad: {self.__unidad}'
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):    
        return self.__nombre
    def getUnidad(self):
        return self.__unidad    
        