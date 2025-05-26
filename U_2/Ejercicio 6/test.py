from ClaseGestorAtenciones import GestorAtencion
from ClaseGestorPaciente import GestorPaciente

def opciones():
    op = int(input("""
                MENU DE OPCIONES
1. Mostrar Pacientes
2. Mostrar Atenciones
3. Leer por teclado una fecha, e informar las atenciones realizadas en dicha fecha y el 
importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha. 
4. Leer por teclado un dni, e informar Nombre y apellido, y cantidad de atenciones 
que tuvo. 
5. Listar nombre, apellido de los pacientes que no tuvieron ninguna atención 
6. Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad.
    -> """))
    return op

def test():
    gestorAtencion = GestorAtencion()
    gestorPaciente = GestorPaciente()
    gestorAtencion.cargar_atencion()
    gestorPaciente.cargar_pacientes()
    op = opciones()
    while(op != 0):
        if(op == 1):
            gestorPaciente.mostrar_pacientes()
        elif(op == 2):
            gestorAtencion.mostrar_atencion()
        elif(op == 3):
            fecha = input("Ingrese la fecha a buscar: ")
            total = gestorAtencion.buscar_importe_total(fecha)
            print(f"El importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha es: {total}")
        elif(op == 4):
            dni= int(input("Ingrese el DNI a buscar: "))
            gestorPaciente.buscar_dni(dni, gestorAtencion)
        elif(op == 5):
            gestorPaciente.listar_pacientes(gestorAtencion)
        elif(op == 6):
            gestorPaciente.ordenar_por_unidad()
        else:
            print("Opcion incorrecta")
        op = opciones()
    