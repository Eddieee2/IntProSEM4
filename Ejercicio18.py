tareas = float(input("Ingrese la calificacion de las tareas (0-100):"))
examen_parcial = float(input("Ingrese la calificacion del examen parcial (0-100):"))
examen_final = float(input("Ingrese la califacion del examen final (0-100): "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)
print(f"La calificacion final es:  {calificacion_final:.2f}")