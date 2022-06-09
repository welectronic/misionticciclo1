# desarrollar una librería en python llamada “figura.py” que permita realizar las siguientes funciones:
# tipodefigura
# mefaltatipodefigura 
# notengo
# puedoCambiar

def tipodefigura(categorias):
    """
    Funcion que determina la lista de categorias sin repeticion
    """

    tipodefigura=[]

    for categoria in categorias:
        if categoria not in tipodefigura:
            tipodefigura.append(categoria)

    return tipodefigura

def mefaltatipodefigura(posiciones, categorias, figura):
    """
    Funcion que determina el tipo de figura de una lista de posiciones
    """

    mefaltatipodefigura=[]

    for posicion in posiciones:
        if  categorias[posicion] == figura:
            tipodefigura.append(posicion)

    return mefaltatipodefigura

def notengo(disponibles, fan):
    """
    Funcion que determina si una lista de figuras disponibles contiene una una lista de figuras de un fan
    """

    notengo=[]

    for figura in disponibles:
        if figura not in fan:
            notengo.append(figura)
    return notengo

def puedoCambiar(disponibles, fan):
    """
    Funcion que determina si una lista de figuras disponibles contiene una una lista de figuras de un fan
    """

    puedoCambiar=[]

    for figura in fan:
        if figura not in disponibles:
            puedoCambiar.append(figura)
    
    return len(puedoCambiar)
