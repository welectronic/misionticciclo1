# Definicion de constantes

# este arreglo se define para una futura validacióin de entradas,
# ya que no se puede ingresar un valor que no sea una de las opciones
# sin embargo no es solicitado en el ejercicio
WEAPONS = { ".", "-", "+", "*", "T", "Y", "|", "W", "X", "M" }


# definicion de funciones

teamVampiricGhosts = []
teamFrenzyShooters = []
timerClock = []
teamVampiricGhostsShoot= 0
teamFrenzyShootersShoot= 0

def checkWinner():
    if teamVampiricGhostsShoot > teamFrenzyShootersShoot:
        return "V"
    elif teamVampiricGhostsShoot < teamFrenzyShootersShoot:
        return "F"
    else:
        return "≈"

teamVampiricGhosts = list(input("Ingrese las armas del grupo Vampiric Ghosts: "))
teamFrenzyShooters = list(input("Ingrese las armas del grupo Frenzy Shooters: "))
timerClock = list(input("Ingrese el tiempo de juego: "))



for i in timerClock:
    if i  in teamVampiricGhosts:
        teamVampiricGhostsShoot+=1
    if i in teamFrenzyShooters:
        teamFrenzyShootersShoot+=1
    print(checkWinner(), end="")