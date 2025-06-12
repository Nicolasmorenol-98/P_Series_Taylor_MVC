import math

class SerieTaylor:
    @staticmethod
    def calcular_seno(valor_x, cantidad_terminos=10):
        """Calcula el seno de valor_x usando la serie de Taylor con 'cantidad_terminos' términos."""
        resultado_seno = 0
        for numero_termino in range(cantidad_terminos):
            coeficiente = (-1)**numero_termino
            numerador = valor_x**(2*numero_termino + 1)
            denominador = math.factorial(2*numero_termino + 1)
            resultado_seno += coeficiente * (numerador / denominador)
        return resultado_seno

    @staticmethod
    def calcular_coseno(valor_x, cantidad_terminos=10):
        """Calcula el coseno de valor_x usando la serie de Taylor con 'cantidad_terminos' términos."""
        resultado_coseno = 0
        for numero_termino in range(cantidad_terminos):
            coeficiente = (-1)**numero_termino
            numerador = valor_x**(2*numero_termino)
            denominador = math.factorial(2*numero_termino)
            resultado_coseno += coeficiente * (numerador / denominador)
        return resultado_coseno

