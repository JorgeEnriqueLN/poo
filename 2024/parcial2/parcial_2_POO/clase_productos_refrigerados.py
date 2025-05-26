from clase_producto import producto
import datetime
class producto_refrigerado(producto):
    __cod_organismo_supervision:str
    def __init__(self,nom,fecha_e,fecha_v,tempR,pais,num_lote,costo_base,cod):
        super().__init__(nom,fecha_e,fecha_v,tempR,pais,num_lote,costo_base)
        self.__cod_organismo_supervision=cod
    def importe_venta(self):
        mesV=super().get_fecha_V()
        mesV=int(mesV.split("/")[1])
        fechaA=datetime.date.today()
        imp=0
        if mesV-fechaA.month<=2:
            imp=super().get_costo()*0.9
        else:
            imp=super().get_costo()*1.01
        return imp
    def mostrar_prod(self):
        print(super().__str__(),f"\nimporte de venta: {self.importe_venta():.2f}\n---------------------------- {datetime.date.today()}\n")