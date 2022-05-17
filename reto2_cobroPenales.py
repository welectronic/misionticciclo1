# Jugadore representados por los caracteres separados por coma ( . , + , T , | , X , - , * , Y , W , ! , @ , # , $)
# minimo 1 maximo 6 jugadores
# no hay jugadores repetidos


# ENTRADA 1 JUGADORES
# ENTRADA 2 PORTEROS
# ENTRADA 3 NOMBRE DEL EQUPO


 # Se definen las constantes

from numpy import empty


GOL = "\u00D8"
EMPATE = "\u265E"
ATAJADA = "\u00A5"

# SE DEFINEN LAS VARIABLES

jugadores=""
porteros=""
nombreEquipo=""
resultado=""
goles=0
maxGoles=0

#SE DEFINEN LAS FUNCIONES


def palindromo(palabra):
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return "ES PALINDROMO"
    else:
        return "NO ES PALINDROMO"

def limpiarCadena(cadena):
    cadena = cadena.replace(" ","")
    cadena = cadena.replace("á","a")
    cadena = cadena.replace("é","e")
    cadena = cadena.replace("í","i")
    cadena = cadena.replace("ó","o")
    cadena = cadena.replace("ú","u")
    cadena=cadena.lower()
    return cadena

# DESARROLLO DEL CÓDIGO

jugadores=input("Ingrese los jugadores: ")
porteros=input("Ingrese los porteros: ")
nombreEquipo=input("Ingrese el nombre del equipo: ")

for jugador in jugadores:
    goles=0
    for portero in porteros:
        if jugador == portero:
            resultado+=EMPATE
        elif jugador < portero:
            resultado+=ATAJADA
        else:
            resultado+=GOL
            goles+=1
    if goles > maxGoles:
        maxGoles = goles

print(resultado)
print(palindromo(limpiarCadena(nombreEquipo)))
print(maxGoles)