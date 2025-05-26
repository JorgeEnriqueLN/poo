from ClassCliente import Cliente
from csv import reader

class GestorClientes:
    __listaClientes = []
    
    def __init__(self):
        self.__listaClientes = []
        
    #retornar una copia de la lista
    def get_listaClientesCopia(self): return self.__listaClientes.copy()
    #retornar la lista real
    def get_listaClientes(self): return self.__listaClientes
    
    def agregarCliente(self,nuevoCliente):
        self.__listaClientes.append(nuevoCliente)
    
    def leerClientes_desde_csv(self,nombre_archivo):
        with open(nombre_archivo, newline='') as archivo_csv:
            lector_csv = reader(archivo_csv, delimiter=';')
            for fila in lector_csv:
                nombre,apellido,dni,numTarjeta,saldoAnterior = fila
                nuevoCliente = Cliente(nombre,apellido,dni,int(numTarjeta),float(saldoAnterior))
                self.agregarCliente(nuevoCliente)
    
    def actualizarCliente(self,DNIingresado,movimientos):
        numTarjetaEncontrado = None
        for cliente in self.__listaClientes:
            if DNIingresado == cliente.get_dni():
                numTarjetaEncontrado = cliente.get_numTarjeta()
                break
            
        if numTarjetaEncontrado is None: # si no se encontro el cliente va a dar error
            return 'NoEncontrado'
        
        # Imprimo primero el encabezado del listado
        print(f"Cliente:{cliente.get_nombre()} {cliente.get_apellido()}\t Numero de tarjeta:{cliente.get_numTarjeta()}")
        print(f"Saldo anterior: {cliente.get_saldoAnterior()}")
        print("Movimientos")
        print("Fecha    Descripcion            Importe   Tipo de movimiento")
        
        for movimiento in movimientos:
            if movimiento.get_numTarjeta() == numTarjetaEncontrado:
                if movimiento.get_tipo() == 'P': #verifica si es un pago
                    print(f"{movimiento.get_fecha()}    {movimiento.get_descripcion()}          ${movimiento.get_importe()}    {movimiento.get_tipo()}")
                    cliente.registrarPago(movimiento.get_importe())
                else: #sino es un credito
                    print(f"{movimiento.get_fecha()}    {movimiento.get_descripcion()}          ${movimiento.get_importe()}    {movimiento.get_tipo()}")
                    cliente.registrarCredito(movimiento.get_importe())
        print(f"Saldo actualizado: ${cliente.get_saldoAnterior()}")