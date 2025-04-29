from claseTarjetaSube import TarjetaSube
class Controlador():
    __tarjetas:list

    def __init__(self):
        self.__tarjetas=[]

    def agregar_tarjetas(self, tarjeta_sube):  #inciso 1
        self.__tarjetas.append(tarjeta_sube)

    def mostrar_tarjetas(self): #inciso 2
        for tarjeta in self.__tarjetas:
            if (tarjeta.getSaldo()<0):
                print(tarjeta)

    def buscar_tarjeta(self, nro): #inciso 3
        pass 