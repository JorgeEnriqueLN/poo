class Movimiento:
    __numTarjeta: int
    __fecha: str
    __descripcion: str
    __tipo: str
    __importe: float
    
    def __init__(self,numTarjeta,fecha,descripcion,tipo,importe):
        self.__numTarjeta = numTarjeta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipo = tipo
        self.__importe = importe
    
    # getters
    def get_numTarjeta(self): return self.__numTarjeta
    def get_fecha(self): return self.__fecha
    def get_descripcion(self): return self.__descripcion
    def get_tipo(self): return self.__tipo
    def get_importe(self): return self.__importe

    # sobrecarga de metodo
    def __lt__(self,other):
        return self.__numTarjeta < other.__numTarjeta