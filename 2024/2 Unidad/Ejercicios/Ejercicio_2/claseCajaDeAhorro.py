"""Ejercicio 1 - Caja de Ahorro"""

class CajaDeAhorro:
    """Clasa que representa cajas de ahorros"""
    __nrocuenta:str
    __cuil:str
    __apellido:str
    __nombre:str
    __saldo:float
    def __init__(self,nc,c,a,n,s):
        """Metodo constructor de la clase CajaDeAhorro"""
        self.__nrocuenta=nc
        self.__cuil=c
        self.__apellido=a
        self.__nombre=n
        self.__saldo=s


    def mostrar_datos(self):
        """Metodo que muestra los datos del objeto"""
        print("--- SUS DATOS SON: ---".center(100))
        print('Numero de cuenta: ', self.__nrocuenta)
        print('CUIL: ', self.__cuil)
        print('Apellido: ', self.__apellido)
        print('Nombre: ', self.__nombre)
        print('Saldo: ', self.__saldo)

    def extraer(self,imp):
        """Metodo para extraer dinero"""
        if self.__saldo<imp:
            return self.__saldo-imp
        else:
            self.__saldo-=imp
            print(f"El nuevo saldo de {self.__nombre} es: ", self.__saldo)
            return 0

    def depositar(self,imp):
        """Metodo para depositar dinero"""
        if imp>0:
            self.__saldo+=imp
            print(f"El nuevo saldo de {self.__nombre} es: ", self.__saldo)
        else:
            print('ERROR. No es posible que el importe sea negativo')

    def validar_cuil(self):
        """Metodo para consultar la validez del CUIL"""
        # Esta validacion no es perfecta. Si ingresamos un CUIL en el que originalmente XY era 20/27,
        # con 23; no sera capaz de detectar el error.
        lista=[]
        acum=0
        indice=(0,1,3,4,5,6,7,8,9,10) #Esta tupla contiene los indices de los digitos con los cuales se hara el producto
        constante=(5,4,3,2,7,6,5,4,3,2) #Esta tupla contiene las constantes que multiplicaran a los digitos
        acum=0
        for i in range(len(self.__cuil)-3): #El -3 se debe a los dos guiones(-) y al digito z; los cuales no se tienen en cuenta para realziar la operacion
            lista.append(int(self.__cuil[indice[i]])*constante[i])

        for i in lista:
            acum+=i
        p1=acum//11
        p2=acum-(p1*11)
        if p2==0:
            if self.__cuil[12]!='0':
                print('CUIL erroneo. El digito de verificacion deberia ser 0')
            else:
                print('El CUIL es valido')
        #Este bloque detecta CUILs cuyos digitos XY deberian ser 23, pues son repetidos
        elif p2==1:
            if self.__cuil[0:2]=='20':
                if self.__cuil[12]!='9':
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23, y Z el 9')
                else:
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23')
            elif self.__cuil[0:2]=='27':
                if self.__cuil[12]!='4':
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23, y Z el 4')
                else:
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23')
        else:
            band=False
            valido=('4','9')
            if self.__cuil[0:2]=='23':
                if (self.__cuil[12] in valido)is False:
                    print('CUIL invalido. Su digito de verificacion deberia ser 4 o 9')
                else:
                    band=True
            else:
                z=11-p2
                if int(self.__cuil[12])!=z:
                    print('CUIL invalido. Z deberia tomar el valor ',z)
                else:
                    band=True
            if band is True:
                print('CUIL valido')

    def obtenerCUIL(self):
        """Metodo para obtener el CUIL"""
        return self.__cuil

    def obtenerNombre(self):
        """Metodo para obtener el Nombre"""
        return self.__nombre

    def obtenerApellido(self):
        """Metodo para obtener el Apellido"""
        return self.__apellido

    def obtenerSaldo(self):
        """Metodo para obtener el Saldo"""
        return self.__saldo
