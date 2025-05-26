from clase_gestor_de_productos import gestor_de_productos
def menu():
    try:
        aux=int(input("1_cargar productos desde archivo\n2_agregar producto al gestor de producto\n3_mostrar por pantalla que tipo de producto se encuentra almacena en una posicion\n4_mostrar cantidad de productos de cada tipo\n5_mostrar todos los productos\n6_fin\n"))
        assert aux>=1 and aux<=6,"se espera una opcion valida"
    except TypeError:
        print("error de tipo ingrese un numero valido")
    except AssertionError as e:
        print(f"error: {e}")
    return aux
if __name__=="__main__":
    xgestor=gestor_de_productos()
    aux1=1
    while aux1!=6:
        aux1=menu()
        if aux1==1:
            xgestor.cargar_productos()
        elif aux1==2:
            xgestor.agregar_producto()
        elif aux1==3:
            xgestor.mostrar_tipo_producto()
        elif aux1==4:
            xgestor.mostrar_cantidad_productos()
        elif aux1==5:
            xgestor.mostrar_productos()