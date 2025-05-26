class Reserva:
    __numReserva:int
    __nombre:str
    __numCabaña:int
    __fecha:str
    __huespedes:int
    __dias:str
    __importeSeña:float

    def __init__(self,numReserva,nombre,numCabaña,fecha,huespedes,dias,importeSeña):
        self.__numReserva=numReserva
        self.__nombre=nombre
        self.__numCabaña=numCabaña
        self.__fecha=fecha
        self.__huespedes=huespedes
        self.__dias=dias
        self.__importeSeña=importeSeña

    def getNumReserva(self):
        return self.__numReserva
    def getNombre(self):
        return self.__nombre
    def getNumCabaña (self):
        return self.__numCabaña
    def getFecha(self):
        return self.__fecha
    def getDias(self):
        return self.__dias
    def getImporteSeña(self):
        return self.__importeSeña
    
    def __str__(self):
        texto="Numero de Reserva {} Nombre de Huespes {} Numero de cabaña {} Fecha de Hospedaje {} Cantidad de huespedes {} Dias {} Importe de seña {}"
        return texto.format(self.__numReserva,self.__nombre.replace(',',''),self.__numCabaña,self.__fecha,self.__huespedes,self.__dias,self.__importeSeña)
    