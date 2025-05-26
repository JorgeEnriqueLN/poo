from abc import ABC, abstractmethod
class producto(ABC):
    __nombre:str
    __fecha_envasado:str
    __fecha_vencimiento:str
    __temp_recomendada:float
    __pais_origen:str
    __num_lote:str
    __costo_base:float
    def __init__(self,nom,fecha_e,fecha_v,tempR,pais,num_lote,costo_base):
        self.__nombre=nom
        self.__fecha_envasado=fecha_e
        self.__fecha_vencimiento=fecha_v
        self.__temp_recomendada=tempR
        self.__pais_origen=pais
        self.__num_lote=num_lote
        self.__costo_base=costo_base
    def __str__(self):
        return f"----------------------------\nnombre: {self.__nombre}\npais de origen: {self.__pais_origen}\ntemperatura ambiente recomendada: {self.__temp_recomendada}"
    @abstractmethod
    def mostrar_prod(self):
        pass
    def get_costo(self):
        return self.__costo_base
    def get_fecha_V(self):
        return self.__fecha_vencimiento