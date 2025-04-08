producto1 = float(input("Ingrese el precio del primer producto: "))
producto2 = float(input("Ingrese el precio del segundo producto: "))
producto3 = float(input("Ingrese el precio del tercer producto: "))

subtotal = producto1 + producto2 + producto3
iva = subtotal * 0.15
total_a_pagar = subtotal + iva


print(f"Subtotal: {subtotal:.2f}")
print(f"IVA (15%): {iva:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")
