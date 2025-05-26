#Ormeño Agustin / E010-270
class Movilidad:
    __patente: str
    __tipo: str
    __capacidad_carga: int
    __importe_mensual_patente: float
    __marca: str
    __modelo: str
    def __init__(self, patente: str, tipo: str, capacidad_carga: int, importe_mensual_patente: float, marca: str, modelo: str):
        self.__patente = patente
        self.__tipo = tipo
        self.__capacidad_carga = capacidad_carga
        self.__importe_mensual_patente = importe_mensual_patente
        self.__marca = marca
        self.__modelo = modelo
    def get_patente(self):
        return self.__patente
    def get_tipo(self):
        return self.__tipo
    def get_capacidad_carga(self):
        return self.__capacidad_carga
    def get_importe_mensual_patente(self):
        return self.__importe_mensual_patente
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def __str__(self):
        return f"Patente: {self.__patente}\nTipo: {self.__tipo}\nCapacidad de Carga: {self.__capacidad_carga}\nImporte Mensual Patente: {self.__importe_mensual_patente}\nMarca: {self.__marca}\nModelo: {self.__modelo}"
    