class Cabaña:
    __numero: int
    __cantHabitaciones: int
    __camasGrandes: int
    __camasChicas: int
    __importe:float

    def __init__(self, numero, cantHabitaciones, camasGrandes, camasChicas, importe) -> None:
        self.__numero=int(numero)
        self.__cantHabitaciones=int(cantHabitaciones)
        self.__camasGrandes=int(camasGrandes)
        self.__camasChicas=int(camasChicas)
        self.__importe=float(importe)

    def getNumero(self):
        return self.__numero

    def getCantHabitaciones (self):
        return self.__cantHabitaciones

    def get_importe(self):
        return self.__importe    
    
    def __ge__(self,other):
        return (self.__camasGrandes * 2 + self.__camasChicas) >= other
    
    def __str__(self):
        texto="Numero de Cabaña  {}  Habitaciones  {}  Camas Grandes  {}  Camas Chicas  {}  Importe {}"
        return texto.format(self.__num,self.__habitaciones,self.__camas_grandes,self.__camas_chicas,self.__importe)