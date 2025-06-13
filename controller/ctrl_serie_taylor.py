from model.mdl_serie_taylor import Serie_Taylor
from view.vta_serie_taylor import Mostrar_resultado

class ControladorSerieTaylor:
    def __init__(self):
        self.modelo = Serie_Taylor()
        self.vista = Mostrar_resultado()

    def calcular_funcion_seno(self, valor_x, cantidad_de_terminos=10):
        resultado_funcion_seno = self.modelo.calcular_funcion_seno(valor_x, cantidad_de_terminos)
        grados = self.modelo.convertir_a_grados(valor_x)  # 🔹 Conversión de radianes a grados
        self.vista.imprimir_resultado(resultado_funcion_seno, f"seno ({grados:.2f}°)")

    def calcular_funcion_coseno(self, valor_x, cantidad_de_terminos=10):
        resultado_coseno = self.modelo.calcular_funcion_coseno(valor_x, cantidad_de_terminos)
        grados = self.modelo.convertir_a_grados(valor_x)  # 🔹 Conversión de radianes a grados
        self.vista.imprimir_resultado(resultado_coseno, f"coseno ({grados:.2f}°)")
