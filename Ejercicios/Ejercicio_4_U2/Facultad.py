class Facultad:
    __idF : int
    __nombre : str
    __direccion : str
    __localidad : str
    __telefono : str
    
    def __init__(self,idF,nombre,direccion,localidad,telefono):
        self.__idF = idF
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
    
    def getId(self):
        return self.__idF
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        return f"""\
            Código: {self.__idF}
            Nombre: {self.__nombre}
            Dirección: {self.__direccion}
            Localidad: {self.__localidad}
            Teléfono: {self.__telefono}"""