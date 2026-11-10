import re
x = input('Introduce el nombre del archivo:')
total = 0
contador = 0
try:
    manejador = open(x)
    for linea in manejador:
        numeros = re.findall('^New Revision: ([0-9]+)', linea)
        if len(numeros) > 0 :
            num = numeros [0]
            total = total + float(num)
            contador = contador + 1
except FileNotFoundError:
    print(f'El archivo {x} no puede ser abierto')
if contador > 0:
    media = total / contador
    print (f'El promedio es {media}')