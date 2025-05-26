from manejadorPaciente import *
from manejadorAtencion import *


def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] 
          [2] 
          [3] 
          [4] 
          [5] 
          [6] 
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    
    mP=ManejadorPaciente()
    mA=ManejadorAtencion()
    mP.cargarPacientes()
    mA.cargarAtencion()

 
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            fec=(input("Ingrese la fecha de atencion: "))
            mA.atencionesRealizadas(fec)
            print('Operacion 1 Exitosa')

        elif opcion==2:
            mA.mostrar()
          
            print('Operacion 2 Exitosa')

        elif opcion==3:
            dni=int(input("Ingrese dni del paciente: "))
            mP.buscarPaciente(dni) 
            mA.buscarAtencion(dni)
             
            
            print('Operacion 3 Exitosa')
        elif opcion==4:
            mA.buscarPorDni(mP)

            print('Operacion 4 Exitosa')
        elif opcion==5:
            
            print("Los colectivos son: \n")

            

            print('Operacion 5 Exitosa')
        elif opcion==6:
           

            print('Operacion 6 Exitosa')
        else:
            print("Opcion Invalida")
        opcion=menu()
