class Tramo():
    __origen=str
    __destino=str
    __distancia=int
    __patente=str


    def __init__(self,origen:str,destino:str,distancia:int,patente:str):
        self.__origen=origen
        self.__destino=destino
        self.__distancia=distancia
        self.__patente=patente

    def __str__(self):        
        return f'Patente: {self.__patente} Desde: {self.__origen} Hasta: {self.__destino} Distancia: {self.__distancia}'
    
    def getOrigen(self):
        return self.__origen
    def getDestino(self):
        return self.__destino
    def getDistancia(self): 
        return self.__distancia
    def getPatente(self):
        return self.__patente
    
    def setOrigen(self,origen:str):
        return self.__origen==origen
    def setDestino(self,destino:str):
        return self.__destino==destino
    
    def __gt__(self, otro):
        return int(self.__distancia) > otro

    