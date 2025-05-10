from manejadorDepto import ManejadorD
from Accidente import Accidente

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Carga
          [2] Mostrar
          [3] Cantidad
          [4] 
          [5] 
          [6] 
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
    md=ManejadorD()
    md.cargarDeptos()
    acc=Accidente()
    acc.inicializar(19,12)
    

    opcion=menu()
    while opcion!=0:
        if opcion==1:
            dep=int(input("Ingrese numero de departamento"))
            mes=int(input("Ingrese numero de mes"))
            cantAcc=int(input("Ingrese cantidad de accidentes"))
            acc.cargar_tabla(dep,mes,cantAcc)

            print('Operacion 1 Exitosa')
        elif opcion==2:
            id=int(input("Ingrese id del departamento"))
            nom=md.GetNombreEnListaDepartamentos(id-1)
            print(f"Departamento: {nom}")
            print('Operacion 2 Exitosa')
        elif opcion==3:
            d=int(input("Ingrese depto"))
            m=int(input("Ingrese mes"))
            can=acc.getCantidadDeAccidentes(d,m)
            print(f"La cant es:   {can}")
            print(f"DEPARTAMENTO: {md.GetNombreEnListaDepartamentos(d-1)}")

            print('Operacion 3 Exitosa')
        elif opcion==4:
            mes=int(input("Ingrese mes a buscar"))
                   
            for i in range (19):
                print(f"Departamento: {md.GetNombreEnListaDepartamentos(i)} cantidad: {acc.busquedaPorMes(i,mes-1)}")
            print('Operacion 4 Exitosa')
        elif opcion==5:
            print('Operacion 5 Exitosa')
        elif opcion==6:
           print('Operacion 6 Exitosa')
        else:
            print("Opcion Invalida")
        opcion=menu()
