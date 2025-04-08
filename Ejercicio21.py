presion = float(input("Ingrese la presion: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"La masa es: {masa:.2f}")
