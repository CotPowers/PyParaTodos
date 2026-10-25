palabra = "Letras"
indice = len(palabra) - 1

while indice >=0:
    letra = palabra[indice]
    print(letra)
    indice = indice - 1

palabra = "Letras"

for caracter in reversed(palabra):
    print(caracter)