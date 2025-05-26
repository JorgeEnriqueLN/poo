
class Movimiento:   
    __num_tarjeta:int
    __fecha:str
    __descripcion:str
    __tipo_mov:str
    __importe:int

    def __init__(self,nt,f,d,t,i):
        
        self.__num_tarjeta=nt
        self.__fecha=f
        self.__descripcion=d
        self.__tipo_mov=t
        self.__importe=i

    def getNumeroTarjeta(self):        
        return self.__num_tarjeta

    def getFecha(self):        
        return self.__fecha

    def getDescripcion(self):        
        return self.__descripcion

    def getTipoMov(self):       
        return self.__tipo_mov

    def getImporte(self):        
        return self.__importe
    