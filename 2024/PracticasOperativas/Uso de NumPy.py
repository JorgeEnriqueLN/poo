import numpy as np

class Objeto:
    __nombre: str
    __numero: int
    def __init__(self, nombre, numero):
        self.__nombre = nombre
        self.__numero = numero
    def __str__(self):
        return f"Nombre: {self.__nombre}, Numero: {self.__numero}"
    def getNombre(self):
        return self.__nombre
    def getNumero(self):
        return self.__numero


class ArregloDeObjetos:
    __cantidad: int #Guarda la cantidad de componentes utilizadas [x][x][x][x][x][x][x][x][x][ ][ ]
    __dimension: int #Cantidad de componentes totales de arreglo  [ ][ ][ ][ ][ ][ ][ ]
    __incremento = 5 #Para el resize
    __arregloObjetos: np.ndarray

    def __init__(self, dimension, incremento=5):
        self.__arregloObjetos = np.empty(dimension, dtype=Objeto)
        self.__cantidad = 0
        self.__incremento = incremento
        self.__dimension = dimension

    def agregarObjeto(self, unObjeto):
        if self. __cantidad == self.__dimension:
            self.__dimension = self.__dimension + self.__incremento
            self.__arregloObjetos.resize(self.__dimension)
        self.__arregloObjetos[self.__cantidad] = unObjeto
        self.__cantidad = self.__cantidad + 1

    def getObjeto(self, indice):
        return self.__arregloObjetos[indice]
    
    def listarObjetos(self):
        for i in range(self.__cantidad):
            print(self.__arregloObjetos[i])



objeto1 = Objeto("Juan", 234)
objeto2 = Objeto("Pedro", 111)
objeto3 = Objeto("Ana", 197)

array1 = ArregloDeObjetos(1)
array1.agregarObjeto(objeto1)
array1.agregarObjeto(objeto2)
array1.listarObjetos()
