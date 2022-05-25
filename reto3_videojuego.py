## teclas disponibles L,R,X,A,B,Y

listaEntrada = []
salida1=""
salida2=""

listaEntrada=input("Ingrese las teclas presionadas: ").upper().split(",")

indice=0
contador=1

while True:

    if listaEntrada[indice]==listaEntrada[indice+1]:
        contador+=1
    else:
        salida1+=listaEntrada[indice]+" "
        salida2+=str(contador)+" "
        contador=1
    indice+=1

    if indice==len(listaEntrada)-1:
        salida1+=listaEntrada[indice]
        salida2+=str(contador)
        break
print(salida1)
print(salida2)