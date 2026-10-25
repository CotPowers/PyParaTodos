total = 0.0
contador = 0

while True:
    num = input("Introduce numeros: ")
    if num == 'fin':
        break
    try:
        numero = float(num)
        total = total + numero
        contador =  contador + 1
    except ValueError:
        print("Error: Introducir solo numeros o fin")
        continue

if contador > 0:
    media = total / contador
    print ('Resultados')
    print (f'Media = {media}')
    print (f'Total = {total}')
    print (f'Cantidad de numeros = {contador}')
else:
    print('No se introdujo ningun numero')
