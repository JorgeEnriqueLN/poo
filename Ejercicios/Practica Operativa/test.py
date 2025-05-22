#Ormeño Agustin / E010-270
from ClaseGestorMovilidad import GestorMovilidad
from ClaseGestorGasto import GestorGasto

def opciones():
    op = int(input("""
                MENU DE OPCIONES
1. Mostrar Movilidades
2. Mostrar Gastos
3. Leer por teclado la patente de una movilidad, si no existe, emitir un mensaje de error, si
existe listar los gastos que ha tenido en el mes de abril, indicando el total de gastos. El
listado deberá tener el siguiente formato:
Patente: xx-xxx-xx Tipo: XXXXXXXXXX Capacidad de Carga:xxxx
Importe Mensual de Patente: xxxxxxx Marca: xxxxxxxxxxx Modelo: xxxxxxx
Gastos
Fecha Importe Descripción
xx/xx/xxxx xxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xx/xx/xxxx xxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xx/xx/xxxx xxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Total de Gastos (incluye Patente): xxxxxxxx
4. Dada una fecha, indicar los gastos que se produjeron ese día, indicando el total general a
pagar.
5. Dada una fecha, indicar para cada movilidad, patente, marca, modelo y total a pagar. Para
resolver este punto, debe ordenar el Gestor de Gastos de menor a mayor, por fecha y
patente, debiendo sobrecargar el operador correspondiente en la clase Gasto. La
funcionalidad deberá hacer uso eficiente del Gestor para el cálculo del gasto.
0. Salir
    -> """))
    return op

def test():
    gestorMovilidad = GestorMovilidad()
    gestorGasto = GestorGasto()
    gestorMovilidad.cargar_movilidad()
    gestorGasto.cargar_gasto()
    op = opciones()
    while(op != 0):
        if(op == 1):
            gestorMovilidad.mostrar_movilidad()
        elif(op == 2):
            gestorGasto.mostrar_gasto()
        elif(op == 3):
            patente = input("Ingrese Patente: ")
            gestorMovilidad.buscar_patente(patente, gestorGasto)
        elif(op == 4):
            fecha = input("Ingrese Fecha a buscar: ")
            gestorGasto.buscar_fecha(fecha)
        elif(op == 5):
            fecha = input("Ingrese Fecha a buscar: ")
            gestorGasto.listar_ordenado(fecha, gestorMovilidad)
        else:
            print("Opcion incorrecta")
        op = opciones()