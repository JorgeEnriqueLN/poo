class Punto:
    __x: int
    __y: int
    
    def inicializar(self, v1: int, v2: int):
        self.__x = v1
        self.__y = v2
    
    def setX(self, v1: int):
        self.__x = v1   
    
    def setY(self, v2: int):
        self.__y = v2

    def getX(self) -> int:
        return self.__x
    
    def getY(self) -> int:
        return self.__y
    
    def mostrarDatos(self):
        print("(x,y)=(", self.__x,',', self.__y,")")

if __name__=='__main__':
    unPunto = Punto()
    otroPunto = Punto()
    unPunto.inicializar(3,4)
    otroPunto.inicializar(4,7)
    unPunto.mostrarDatos()
    otroPunto.mostrarDatos()
