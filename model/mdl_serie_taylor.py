class Serie_Taylor:
    @staticmethod
    def calcular_factorial(numero):
        """Se calcula el factorial de un número."""
        if numero == 0 or numero == 1:
            return 1
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

    @staticmethod
    def calcular_potencia(base, exponente):
        """Se calcula la potencia de un número."""
        resultado = 1
        for _ in range(exponente):
            resultado *= base
        return resultado

    @staticmethod
    def convertir_a_grados(radianes):
        """Se convierte un valor en radianes a grados."""
        grados_por_radianes = 180 / 3.141592653589793  # Se hace una proximación de π
        return radianes * grados_por_radianes

    @staticmethod
    def calcular_funcion_exponencial(valor_x, cantidad_de_terminos=10):
        """Se calcula la función exponencial (e^x) usando la serie de Taylor."""
        resultado = 0
        for n in range(cantidad_de_terminos):
            resultado += Serie_Taylor.calcular_potencia(valor_x, n) / Serie_Taylor.calcular_factorial(n)
        return resultado
    
    @staticmethod
    def calcular_funcion_seno(valor_x, cantidad_de_terminos=10):
        """Se calcula la función seno de valor_x usando la serie de Taylor con 'cantidad_terminos' términos."""
        resultado_funcion_seno = 0
        for numero_de_terminos in range(cantidad_de_terminos):
            coeficiente = (-1)**numero_de_terminos
            numerador = Serie_Taylor.calcular_potencia(valor_x, 2*numero_de_terminos + 1)
            denominador = Serie_Taylor.calcular_factorial(2*numero_de_terminos + 1)
            resultado_funcion_seno += coeficiente * (numerador / denominador)
        return resultado_funcion_seno

    @staticmethod
    def calcular_funcion_coseno(valor_x, cantidad_de_terminos=10):
        """Se calcula la función coseno de valor_x usando la serie de Taylor con 'cantidad_terminos' términos."""
        resultado_funcion_coseno = 0
        for numero_de_terminos in range(cantidad_de_terminos):
            coeficiente = (-1)**numero_de_terminos
            numerador = Serie_Taylor.calcular_potencia(valor_x, 2*numero_de_terminos)
            denominador = Serie_Taylor.calcular_factorial(2*numero_de_terminos)
            resultado_funcion_coseno += coeficiente * (numerador / denominador)
        return resultado_funcion_coseno
    
    @staticmethod
    def calcular_funcion_arcsen(valor_x, cantidad_de_terminos=10):
        """Se calcula la función arcsen(x) usando la serie de Taylor."""
        resultado = 0
        for n in range(cantidad_de_terminos):
            coeficiente = Serie_Taylor.calcular_factorial(2*n) / (Serie_Taylor.calcular_potencia(4, n) * Serie_Taylor.calcular_factorial(n)**2 * (2*n + 1))
            resultado += coeficiente * Serie_Taylor.calcular_potencia(valor_x, 2*n + 1)
        return resultado

    @staticmethod
    def calcular_funcion_arccos(valor_x, cantidad_de_terminos=10):
        """Se calcula la función arccos(x) usando la serie de Taylor."""
        return (3.141592653589793 / 2) - Serie_Taylor.calcular_funcion_arcsen(valor_x, cantidad_de_terminos)

    @staticmethod
    def calcular_funcion_senh(valor_x, cantidad_de_terminos=10):
        """Se calcula la función de seno hiperbólico usando la serie de Taylor."""
        resultado = 0
        for n in range(cantidad_de_terminos):
            numerador = Serie_Taylor.calcular_potencia(valor_x, 2*n + 1)
            denominador = Serie_Taylor.calcular_factorial(2*n + 1)
            resultado += numerador / denominador
        return resultado

    @staticmethod
    def calcular_funcion_cosh(valor_x, cantidad_de_terminos=10):
        """Se calcula la función de coseno hiperbólico usando la serie de Taylor."""
        resultado = 0
        for n in range(cantidad_de_terminos):
            numerador = Serie_Taylor.calcular_potencia(valor_x, 2*n)
            denominador = Serie_Taylor.calcular_factorial(2*n)
            resultado += numerador / denominador
        return resultado