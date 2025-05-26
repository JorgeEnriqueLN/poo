from anuncio import Anuncio

class Audiovisual(Anuncio):
    def __init__(self, titulo, duracion, fecha_creacion, costo, formato, resolucion):
        super().__init__(titulo, duracion, fecha_creacion, costo, formato)
        self.__resolucion_video = resolucion
    
    def calcular_costo_total(self):
        costo_total = super().getcosto()* super().getduracion()
        if self.__resolucion_video == '1440':
            #costo_total = (super().getcosto * 1,015) * super().getduracion   # 1,5% -----> 1,5/100= 0,015 
            costo_total *= 1.015
            return costo_total
        elif self.__resolucion_video == '1080':
            #costo_total = (super().getcosto * 1,01) * super().getduracion   
            costo_total *= 1.01
            return costo_total
        else:
            return costo_total
        
    def getresolucion_video(self):
        return self.__resolucion_video


