from GestorEquipo import GestorE
# from gestorFecha import gestorF

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Leer datos de motos desde archivo csv
          [2] Leer datos de pedidos desde archivo csv
          [3] Cargar nuevo pedido
          [4] Modificar tiempo real de entrega
          [5] Mostrar datos de conductor y promedio de tiempo real de entrega
          [6] Mostrar comisiones de cada moto
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    #Recuerdo que todos los pedidos tienen tiempo de entrega real en 0 por defecto
    #Si se quiere modificar se debe usar la opcion 4 (sino se modifica afectara el promedio de la op 5)
    #Te recomiendo usar la opcion 6 para ver los datos precargados y las modificaciones que hagas
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            equipos=GestorE()
            equipos.cargar_equipo()