from claseEquipos import equipo

class electrica(equipo):
    __carga: str
    def __init__(self, mar, mod, anio, tipo, pote, cap, tar, dias, car):
        super().__init__(mar, mod, anio, tipo, pote, cap, tar, dias)
        self.__carga=car
    def tarifa(self):
        x=0
        if self.__carga=='bateria':
            x=(super().getTarifa()*super().getDias())+(super().getTarifa()*super().getDias())*0.2
        else:
            x=super().getTarifa()*super().getDias()
        return x
    