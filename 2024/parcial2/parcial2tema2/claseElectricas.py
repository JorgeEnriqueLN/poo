from claseEquipo import Equipo
class Electrica(Equipo):
   __fuente: str
   
   def __init__(self, tipo, marca, modelo, anioDeFabricacion, tipoDeCombustible, potencia, capacidadDeCarga, tarifaAlquilerDiario, cantidadDiasAlquiler, fuente):
        super().__init__(tipo, marca, modelo, anioDeFabricacion, tipoDeCombustible, potencia, capacidadDeCarga, tarifaAlquilerDiario, cantidadDiasAlquiler)
        self.__fuente = fuente
        
   def getfuente(self):
      return self.__fuente
   
  
   
   def calcular_precio (self):
      if self.__fuente == ("bateria"):
         tarifa = (int(self.gettarifaAlquilerDiario())*int(self.getcantidadDiasAlquiler()))*1.10
      elif self.__fuente==("cable"):
         tarifa = (int(self.gettarifaAlquilerDiario())*int(self.getcantidadDiasAlquiler()))
      return tarifa