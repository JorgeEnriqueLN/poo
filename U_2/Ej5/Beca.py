class Beca:
    __idBeca : int
    __tipo : str
    __importe: float
    
    def __init__(self,idBeca,tipo,importe):
        self.__tipo = tipo
        self.__importe = importe
        self.__idBeca = idBeca
    def getTipo(self):
        return self.__tipo
    def getImporte(self):
        return self.__importe
    def getIdBeca(self):
        return self.__idBeca
    