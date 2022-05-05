# Import math library
import math

# Definición de constantes

PRECIO_PANES:int = 300
PRECIO_LECHE:int = 3300
PRECIO_HUEVOS:int = 500

# Definición de variables

cantidadPanes:int = 0
cantidadLeche:int = 0
cantidadHuevos:int = 0
valorBillete:int = 0
valorDevuelta:int = 0

def precioTotal(cantidadPanes:int, cantidadLeche:int, cantidadHuevos:int):
    """
    Funcion que calcula el precio total de la compra
    """
    precioTotal = (cantidadPanes * PRECIO_PANES) + (cantidadLeche * PRECIO_LECHE) + (cantidadHuevos * PRECIO_HUEVOS)
    return precioTotal

def devuelta(valorBillete:int, precioTotal:int):
    """
    Funcion que calcula la cantidad de dinero devuelta
    """
    devuelta = valorBillete - precioTotal
    return devuelta

print("Calculadora de cantidad de dinero devuelta o adeudado")
cantidadPanes = int(input("Introduzca la cantidad de panes: "))
cantidadLeche = int(input("Introduzca la cantidad de leche: "))
cantidadHuevos = int(input("Introduzca la cantidad de huevos: "))
valorBillete = int(input("Introduzca el valor del billete: "))

valorDevuelta = devuelta(valorBillete, precioTotal(cantidadPanes, cantidadLeche, cantidadHuevos))

if valorDevuelta < 0:
    print("Adeuda: ", math.abs(valorDevuelta))
else:
    print("Devuelve: ", valorDevuelta)

