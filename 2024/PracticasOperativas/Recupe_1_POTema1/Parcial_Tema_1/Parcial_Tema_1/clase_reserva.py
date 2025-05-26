class reserva:
    __num:int
    __nombre:str
    __num_cab:int
    __fecha:str
    __huespedes:int
    __dias:str
    __importe:float
    def __init__(self,num,nom,nc,fe,hues,di,imp):
        self.__num=int(num)
        self.__nombre=nom
        self.__num_cab=int(nc)
        self.__fecha=fe
        self.__huespedes=int(hues)
        self.__dias=int(di)
        self.__importe=float(imp)
    def __str__(self):
        texto="Numero de Reserva {} Nombre de Huespes {} Numero de cabaña {} Fecha de Hospedaje {} Cantidad de huespedes {} Dias {} Importe de seña {}"
        return texto.format(self.__num,self.__nombre.replace(',',''),self.__num_cab,self.__fecha,self.__huespedes,self.__dias,self.__importe)
    def get_num(self):
        return self.__num_cab
    def get_fecha(self):
        return self.__fecha
    def get_dias(self):
        return self.__dias
    def get_seña(self):
        return self.__importe
    