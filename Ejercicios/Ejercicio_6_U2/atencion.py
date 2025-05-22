from datetime import datetime
class Atencion():

    __dni=int
    __fecha=datetime
    __importe=float

    def __init__(self, dni:int, fecha:datetime, importe:float):
        self.__dni=dni
        self.__fecha=fecha
        self.__importe=importe

    def __str__(self):
        return f'DNI: {self.__dni} Fecha: {self.__fecha} Importe: {self.__importe}'
    
    def getDni(self):
        return self.__dni
    def getFecha(self):
        return self.__fecha 
    def getImporte(self):
        return self.__importe