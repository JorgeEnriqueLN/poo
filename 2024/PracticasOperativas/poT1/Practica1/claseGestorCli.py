import csv
from claseCliente import Cliente

class GestorClientes:
    __gestor:list

    def __init__(self) -> None:
        self.__gestor=[]

    def carga(self):
        archivo = open('ClientesAbril2024.csv')
        reader = csv.reader(archivo, delimiter=";")
        band=False
        for fila in reader:
            if not band:
                band=True
            else:
                cliente = Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4]))
                self.__gestor.append(cliente)

    def mostrar(self):
        for cli in self.__gestor:
            cli.mostrar()

    def actualizar(self, gestorM):
        dni=int(input("\nIngrese DNI: "))
        for cliente in self.__gestor:
            if cliente.getDNI()==dni:
                num=cliente.getNumT()
                saldoant=cliente.getSaldo()
                importe = gestorM.actImp(num)
                cliente.setSaldo(importe)
                gestorM.mostrarCliente(cliente.getNom(), 
                                       cliente.getApp(),
                                       num,
                                       saldoant,
                                       cliente.getSaldo()
                                       )
                
    def movimientosAbril(self, gestorM):
        num=int(input("\nIngrese Numero de Tarjeta: "))
        for cliente in self.__gestor:
            if cliente.getNumT()==num:
                if gestorM.Mov(num):
                    print(f"\nNombre: {cliente.getNom()}, Apellido: {cliente.getApp()}")
                    print("El cliente no tuvo movimientos durante el mes de abril.\n")
                else:
                    print("\nEl cliente tuvo movimientos durante el mes de abril.\n")