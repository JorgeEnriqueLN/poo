class Movimiento:
    __numT:int
    __fecha:str
    __desc:str
    __tipo:str
    __imp:float

    def __init__(self, num, fecha, desc, tipo, imp) -> None:
        self.__numT=num
        self.__fecha=fecha
        self.__desc=desc
        self.__tipo=tipo
        self.__imp=imp

    def mostrar(self):
        print(f"{self.__numT}, {self.__fecha}, {self.__tipo}, {self.__imp}")

    def getNumT(self):
        return self.__numT
    
    def getTipo(self):
        return self.__tipo
    
    def getImp(self):
        return self.__imp
    
    def getFecha(self):
        return self.__fecha
    
    def getDesc(self):
        return self.__desc
    
    def __lt__(self, other):
        return self.__numT<other
    
    def __gt__(self, other):
        return self.__numT>other
    
