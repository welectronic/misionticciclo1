# Entrada

# La entrada consta de una sucesión de caracteres separados por coma 
# que corresponden a las cuerdas asociadas a los sonidos determinados 
# por el jugador.

# Salida

# La salida consta de dos líneas: la primera es la sucesión de sonidos 
# de cuerdas sin repeticiones, en mayúscula y separadas por espacio; 
# la segunda es la cantidad de veces que se repitió cada sonido de 
# cuerda de manera consecutiva, separado también por espacio.


# Definir constantes


# Definir Variables

secuenciaEntrada = ["E","E","e","E","E","d","E","E","D","c","C","E","E","B","E","E","a","E","A","E","g","E","G","E","f","E"]
secuenciaSalida=[]
conteoSalida=[]

# Inicializar Variables
secuenciaSalida.append(secuenciaEntrada[0].upper())
conteoSalida.append(0)

#secuenciaEntrada=input("Ingrese la secuencia de sonidos: ").split(",")

for indice in range(len(secuenciaEntrada)):
    if len(secuenciaEntrada) == indice-1 or secuenciaEntrada[indice].upper() == secuenciaEntrada[indice+1].upper() :
        conteoSalida[-1]+=1
    else:
        conteoSalida[-1]+=1
        conteoSalida.append(0)
        secuenciaSalida.append(secuenciaEntrada[indice+1].upper())
print(secuenciaSalida)


################# no está terminado ######################




