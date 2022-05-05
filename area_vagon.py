# Import math library
import math

# Se definen las constantes
PI: float = math.pi

# Se definen las variables

lado1: float
lado2: float
radio: float

def area_rectangulo(lado1, lado2):
    """
    Funcion que calcula el area de un rectangulo
    """
    area_rectangulo = lado1 * lado2
    return area_rectangulo

def area_circulo(radio):
    """
    Funcion que calcula el area de un circulo
    """
    area_circulo = PI * (radio ** 2)
    return area_circulo

print("Calculadora de Area de un vagón bidimensional")
lado1 = float(input("Introduzca el valor del primer lado del rectangulo: "))
lado2 = float(input("Introduzca el valor del segundo lado del rectangulo: "))
radio = float(input("Introduzca el valor del radio del circulo: "))

print("El area del vagón es: ", area_rectangulo(lado1, lado2)+area_circulo(radio))

