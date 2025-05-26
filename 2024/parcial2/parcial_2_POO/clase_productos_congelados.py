from clase_producto import producto
class producto_congelado(producto):
    __nitrogeno:int
    __oxigeno:int
    __dioxido_de_carbono:int
    __vapor_de_agua:int
    __metodo_congelacion:str
    def __init__(self,nom,fecha_e,fecha_v,tempR,pais,num_lote,costo_base,nitro,oxi,dioxi,vapor,metodo):
        super().__init__(nom,fecha_e,fecha_v,tempR,pais,num_lote,costo_base)
        self.__nitrogeno=nitro
        self.__oxigeno=oxi
        self.__dioxido_de_carbono=dioxi
        self.__vapor_de_agua=vapor
        self.__metodo_congelacion=metodo
    def importe_venta(self):
        return super().get_costo()*1.15
    def mostrar_prod(self):
        print(super().__str__(),f"\nimporte de venta: {self.importe_venta():.2f}\n----------------------------\n")
