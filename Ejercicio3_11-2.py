try:
    horas = float(input("Cuantas horas trabajas? "))
    tarifa = float(input("Cual es la tarifa? "))
except ValueError:
    print('Por favor, introduzca un numero')
    exit()

if horas > 40 :
    hora_extra = 40 + ((horas - 40) * 1.5)
else:
    hora_extra = horas

salario = hora_extra * tarifa

print(f"Tu salario es {salario}")