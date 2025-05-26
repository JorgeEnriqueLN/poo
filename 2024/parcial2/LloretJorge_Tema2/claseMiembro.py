class Miembro:
    __id_miembro: int
    __ayn: str
    __correo: str

    def __init__(self, id, ayn, correo) -> None:
        self.__id_miembro=id
        self.__ayn=ayn
        self.__correo=correo

    def get_id_miembro(self):
        return self.__id_miembro
    
    def get_ayn(self):
        return self.__ayn
    
    def get_correo(self):
        return self.__correo
    
    