from anuncio import Anuncio

class Audio(Anuncio):
    def __init__(self, titulo, duracion, fecha_creacion, costo, formato, canal_audio):
        super().__init__(titulo, duracion, fecha_creacion, costo, formato)
        self.__canal_audio = canal_audio
    
    def calcular_costo_total(self):
        costo_total = super().getcosto() * super().getduracion()
        if self.__canal_audio == 'surround':
            #costo_total = (super().getcosto * 1,005) * int(super().getduracion)   # 0,5% -----> 0,5/100= 0,005
            costo_total *= 1.005
            return costo_total
        elif self.__canal_audio == 'mono':
            #costo_total = (super().getcosto * 1,001) * (super().getduracion)
            costo_total *= 1.001
            return costo_total
        else:
            return costo_total


    def getcanal_audio(self):
        return self.__canal_audio

