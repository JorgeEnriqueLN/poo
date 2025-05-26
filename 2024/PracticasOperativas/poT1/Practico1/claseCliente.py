"""Práctico 1 - POO"""

class Cliente:
    __nombre:str
    __apellido:str
    __dni:str
    __num_tarj:int
    __saldo:int

    def __init__(self,n,a,dni,numt,s):
        self.__nombre=n
        self.__apellido=a
        self.__dni=dni
        self.__num_tarj=numt
        self.__saldo=s

    def getNombre(self):
        return self.__nombre

    def getApellido(self):    
        return self.__apellido

    def getDni(self):
        return self.__dni

    def getConductor(self):        
        return self.__num_tarj

    def getKilometraje(self):    
        return self.__saldo
    
    def setSaldoActual(self,sal):
        self.__saldo=sal
        print('Saldo actualizado')