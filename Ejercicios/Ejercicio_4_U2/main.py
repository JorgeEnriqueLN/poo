from manejadorCarrera import *
from manejadorFacultad import *


def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Facultad donde se dicta la carrera
          [2] Mostrar
          [3] Listar
          [4] 
          [5] 
          [6] 
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    mf= ManejadorF()
    mc= ManejadorC()
    mc.cargarCarrera()
    mf.cargarFacultad()
 
    # este metodo ordena el arreglo alfabeticamente. esta asociado al método __lt__ declarado en la clase Carrera
    mc.ordenar()

    opcion=menu()
    while opcion!=0:
        if opcion==1:
            nombre=input("ingrese el nombre de la carrera:  ")
            idFac=mc.buscarCarrera(nombre)
            if (idFac != -1):
                print("Facultad:  ", mf.buscarFacultad(idFac))
            else:
                print("No se encontró")

            print('Operacion 1 Exitosa')

        elif opcion==2:
            mf.mostrarFac(mc)

            print('Operacion 2 Exitosa')

        elif opcion==3:
            facul=input("Ingrese el nombre de la facultad:  ")
            aux = mf.buscarFacultadPorNombre(facul)
            if (aux != -1):
                mc.listarOrdenado(aux)
        
            else:
                print("No se encontró nombre")
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
