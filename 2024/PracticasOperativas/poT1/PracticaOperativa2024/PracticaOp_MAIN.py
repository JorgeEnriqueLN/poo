from GestorClientes import GestorClientes
from GestorMovimientos import GestorMovimientos
# from colorama import Style

def test():
    movimientosManager = GestorMovimientos()
    clientesManager = GestorClientes()
    clientesManager.leerClientes_desde_csv("ClientesAbril2024.csv")
    movimientosManager.leerMovimientos_desde_csv("MovimientosAbril2024.csv")
    
    opcion = None
    while opcion != '4':
        print("1. Actualizar el saldo de un cliente")
        print("2. Verificar si un cliente tuvo movimientos en el mes a partir de numero de tarjeta")
        print("3. Ordenar datos de movimientos por numero de tarjeta")
        
        opcion = input('\n\n>>>> ')
        
        if opcion == '1':
            dni = input('Ingrese el dni del cliente a actualizar: ')
            if(clientesManager.actualizarCliente(dni,movimientosManager.get_movimientosCopia()) == 'NoEncontrado'):
                print("El dni ingresado no corresponde a ningun cliente en el sistema")
        
        elif opcion == '2':
            tarjeta = int(input('Ingrese la tarjeta para verificar si tuvo movimientos: '))
            movimientosManager.verificarMovimientos(tarjeta,clientesManager.get_listaClientesCopia())
        
        elif opcion  == '3':
            movimientosManager.ordenarPorTarjeta()
            print("Los movimientos se ordenaron con exito")
        elif opcion == '4':
            pass
        
        else: 
            print( "La opcion ingresada no es valida")

if __name__ == '__main__':
    test()