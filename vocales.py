# Definicion de variables

listaVocales=[ord("a"),ord("e"),ord("i"),ord("o"),ord("u")]


print("Verificador de vocales")
vocalParaVerificar=int(input("Introduzca una vocal: "))

if vocalParaVerificar in listaVocales:
    print("El número ingresado corresponde una vocal minúscula")
else:
    print("El número ingresado no corresponde a una vocal minúscula")