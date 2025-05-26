class Accidente():
    __tabla: list

    def __init__(self):
        self.__tabla=[] 

    def inicializar(self, filas, columnas):
        self.__tabla = [[0 for j in range(columnas)] for i in range(filas)]
    
    def cargar_tabla(self, depto, mes, cant):
        self.__tabla[depto-1][mes-1]+=cant

  
    def getCantidadDeAccidentes(self, id, mes):
        return self.__tabla[id-1][mes-1]
    
    
    def busquedaPorMes(self, id, mes):
        #for i in range (len(self.__tabla)):
            #print(f"Departamento: --- y la cantidad es: {self.__tabla[i][mes-1]}")
        cant=self.__tabla[id][mes]
        
        return cant