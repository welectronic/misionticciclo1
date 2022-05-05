# Definir constantes
# para este caso se definieron los límites superiores

ETAPA_UNO:int = 20
ETAPA_DOS:int = 40
ETAPA_TRES:int = 80

# Definir variables

pesoChavo:int = 0
pesoKiko:int = 0
pesoNono:int = 0

print("Bienvenido a la calculadora de peso de la vecindad")
pesoChavo = int(input("Introduzca el peso del chavo: "))

pesoKiko= 2*pesoChavo+4
pesoNono= (pesoKiko+pesoChavo)//5

print(pesoChavo," ", pesoKiko," ", pesoNono)

if pesoNono<ETAPA_UNO:
    print("uno")
elif pesoNono<ETAPA_DOS:
    print("dos")
elif pesoNono<ETAPA_TRES:
    print("tres")
else:
    print("cuatro")



