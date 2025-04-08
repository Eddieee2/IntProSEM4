
total_estudiantes = int(input("Ingrese el número total de estudiantes: "))
mujeres = int(input("Ingrese el número de mujeres en el aula: "))
hombres = int(input("Ingrese el número de hombres en el aula: "))

porcentaje_mujeres = (mujeres / total_estudiantes) * 100
porcentaje_hombres = (hombres / total_estudiantes) * 100

print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
