from claseTarjetaSube import TarjetaSube

def test():
    for i in range(3):
        saldo= int(input("Ingrese el saldo de la tarjeta: "))
        numero= int(input("Ingrese el numero de la tarjeta: "))
        tarjeta= TarjetaSube(saldo, numero)
