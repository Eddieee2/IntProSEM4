total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

propina = (porcentaje_propina / 100) * total_cuenta


print(f"La propina a dejar es: {propina:.2f}")
