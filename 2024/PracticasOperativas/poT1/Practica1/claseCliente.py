class Cliente:
    __nombre:str
    __apellido:str
    __dni:int
    __numT:int
    __saldoAnt:float

    def __init__(self, nom, app, dni, num, saldo) -> None:
        self.__nombre=nom
        self.__apellido=app
        self.__dni=dni
        self.__numT=num
        self.__saldoAnt=saldo

    def mostrar(self):
        print(f"{self.__nombre}, {self.__apellido}, {self.__numT}, {self.__saldoAnt}")

    def getDNI(self):
        return self.__dni
    
    def getNumT(self):
        return self.__numT
    
    def getNom(self):
        return self.__nombre
    
    def getApp(self):
        return self.__apellido 
    
    def getSaldo(self):
        return self.__saldoAnt
    
    def setSaldo(self, imp):
        self.__saldoAnt+=imp