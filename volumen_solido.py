# Import math Library
import math

# Se definen las variables
radio1: float
radio2: float
altura: float
volumen_esfera: float
volumen_cono: float

# Se definen las constantes
PI: float = math.pi

def volumen_esfera(radio):
    """
    Funcion que calcula el volumen de una esfera
    """
    volumen_esfera = (4/3) * PI * (radio ** 3)
    return volumen_esfera

def volumen_cono(radio, altura):
    """
    Funcion que calcula el volumen de un cono
    """
    volumen_cono = (1/3) * PI * (radio ** 2) * altura
    return volumen_cono

print("Calculadora de Volumen de un sólido compuesto")
altura = float(input("Introduzca el valor de la altura del cono: "))
radio1 = float(input("Introduzca el valor del radio del cono: "))
radio2 = float(input("Introduzca el valor del radio de la esfera: "))

print("El volumen del sólido es: ", volumen_cono(radio1, altura)+volumen_esfera(radio2))