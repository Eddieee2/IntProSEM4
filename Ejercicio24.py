tiempo_lunes = float(input("Ingrese el tiempo del lunes (en minutos): "))
tiempo_miercoles= float(input("Ingrese el tiempo del miercoles (en minutos): "))
tiempo_viernes = float(input("Ingrese el tiempo del viernes (en minutos): "))

tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3

print(f"El tiempo promedio es: {tiempo_promedio:.2f} minutos")