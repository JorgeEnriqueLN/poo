class cabana:
    __num:int
    __habitaciones:int
    __camas_grandes:int
    __camas_chicas:int
    __importe:str
    def __init__(self,num,hab,gran,chic,imp):
        self.__num=int(num)
        self.__habitaciones=int(hab)
        self.__camas_grandes=int(gran)
        self.__camas_chicas=int(chic)
        self.__importe=float(imp)
    def __str__(self):
        texto="Numero de Cabaña  {}  Habitaciones  {}  Camas Grandes  {}  Camas Chicas  {}  Importe {}"
        return texto.format(self.__num,self.__habitaciones,self.__camas_grandes,self.__camas_chicas,self.__importe)
    def __ge__(self,other):
        return (self.__camas_grandes * 2 + self.__camas_chicas) >= other
    def get_num(self):
        return self.__num
    def get_importe(self):
        return self.__importe