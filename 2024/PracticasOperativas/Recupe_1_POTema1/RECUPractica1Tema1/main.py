from gestorCabaña import GestorC
from gestorReserva import GestorR
def menu():
    op=int(input("""
                 Menu de Opciones
    [1] Capacidad de Cabañas
    [2] Fechas de Hospedaje
    [0] Salir                
    --->"""))
    return op

if __name__ == '__main__':
    opcion=menu()
    GC=GestorC()
    GR=GestorR()

    GC.cargarCabañas()
    GR.carga()
    
    while opcion != 0:
        if opcion==1:
            GC.capacidad(GR)
            input("Presione Enter Para Continuar")
        elif opcion==2:
            GR.listado_reservas(GC)
            input("Presione Enter Para Continuar")
        else:
            input("Opcion Invalida")    
        opcion=menu()
    print("Tenga un Gran Dia") 