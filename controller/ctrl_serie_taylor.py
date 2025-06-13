from model.mdl_serie_taylor import Serie_Taylor
from view.vta_serie_taylor import Mostrar_resultado

class ControladorSerieTaylor:
    def __init__(self):
        self.modelo = Serie_Taylor()
        self.vista = Mostrar_resultado()

    def calcular_funciones(self, valor_x, cantidad_de_terminos=10):
        funciones = {
            "Exponencial (e^x)": self.modelo.calcular_funcion_exponencial(valor_x, cantidad_de_terminos),
            "Seno (sen x)": self.modelo.calcular_funcion_seno(valor_x, cantidad_de_terminos),
            "Coseno (cos x)": self.modelo.calcular_funcion_coseno(valor_x, cantidad_de_terminos),
            "Arcsen (arcsen x)": self.modelo.calcular_funcion_arcsen(valor_x, cantidad_de_terminos),
            "Arccos (arccos x)": self.modelo.calcular_funcion_arccos(valor_x, cantidad_de_terminos),
            "Seno hiperbólico (senh x)": self.modelo.calcular_funcion_senh(valor_x, cantidad_de_terminos),
            "Coseno hiperbólico (cosh x)": self.modelo.calcular_funcion_cosh(valor_x, cantidad_de_terminos),
        }

        for nombre, resultado in funciones.items():
            self.vista.imprimir_resultado(resultado, nombre)