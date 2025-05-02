class Carrera:
    __idC : int
    __nombre : str
    __titulo : str
    __duracion : str
    __nivel :  str
    __codigoFacultad : int
    
    def __init__(self, idC,nombre,titulo,duracion,nivel,codigoFacultad):
        self.__idC = idC
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__nivel = nivel
        self.__codigoFacultad = codigoFacultad

    def getIdC(self):
        return self.__idC
        
    def getNombre(self):
        return self.__nombre
    
    def getTitulo(self):
        return self.__titulo
    
    def getNivel(self):
        return self.__nivel
    
    def getDuracion(self):
        return self.__duracion
    
    def getCodigoFacultad(self):
        return self.__codigoFacultad
        
    def __str__(self):
        return f"""\
            Id: {self.__idC}, 
            Nombre: {self.__nombre},
            Nivel: {self.__nivel},
            Duracion: {self.__duracion}, 
            Titulo: {self.__titulo},
            CodigoFacultad: {self.__codigoFacultad}"""
    
    # método para ordenar las carreras en orden
    def __lt__(self,otroNombre):
        return (self.__nombre<otroNombre.getNombre())

    
    
