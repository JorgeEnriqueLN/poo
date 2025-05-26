from gestorCliente import GestorC
from gestorMovimiento import GestorM

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Leer datos de Clientes y Movimientos
          [2] Leer Movimientos
          [3] Cargar
          [4] 
          [5] 
          [6] Mostrar
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    clientes=GestorC()
    movimientos=GestorM()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            
            clientes.cargaCliente()
            
            movimientos.cargaMovimiento()
            
            print('Se cargaron los clientes')
        elif opcion==2:
            #movimientos=Movimiento()
            movimientos.cargarMovimientos()
            print('Movimientos cargados')
        # elif opcion==3:
        #     movimientos.()
        # elif opcion==4:
        #     movimientos
        # elif opcion==5:
        #     movimientos.
        elif opcion==6:
            Cliente.mostrar
        else:
            print("Opcion Invalida")
        opcion=menu()