class TarjetaSube:
    __saldo = int
    __numero = int

    def __init__(self, sal, nro):
        self.__saldo = sal
        self.__numero = nro

    def getSaldo(self): #este metodo devuelve el saldo de la tarjeta. En la clase se  llamo consultar_saldo (self)
        return self.__saldo

    def getNumero(self):
        return self.__numero
    
    def __str__(self):
        return f"Numero de tarjeta: {self.__numero} \nSaldo: {self.__saldo}"
     
    def Pagar_pasaje (self, importe):
        aux = 0
        if self.__saldo >= importe:
            self.__saldo -= importe
            aux = self.__saldo
        else:
            aux = self.__saldo -importe
        return (aux)
        
    def Cargar_saldo (self, importe):
        if (importe>0):
            self.__saldo += importe
        return (self.__saldo)   