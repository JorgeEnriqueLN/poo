from gestor import GestorA
from aAudio import Audio
from aAudiovisual import Audiovisual

def menu():
    gestor = GestorA()
    gestor.cargar_anuncios('anuncios.csv')
   
    
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar anuncio")
        print("2. Mostrar anuncio por título")
        print("3. Mostrar anuncios por resolución de video")
        print("4. Mostrar todos los anuncios")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            tipo = input("Ingrese el tipo de anuncio (AA-Audio, AV-Audiovisual): ")
            titulo = input("Ingrese el título: ")
            duracion = int(input("Ingrese la duración (en segundos): "))
            fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
            costo = float(input("Ingrese el costo por segundo: "))
            formato = input("Ingrese el formato del archivo: ")
            
            if tipo == 'AA':
                canal_audio = input("Ingrese el canal de audio (mono, estéreo, surround, etc.): ")
                anuncio = Audio(titulo, duracion, fecha_creacion, costo, formato, canal_audio)
            elif tipo == 'AV':
                resolucion_video = input("Ingrese la resolución del video (720p, 1080p, 1440p, 2160p, etc.): ")
                anuncio = Audiovisual(titulo, duracion, fecha_creacion, costo, formato, resolucion_video)
            
            gestor.agregar_anuncio(anuncio)
        
        elif opcion == 2:
            titulo = input("Ingrese el título del anuncio: ")
            gestor.mostrar_anuncio_por_titulo(titulo)
        
        elif opcion == 3:
            resolucion = input("Ingrese la resolución del video: ")
            gestor.mostrar_anuncios_por_resolucion(resolucion)
        
        elif opcion == 4:
            gestor.mostrar_todos_los_anuncios()
        
        elif opcion == 5:
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
