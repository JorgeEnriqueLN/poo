from ControladorBeca import *
from ControladorBeneficiario import *


if __name__ == '__main__':
    
    becas = ControladorBeca(6)
    beneficiarios = ControladorBeneficiario(14)
    becas.cargar()
    beneficiarios.cargar()
    
    nombreBeca = input("Ingrese tipo de beca: ")
    idBeca = becas.buscarNombre(nombreBeca)
    beneficiarios.importePagarPorTipoBeca(nombreBeca,idBeca,becas.getBecas())