from claseLista import lista

def menu():
    print("Menu\n1- Mostrar por posicion\n2- Mostrar cantidad por anio\n3- Mostrar cantidad por capacidad\n4- Mostrar todo\n5- Salir")

if __name__=='__main__':
    lista1=lista()
    lista1.carga()
    menu()
    o=int(input("Ingrese una opcion\n"))
    while(o!=5):
        if(o==1):
            try:
                lista1.pos()
            except IndexError:
                print("Indice fuera de rango\n")
        elif(o==2):
            lista1.cantAnio()
        elif(o==3):
            lista1.cantCap()
        elif(o==4):
            lista1.mostrar()
        else:
            print(f"La opcion ingresada es incorrecta\n")
        menu()
        o=int(input("Ingrese una opcion\n"))