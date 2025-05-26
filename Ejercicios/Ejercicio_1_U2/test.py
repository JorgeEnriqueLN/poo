from claseTarjetaSube import TarjetaSube

def test():
    for i in range(1):
        saldo= int(input("Ingrese el saldo de la tarjeta: "))
        numero= int(input("Ingrese el numero de la tarjeta: "))
        tarjeta= TarjetaSube(saldo, numero)
    print(tarjeta)

    print ("El saldo de la tarjeta es: ", tarjeta.getSaldo())
            
    importe= int(input("Ingrese el importe a cargar: "))
    tarjeta.Cargar_saldo(importe)

    print("el nuevo saldo es ", tarjeta.getSaldo())
        
    pago= int(input("Ingrese monto a pagar: "))

    pag = tarjeta.Pagar_pasaje(pago)
            
    if (pag >= 0):
        print("Su saldo actual es: ", tarjeta.getSaldo())
    else:
        print("Su saldo no es suficiente, le faltan: ", -1*pag)

        


