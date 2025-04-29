class Carrera():
    __codigo:int
    __nombre:str
    __duracion:int
    __nivel:str
    __codigoFacultad:int

    def __init__(self,cod,nomb,duracion,titulo,codFacultad):
        self.__codigo=cod
        self.__nombre=nomb
        self.__duracion=duracion
        self.__nivel=titulo
        self.__codigoFacultad=codFacultad

    def __lt__(self, otro):
        return self.__codigo < otro.__codigo

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDuracion(self):
        return self.__duracion

    def getNivel(self):
        return self.__nivel

    def getCodigoFacu(self):
        return self.__codigoFacultad