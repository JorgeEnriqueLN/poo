from claseEquipo import Equipo
class Pesada(Equipo):
   __maquina: str
   __peso : int
   
   
   def __init__(self, tipo, marca, modelo, anioDeFabricacion, tipoDeCombustible, potencia, capacidadDeCarga, tarifaAlquilerDiario, cantidadDiasAlquiler, maquina, peso):
        super().__init__(tipo, marca, modelo, anioDeFabricacion, tipoDeCombustible, potencia, capacidadDeCarga, tarifaAlquilerDiario, cantidadDiasAlquiler)
        self.__maquina = maquina
        self.__peso = peso
   
   def getmaquina(self):
      return self.__maquina
   def getpeso(self):
      return self.__peso
   
 
   
   def calcular_precio (self):
      if self.__peso > 10:
         tarifa = (int(self.gettarifaAlquilerDiario())*int(self.getcantidadDiasAlquiler()))
      elif self.__peso <= 10:
         tarifa = (int(self.gettarifaAlquilerDiario())*int(self.getcantidadDiasAlquiler()))*1.20
      return tarifa