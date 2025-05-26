from claseEquipos import equipo

class pesada(equipo):
    __tipoM: str
    __peso: float
    def __init__(self, mar, mod, anio, tipo, pote, cap, tar, dias, **kwargs):
        super().__init__(mar, mod, anio, tipo, pote, cap, tar, dias)
        self.__tipoM=kwargs['tipoM']
        self.__peso=kwargs['peso']
    def tarifa(self):
        x=0
        if self.__peso<=10:
            x=super().getTarifa()*super().getDias()
        else:
            x=(super().getTarifa()*super().getDias())+(super().getTarifa()*super().getDias())*0.2
        return x