# reto para saber si es palindromo




def palindromo(palabra):
    palabra = palabra.lower() 
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return "ES PALINDROMO"
    else:
        return "NO ES PALINDROMO"

    