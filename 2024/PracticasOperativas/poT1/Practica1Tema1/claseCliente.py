
class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __nro_tarjeta: int
    __saldo: int

    def __init__ (self, n, a, d, nt, s):
        self.__nombre= n
        self.__apellido=a
        self.__dni= d
        self.__nro_tarjeta= nt
        self.__saldo= s

    def get_Nombre(self):
        return self.__nombre
    
    def get_Apellido(self):
        return self.__apellido

    def get_Dni(self):
        return self.__dni

    def get_NroTarjeta(self):        
        return self.__nro_tarjeta

    def get_Saldo(self):    
        return self.__saldo
    
    def mostrar(self):
        print(f"{self.__nombre},{self.__apellido},{self.__dni},{self.__nro_tarjeta},{self.__saldo}")