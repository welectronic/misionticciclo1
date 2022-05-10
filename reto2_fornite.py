# Definicion de constantes

# este arreglo se puede definir para una futura validacióin de entradas,
# ya que no se puede ingresar un valor que no sea una de las opciones
# sin embargo no es solicitado en el ejercicio
# WEAPONS = { ".", "-", "+", "*", "T", "Y", "|", "W", "X", "M" }

# definicion de funciones

teamVampiricGhosts = []
teamFrenzyShooters = []
timerClock = []
teamVampiricGhostsShoot= 0
teamFrenzyShootersShoot= 0

def checkWinner():
    """
    Función que verifica el estado de la partida por cada ciclo de reloj
    """
    if teamVampiricGhostsShoot > teamFrenzyShootersShoot:
        return "V"
    elif teamVampiricGhostsShoot < teamFrenzyShootersShoot:
        return "F"
    else:
        return "≈"

teamVampiricGhosts = list(input("Ingrese las armas del grupo Vampiric Ghosts: "))
teamFrenzyShooters = list(input("Ingrese las armas del grupo Frenzy Shooters: "))
timerClock = list(input("Ingrese el tiempo de juego: "))

# El reloj corre y verifica el daño de cada facción de acuerdo a las armas asignadas
for i in timerClock:
    if i  in teamVampiricGhosts:
        teamVampiricGhostsShoot+=1
    if i in teamFrenzyShooters:
        teamFrenzyShootersShoot+=1
    print(checkWinner(), end="")