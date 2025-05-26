class Cliente:
    __nombre: str
    __apellido: str
    __dni: str
    __numTarjeta: int
    __saldoAnterior: float
    
    def __init__(self,nombre,apellido,dni,numTarjeta,saldoAnterior):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numTarjeta = numTarjeta
        self.__saldoAnterior = saldoAnterior
    
    # getters
    def get_nombre(self): return self.__nombre
    def get_apellido(self): return self.__apellido
    def get_dni(self): return self.__dni
    def get_numTarjeta(self): return self.__numTarjeta
    def get_saldoAnterior(self): return self.__saldoAnterior
    
    # setters
    def registrarPago(self,importe): self.__saldoAnterior -= importe
    def registrarCredito(self,importe): self.__saldoAnterior += importe