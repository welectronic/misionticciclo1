# recibe un diccionario que contiene las criptomonedas
# y su respectivo valor en dólares, adicionalmente recibe
# el listado de criptomonedas manejadas por el magnate 
# separado por espacios. 
# La salida se representará en dos líneas, donde 
# la primera mostrará una cadena de texto con las llaves 
# de las criptomonedas encontradas en el diccionario 
# separadas por espacio.
# luego en una línea aparte la suma total en dólares 
# que posee el magnate

#include json library
import json

# se definen las variables

bdCriptos= json.loads(input("ingrese el listado de criptos en formato JSON: "))

wallet = input("ingrese el listado de criptos separados por espacio: ").split(" ")

saldo=0
listaCriptosValidas=""

for criptos in wallet:
    if criptos in bdCriptos:
        listaCriptosValidas+=criptos+" "
        saldo+=bdCriptos[criptos]

print(listaCriptosValidas.rstrip())
print(saldo)