horas = float(input("Cuantas horas trabajas? "))
if horas > 40 :
    horas = ((horas - 40) * 1.5) + 40
tarifa = float(input("Cual es la tarifa? "))

salario = horas * tarifa

print(f"Tu salario es {salario}")