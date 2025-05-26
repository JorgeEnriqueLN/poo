from gestorMiembro import GestorM
from gestorvisualizacion import GestorV
def menu():
    op=int(input("""
                 Menu de Opciones
    [1] Ingrese el correo del miembro para ver los minutos de películas
    [2] Visualizaciones simultaneas
    [0] Salir                
    --->"""))
    return op

if __name__ == '__main__':
    opcion=menu()
    GM=GestorM()
    GV=GestorV()

    GM.cargarMiembros()
    GV.carga()
    
    while opcion != 0:
        if opcion==1:
            GM.min_vistos(GV)
            input("Presione Enter Para Continuar")
        elif opcion==2:
            GV(GM)
            input("Presione Enter Para Continuar")
        else:
            input("Opcion Invalida")    
        opcion=menu()
    print("Gracias") 