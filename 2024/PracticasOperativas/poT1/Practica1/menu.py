class menu:
    def __init__(self) -> None:
        pass

    def opciones(self, gestorCli, gestorMov):

        print("""
            a. Actualizar Saldo por DNI.
            b. Verificar si el cliente no tuvo movimientos durante el mes de abril.
            c. Ordenar Gestor de Movimientos por numero de tarjeta.
            d. Salir
        """)
        k=0
        while k!=1:
            k=input("\tIngrese una opcion: ")

            if k == "a":
                gestorCli.actualizar(gestorMov)

            elif k == "b":
                gestorCli.movimientosAbril(gestorMov)

            elif k == "c":
                gestorMov.ordenar()
                print("\nArreglo ordenado: ")
                gestorMov.mostrar()
            
            elif k == "d":
                k=1

            else:
                print("\nOpcion incorrecta.")
            