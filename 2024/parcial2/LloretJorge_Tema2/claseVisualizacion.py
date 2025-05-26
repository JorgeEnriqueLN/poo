class Visualizacion:
    __id_miembro: int
    __id_pelicula: str
    __fecha: str
    __hora: str
    __minutos: int
  

    def __init__(self, id_miembro, id_pelicula, fecha, hora, minutos) -> None:
        self.__id_miembro=id_miembro
        self.__id_pelicula=id_pelicula
        self.__fecha=fecha
        self.__hora=hora
        self.__minutos=minutos

    def get_id_miembro(self):
        return self.__id_miembro
    
    def get_id_pelicula(self):
        return self.__id_pelicula
    
    def get_fecha(self):
        return self.__fecha
    
    def get_hora(self):
        return self.__hora
    
    def get_minutos(self):
        return self.__minutos
    