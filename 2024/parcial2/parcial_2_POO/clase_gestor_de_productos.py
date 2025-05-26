from clase_productos_congelados import producto_congelado
from clase_productos_refrigerados import producto_refrigerado
import csv
class gestor_de_productos:
    __lista:list
    def __init__(self):
        self.__lista=[]
    def cargar_productos(self):
        archi=open("productos.csv")
        reader=csv.reader(archi,delimiter=";")
        next(reader)
        for f in reader:
            if f[0]=="C":
                xproducto=producto_congelado(f[1],f[2],f[3],float(f[4]),f[5],f[6],float(f[7]),int(f[8]),int(f[9]),int(f[10]),int(f[11]),f[12])
            else:
                xproducto=producto_refrigerado(f[1],f[2],f[3],float(f[4]),f[5],f[6],float(f[7]),f[8])
            self.__lista.append(xproducto)
    def agregar_producto(self):
        try:
            aux=input("ingrese el tipo de producto(refrigerado'R' o congelado'C'):\n").upper()
            assert aux=="R" or aux=="C" ,"la opcion ingresada debe ser una de las sugeridas\n"
            if aux=="R":
                nom=input("ingrese el nombre del producto:\n")
                fechaE=input("ingrese fecha de envasado del producto:\n")
                fechaV=input("ingrese fecha de vencimiento del producto:\n")
                temp=float(input("ingrese la temperatura de mantenimiento recomendada:\n"))
                pais=input("ingrese el pais de origen del producto:\n")
                num_lote=input("ingrese el numero de lote del producto:\n")
                costo_base=float(input("ingrese el costo base del producto:\n"))
                codigo=input("ingrese el codigo del organismo de supervision alimentaria:\n")
                xproducto=producto_refrigerado(nom,fechaE,fechaV,temp,pais,num_lote,costo_base,codigo)
            else:
                nom=input("ingrese el nombre del producto:\n")
                fechaE=input("ingrese fecha de envasado del producto:\n")
                fechaV=input("ingrese fecha de vencimiento del producto:\n")
                temp=float(input("ingrese la temperatura de mantenimiento recomendada:\n"))
                pais=input("ingrese el pais de origen del producto:\n")
                num_lote=input("ingrese el numero de lote del producto:\n")
                costo_base=float(input("ingrese el costo base del producto:\n"))
                nitro=int(input("ingrese el porcentaje de nitrogeno:\n"))
                oxi=int(input("ingrese el porcentaje de oxigeno:\n"))
                dioxi=int(input("ingrese el porcentaje de dioxido de carbono:\n"))
                vapor=int(input("ingrese el porcentaje de vapor de agua:\n"))
                metodo=input("ingrese el metodo de congelacion:\n")
                xproducto=producto_congelado(nom,fechaE,fechaV,temp,pais,num_lote,costo_base,nitro,oxi,dioxi,vapor,metodo)
            self.__lista.append(xproducto)
        except TypeError:
            print("error de tipo")
        except AssertionError as e:
            print(f"error: {e}")
        except ValueError:
            print("se espera un valor valido")
    def mostrar_tipo_producto(self):
        try:
            pos=int(input("ingrese la posicion del producto:\n"))
            if isinstance(self.__lista[pos],producto_congelado):
                print("el producto es de tipo congelado\n")
            elif isinstance(self.__lista[pos],producto_refrigerado):
                print("el producto es de tipo refrigerado\n")
            else:
                print("error en el tipo del producto")
        except TypeError:
                print("error de tipo")
        except IndexError:
            print("error el indice ingresado excede el numero de componentes de la lista")
    def mostrar_cantidad_productos(self):
        contC=0
        contR=0
        for xprod in self.__lista:
            if isinstance(xprod,producto_congelado):
                contC+=1
            elif isinstance(xprod,producto_refrigerado):
                contR+=1
        print(f"productos congelados: {contC}\nproductos refrigerados: {contR}\n")
    def mostrar_productos(self):
        for prod in self.__lista:
            prod.mostrar_prod()