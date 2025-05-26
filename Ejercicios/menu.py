#import Manejador import clase

def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] 
          [2] 
          [3] 
          [4] 
          [5] 
          [6] 
          [0] SALIR
          -> """))
    return op

if __name__=='__main__':
   
 

    opcion=menu()
    while opcion!=0:
        if opcion==1:
           

            print('Operacion 1 Exitosa')

        elif opcion==2:
          

            print('Operacion 2 Exitosa')

        elif opcion==3:
            
            print('Operacion 3 Exitosa')
        elif opcion==4:
            print('Operacion 4 Exitosa')
        elif opcion==5:
            print('Operacion 5 Exitosa')
        elif opcion==6:
            print('Operacion 6 Exitosa')
        else:
            print("Opcion Invalida")
        opcion=menu()
