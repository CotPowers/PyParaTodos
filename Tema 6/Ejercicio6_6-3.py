def cuenta(cadena, letra_buscada):
    contador = 0
    for letra in cadena:
        if letra == letra_buscada:
            contador = contador + 1
    return contador


# Ejemplos de uso:
print(cuenta("banana", "a"))  # Devuelve 3
print(cuenta("murcielago", "u"))  # Devuelve 1
print(cuenta("esternocleidomastoideo", "o"))  # Devuelve 4