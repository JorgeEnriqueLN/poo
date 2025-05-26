from ClaseGestorC import GestorCabaña
from ClaseGestorR import GestorReservas

def menu():
    op= int(input("""
                MENU DE OPCIONES
[1] Mostrar el gestor de cabaña
[2] Mostrar el gestor de reservas
[3] Ingresar por teclado una cantidad de huéspedes y mostrar el o los números de las cabañas 
que tienen una capacidad igual o mayor a la cantidad ingresada y no tienen ninguna reserva 
registrada.
[4] Ingresar una fecha y emitir un listado con las reservas cuya fecha de inicio del hospedaje sea 
igual a la ingresada
[5] Ordenar arreglo
[6] Ordenar lista
[0] Salir 
        ----> """))
    return op

if __name__ == "__main__":
    gestorC = GestorCabaña()
    gestorR = GestorReservas()
    gestorC.cargar()
    gestorR.cargar()
    op = menu()
    while op!=0:
        if op == 1:
            gestorC.imprimir()
        elif op == 2:
            gestorR.imprimir()
        elif op == 3:
            cantidad = int(input("Ingrese la cantidad de huéspedes: "))
            gestorC.buscar_cabaña(cantidad, gestorR)
        elif op == 4:
            fecha= input("Ingrese fecha: ")
            gestorR.listado(fecha, gestorC)
        elif op==5:
            gestorC.ordenar_arreglo()
            gestorC.imprimir()
        elif op==6:
            gestorR.ordenar_lista()
            gestorR.imprimir()
        else:
            print("Opción no válida")
        op= menu()