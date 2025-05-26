from claseTarjetaSube import TarjetaSube
class Controlador():
    __tarjetas:list

    def __init__(self):
        self.__tarjetas=[]

    def agregar_tarjetas(self, tarje):  #inciso 1
        self.__tarjetas.append(tarje)

    def mostrar_tarjetas(self): #inciso 2
        for t in self.__tarjetas:
            if (t.getSaldo()<0):
                print(t)

#este codigo tiene el problema que cada vez que pasa por un objeto y no es el buscado muestra el mensaje tantas veces como se itere hasta encontrar la tarjeta correcta. 
#por lo que no es óptimo, para resolver esto lo hago en el otro bloque, método buscar tarjeta
    def buscar_tarjeta (self,numerosube):
        i=0
        encontrado=False
        while(i < len(self.__tarjetas) and encontrado==False):
            if(self.__tarjetas[i].getNumero() == numerosube):
                encontrado=True
                print (f"El saldo es: {self.__tarjetas[i].getSaldo()} y el numero de tarjeta es {self.__tarjetas[i].getNumero()}")
            i+=1
        if encontrado==False:    
            print ("No se encontro la tarjeta con el numero:", numerosube)
            
        
    # def buscar_tarjeta (self,numerosube):
    #     i=0
    #     encontrado=False
    #     while(i != len(self.__tarjetas) and encontrado==False):
    #         if(self.__tarjetas[i].getNumero() == numerosube):
    #             encontrado=True
    #         i+=1
    #     return int(i+1)
        
    # def tamano_lista(self):
    #     return int(len(self.__tarjetas))