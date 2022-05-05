# Definición de constantes

INTERES:float = 0.03
PLAZO_MESES:int = 3

montoPrestamo:float = 0

def interes_compuesto(montoPrestamo, INTERES, PLAZO_MESES):
    """
    Funcion que calcula el interes compuesto
    """
    interesCompuesto = montoPrestamo * (INTERES / 12) * PLAZO_MESES
    return interesCompuesto

print("Calculadora de interes compuesto")
montoPrestamo = float(input("Introduzca el monto del prestamo: "))

print("El interes compuesto es: ", interes_compuesto(montoPrestamo, INTERES, PLAZO_MESES))
