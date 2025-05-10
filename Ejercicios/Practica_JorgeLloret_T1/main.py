from manejadorCole import *
from manejadorTramo import *


def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Buscar tramo por dni del chofer
          [2] 
          [3] 
          [4] 
          [5] 
          [6] 
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    mc= ManejadorCole()
    mt= ManejadorTramo()
    mc.cargarColectivo()
    mt.cargarTramo()
 

    #mc.ordenar()

    opcion=menu()
    while opcion!=0:
        if opcion==1:
            dni=input("ingrese el dni del chofer:  ")
            pat=mc.buscarChofer(dni)
            print(f'Patente: {pat}')
            mt.mostrarTramos(pat)
            print('Operacion 1 Exitosa')

        elif opcion==2:
            
            mc.mostrar()
            print('Operacion 2 Exitosa')

        elif opcion==3:
            mt.mostrarListaTramos()
            
            print('Operacion 3 Exitosa')
        elif opcion==4:
            print('Operacion 4 Exitosa')
        elif opcion==5:
            print('Operacion 5 Exitosa')
        elif opcion==6:
            print('Operacion 6 Exitosa')
        else:
            print("Opcion Invalida")
        opcion=menu()
