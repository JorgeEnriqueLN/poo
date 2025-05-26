class Equipo:
    __idEquipo = int
    __nombre = str
    __golesAFavor = int
    __golesEnContra = int
    __difGoles = int
    __puntos = int
    
    def __init__(self, idEquipo, nombre, golesAFavor, golesEnContra, difGoles, puntos):
        self.__idEquipo = idEquipo
        self.__nombre = nombre
        self.__golesAFavor = golesAFavor
        self.__golesEnContra = golesEnContra
        self.__difGoles = difGoles
        self.__puntos = puntos
        
    def getIdEquipo(self):
        return self.__idEquipo
    
    def getNombre(self):
        return self.__nombre
    
    def getGolesAFavor(self):
        return self.__golesAFavor
    
    def getGolesEnContra(self):
        return self.__golesEnContra
    
    def getDifGoles(self):
        return self.__difGoles
    
    def getPuntos(self):
        return self.__puntos