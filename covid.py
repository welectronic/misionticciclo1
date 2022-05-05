# Definir constantes

CRECMIENTO_DIARIO:int= 2


# Definicion de variables

diasContagio:int=0
ContagiadosActuales:int=1

def suma_recursiva(diasContagio, ContagiadosActuales):
    """
    Funcion que calcula la cantidad de contagiados
    """
    if diasContagio == 0:
        return ContagiadosActuales
    else:
        return suma_recursiva(diasContagio - 1, ContagiadosActuales * CRECMIENTO_DIARIO)

print("Calculadora de la cantidad de contagiados")
diasContagio = int(input("Introduzca la cantidad de días de contagio: "))

print("La cantidad de contagiados es: ", suma_recursiva(diasContagio, ContagiadosActuales))
