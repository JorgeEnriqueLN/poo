class Departamento:
    __numero:int
    __nombre:str

    def __init__(self, nro, nombre):
        self.__numero=nro
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    def setNombre(self, otroNombre):
        return self.__nombre==otroNombre
    
    def getNumero(self):
        return self.__numero
    def setNumero(self, otroNro):
        return self.__nombre==otroNro
    
    def __str__(self):
        cadena= f"= Numero: {self.__numero} Nombre: {self.__nombre}"
        return cadena
    