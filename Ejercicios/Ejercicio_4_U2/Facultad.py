class Facultad:
    __id: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: int

    def __init__(self, id, nombre, direccion, localidad, telefono):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono

    def _str_(self):
        #return "ID: {} - Nombre: {} - Direccion: {} - Localidad: {} - Telefono: {}".format(self._id, self.nombre, self.direccion, self.localidad, self._telefono)
        return f"ID: {self.__id} - Nombre: {self.__nombre} - Direccion: {self.__direccion} - Localidad: {self.__localidad} - Telefono: {self.__telefono}"
    
    def get_id(self):
       return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get__direccion(self):
        return self.__direccion
    
    def get_localidad(self):
        return self.__localidad
    
    def get_telefono(self):
        return self.__telefono
  