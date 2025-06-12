from model.mdl_serie_taylor import SerieTaylor
from view.vta_serie_taylor import MostrarResultado

class ControladorSerieTaylor:
    def __init__(self):
        self.modelo = SerieTaylor()
        self.vista = MostrarResultado()

    def calcular_seno(self, valor_x, cantidad_terminos=10):
        resultado_seno = self.modelo.calcular_seno(valor_x, cantidad_terminos)
        self.vista.imprimir_resultado(resultado_seno, "seno")

    def calcular_coseno(self, valor_x, cantidad_terminos=10):
        resultado_coseno = self.modelo.calcular_coseno(valor_x, cantidad_terminos)
        self.vista.imprimir_resultado(resultado_coseno, "coseno")
