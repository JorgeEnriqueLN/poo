class Colectivo():
    __combustible=35

    __patente=str
    __marca=str
    __modelo=int
    __capacidad=int
    __dni=int
    

    def __init__(self,patente:str,marca:str,modelo:int,capacidad:int,dni:int, combustible=35):
        self.__patente=patente
        self.__marca=marca
        self.__modelo=modelo
        self.__capacidad=capacidad
        self.__dni=dni
        self.__combustible=combustible

    def __str__(self):        
        return f'PATENTE: {self.__patente} MARCA: {self.__marca} MODELO: {self.__modelo} CAPACIDAD: {self.__capacidad} DNI CHOFER: {self.__dni} COMBUSTIBLE: {self.__combustible}'
    
    def getCombustible(self):
        return self.__combustible
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getCapacidad(self):
        return self.__capacidad
    def getDni(self):
        return self.__dni
    
  


