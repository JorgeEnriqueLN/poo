from gestor import gestorEquipo
def main():
   gestorE = gestorEquipo()
   opcion = 1
   while opcion != 0:
      try:
        opcion = int(input("""Menu de opciones
                           Opcion 1: mostrar el tipo de una herramienta
                           Opcion 2: buscar año de fabricacion
                           Opcion 3: buscar capacidad de carga
                           Opcion 4: mostrar datos
                           Opcion 5: mostrar la lista
                           Opcion 0: Detener la ejecucion: """))
      except ValueError:
         print("No se ingreso un numero")
         #opcion = 5
      if opcion in [0,1,2,3,4,5]:
         if opcion == 1:
            try:
               i = int(input("ingrese el indice de la lista: "))
            except ValueError:
               print("no se ingreso un numero entero")
            else:
               gestorE.mostrar_tipo(i)
         elif opcion == 2:
            try:
               i = int(input("ingrese el año que quiere buscar: "))
            except ValueError:
               print("no se ingreso un numero entero")
            else:
               gestorE.cantidad_por_anio(i)
         elif opcion == 3:
            try:
               i = int(input("ingrese capacidad de carga maxima: "))
            except ValueError:
               print("no se ingreso un numero entero")
            else:
               gestorE.buscar_capacidad(i)
         elif opcion == 4:
            gestorE.mostrar_datos()       
         elif opcion == 5:
            gestorE.mostrar_equipo()
      else:
         print("La opcion ingresada no es valida")
   
if __name__ == "__main__":
   main()