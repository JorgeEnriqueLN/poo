from manejadorColectivo import *
from manejadorTramo import *


def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Buscar tramo por dni del chofer, punto 1
          [2] 
          [3] 
          [4] 
          [5] Calcula el combusltible utilizado. punto 2
          [6] Lista por distancia, punto 3
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    
    mt= ManejadorTramo()
    c=int(input("Ingrese cantidad de colectivos"))
    mc= ManejadorCole(c)
    mc.cargarColectivo()
    mt.cargarTramo()
 
 
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            #apartado 1 del practico
            dni=input("ingrese el dni del chofer:  ")
            pat=mc.buscarChofer(dni)
            print(f'Patente: {pat}')
            mt.mostrarTramos(pat)
           # print(f'Distancia total: {mt.mostrarTramos(pat)}')
            print('Operacion 1 Exitosa')

        elif opcion==2:
            
            mc.mostrar()
            print('Operacion 2 Exitosa')

        elif opcion==3:
            mt.mostrarListaTramos()
            
            print('Operacion 3 Exitosa')
        elif opcion==4:
            cole=int(input("Ingrese numero de colectivo: "))
            print(f'Colectivo datos {mc.getunColectivo(cole)}')
            print('Operacion 4 Exitosa')
        elif opcion==5:
            #apartado 2 del practico
            print("Los colectivos son: \n")

            mc.obtenerColectivos(mt)

            print('Operacion 5 Exitosa')
        elif opcion==6:
            #apartado 3 del practico
            distancia=int(input("Ingrese distancia: "))
            mt.listarDistancia(distancia)

            print('Operacion 6 Exitosa')
        else:
            print("Opcion Invalida")
        opcion=menu()
