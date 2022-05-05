# Import math library
import math

# Se definen las constantes
PI: float = math.pi

# Se definen las variables

lado1: float
lado2: float
lado3: float
lado4: float
radio1: float
radio2: float

def area_rectangulo(ladoa, ladob):
    """
    Funcion que calcula el area de un rectangulo
    """
    area_rectangulo = ladoa * ladob
    return area_rectangulo

def area_circulo(radio):
    """
    Funcion que calcula el area de un circulo
    """
    area_circulo = PI * (radio ** 2)
    return area_circulo

print("Calculadora de Area de un vagón bidimensional")
lado1 = float(input("Introduzca el valor del primer lado del rectangulo 1: "))
lado2 = float(input("Introduzca el valor del segundo lado del rectangulo 1: "))
lado3 = float(input("Introduzca el valor del primer lado del rectangulo 2: "))
lado4 = float(input("Introduzca el valor del segundo lado del rectangulo 2: "))
radio1 = float(input("Introduzca el valor del radio del circulo: "))
radio2 = float(input("Introduzca el valor del radio del circulo: "))

print("El area del vagón es: ", area_rectangulo(lado1, lado2)+area_rectangulo(lado3, lado4)+area_circulo(radio1)+area_circulo(radio2))

