class TarjetaSube:
    __saldo = int
    __numero = int

    def __init__(self, sal, nro):
        self.__saldo = sal
        self.__numero = nro

    def getSaldo(self): #este metodo devuelve el saldo de la tarjeta. En la clase se llamo consultar_saldo (self)
        return self.__saldo

    def getNumero(self):
        return self.__numero
    
    def __str__(self):
        return f"Numero de tarjeta: {self.__numero} \nSaldo: {self.__saldo}"
     
    def Pagar_pasaje (self, importe):
        if self.__saldo >= importe:
            self.__saldo -= importe
            return (self.__saldo)
        else:
            return False
        
    def Cargar_saldo (self, importe):
        self.__saldo += importe
        return (self.__saldo)   
    
   
    
