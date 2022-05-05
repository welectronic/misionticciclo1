############################################
# Dado el centro y el radio de un círculo, #
#  determinar si un punto de R2 pertenece  #
#  o no al interior del c ́ırculo.          #
############################################

import math

# Definicion de las variables

radioCirculo: float
centroX: float
centroY: float
puntoX: float
puntoY: float
distancia: float

print(" programa para determinar si un punto está dentro de un círculo o no")
radioCirculo = float(input("Introduzca el radio del círculo: "))
centroX = float(input("Introduzca la coordenada X del centro del círculo: "))
centroY = float(input("Introduzca la coordenada Y del centro del círculo: "))
puntoX = float(input("Introduzca la coordenada X del punto: "))
puntoY = float(input("Introduzca la coordenada Y del punto: "))

def distancia_puntos(puntoX, puntoY, centroX, centroY):
    """
    Funcion que calcula la distancia entre dos puntos
    """
    distancia = math.sqrt((puntoX - centroX) ** 2 + (puntoY - centroY) ** 2)
    return distancia

distancia=distancia_puntos(puntoX, puntoY, centroX, centroY)

if distancia <= radioCirculo:
    print("El punto está dentro del círculo")
else:
    print("El punto está fuera del círculo")

