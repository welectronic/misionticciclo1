# Desarrollar un programa que imprima el cuadrado del n ́umero que el
# usuario ingresa mientras que el n ́umero ingresado no sea negativo.

while 1:
    numero = int(input("Ingrese un número: "))
    print("El cuadrado del número es: ", numero ** 2)
    if numero < 0:
        break   # rompe el ciclo
