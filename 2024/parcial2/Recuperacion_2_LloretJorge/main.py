from gestorP import *
def main():
    gestor = GestorPlanes()
    archivo = 'planes.csv'
    gestor.cargar_planes(archivo)
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar tipo de plan en una posición dada")
        print("2. Mostrar cantidad de planes por cobertura geográfica")
        print("3. Mostrar nombres de compañías con más canales internacionales que una cantidad dada")
        print("4. Mostrar todos los planes")
        

        opcion = input("Seleccione una opción: ")

        
        if opcion == "1":
            try:
                posicion = int(input("Ingrese la posición del plan: "))
                print(gestor.mostrar_tipo_plan(posicion))
            except IndexError as e:
                print(e)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        elif opcion == "2":
            cobertura = input("Ingrese la cobertura geográfica: ")
            cantidad = gestor.contar_planes_por_cobertura(cobertura)
            print(f"Cantidad de planes con cobertura {cobertura}: {cantidad}")
        elif opcion == "3":
            try:
                min_canales = int(input("Ingrese la cantidad mínima de canales internacionales: "))
                nombres = gestor.buscar_planes_por_canales_internacionales(min_canales)
                if nombres:
                    print("Compañías que ofrecen esa cantidad de canales internacionales o más:")
                    for nombre in nombres:
                        print(nombre)
                else:
                    print("Ninguna compañía ofrece esa cantidad de canales internacionales o más.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        elif opcion == "4":
            for datos in gestor.mostrar_todos_los_planes():
                print(datos)
        

if __name__ == "__main__":
    main()
