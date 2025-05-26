class Beneficiario:
    __dni : str
    __nombre : str
    __apellido : str
    __carrera : str
    __siglaFacultad : str
    __anioCursa : int
    __promedio : float
    __idBeca : int
    
    def __init__(self,dni,nombre,apellido,carrera,siglaFacultad,anioCursa,promedio,idBeca):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__siglaFacultad = siglaFacultad
        self.__anioCursa = anioCursa
        self.__promedio = promedio
        self.__idBeca = idBeca
    
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCarrera(self):
        return self.__carrera
    def getSiglaFacultad(self):
        return self.__siglaFacultad
    def getAnioCursa(self):
        return self.__anioCursa
    def getPromedio(self):
        return self.__promedio
    def getIdBeca(self):
        return self.__idBeca
    