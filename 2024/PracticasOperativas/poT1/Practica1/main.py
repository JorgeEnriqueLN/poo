from claseGestorCli import GestorClientes
from claseGestorMov import GestorMovimiento
from menu import menu

if __name__ == '__main__':
    a=GestorClientes()
    b=GestorMovimiento()
    a.carga()
    b.carga()
    Menu=menu()
    Menu.opciones(a,b)