from controller.ctrl_serie_taylor import ControladorSerieTaylor

if __name__ == "__main__":
    controlador = ControladorSerieTaylor()
    
    valor_x = float(input("Ingrese el valor de x en radianes: "))
    cantidad_de_terminos = int(input("Ingrese el número de términos para la serie de Taylor: "))

    controlador.calcular_funciones(valor_x, cantidad_de_terminos)