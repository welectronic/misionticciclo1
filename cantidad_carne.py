# Definición de constantes

PESO_GALLINA:int = 6
PESO_GALLO:int = 7
PESO_POLLO:int = 1


# Definición de variables
cantidadGallinas:int = 0
cantidadGallos:int = 0
cantidadPollos:int = 0

print("Calculadora de cantidad de carne de animales")
cantidadGallinas = int(input("Introduzca la cantidad de gallinas: "))
cantidadGallos = int(input("Introduzca la cantidad de gallos: "))
cantidadPollos = int(input("Introduzca la cantidad de pollos: "))

def cantidadCarne(cantidadGallinas, cantidadGallos, cantidadPollos):
    """
    Funcion que calcula la cantidad de carne de animales
    """
    cantidadCarne = (cantidadGallinas * PESO_GALLINA) + (cantidadGallos * PESO_GALLO) + (cantidadPollos * PESO_POLLO)
    return cantidadCarne

print("La cantidad de carne de animales es: ", cantidadCarne(cantidadGallinas, cantidadGallos, cantidadPollos))


