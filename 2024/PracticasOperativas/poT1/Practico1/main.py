from GestorCliente import Cliente
from GestorMovimiento import Movimiento

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Leer datos de Clientes
          [2] Leer Movimientos
          [3] Cargar
          [4] 
          [5] 
          [6] 
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
  
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            clientes=Cliente()
            clientes.cargaCliente()
            
            print('Se cargaron los clientes')
        elif opcion==2:
            movimientos=Movimiento()
            movimientos.cargarMovimientos()
            print('Movimientos cargados')
        elif opcion==3:
            movimientos.()
        elif opcion==4:
            movimientos
        elif opcion==5:
            movimientos.
        elif opcion==6:
            movimientos
        else:
            print("Opcion Invalida")
        opcion=menu()