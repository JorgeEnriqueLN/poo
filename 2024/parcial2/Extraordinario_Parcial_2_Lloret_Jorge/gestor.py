import csv
from aAudio import Audio
from aAudiovisual import Audiovisual

class GestorA:
    def __init__(self):
        self.__lista_A = []

    
    def cargar_anuncios(self, archivo):
        with open(archivo, newline='') as arch:
            reader = csv.reader(arch, delimiter=';')
            next (reader)
            for fila in reader:
                tipo = fila[0]
                titulo = fila[1]
                duracion = int(fila[2])
                fecha_creacion = fila[3]
                costo = float(fila[4])
                formato = fila[5]
                
                if tipo == 'AA':
                    canal_audio = fila[6]
                    anuncio = Audio(titulo, duracion, fecha_creacion, costo, formato, canal_audio)
                elif tipo == 'AV':
                    resolucion_video = fila[6]
                    anuncio = Audiovisual(titulo, duracion, fecha_creacion, costo, formato, resolucion_video)
                
                self.__lista_A.append(anuncio)

          
    
    def agregar_anuncio(self, anuncio):
        self.__lista_A.append(anuncio)
    
    def mostrar_anuncio_por_titulo(self, titulo):
        for anuncio in self.__lista_A:
            if anuncio.gettitulo() == titulo:
                if isinstance(anuncio, Audio):
                    print(f'Tipo: Audio, Formato: {anuncio.getformato()}, Canal: {anuncio.getcanal_audio()}')
                elif isinstance(anuncio, Audiovisual):
                    print(f'Tipo: Audiovisual, Formato: {anuncio.getformato()}, Resolución: {anuncio.getresolucion_video()}')
    
    def mostrar_anuncios_por_resolucion(self, resolucion):
        for anuncio in self.__lista_A:
            if isinstance(anuncio, Audiovisual) and anuncio.getresolucion_video() == resolucion:
                print(f'Título: {anuncio.gettitulo()}')
    
    def mostrar_todos_los_anuncios(self):
        for anuncio in self.__lista_A:
            anuncio.mostrar_info()
