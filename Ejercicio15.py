nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
descuento_porcentaje = float(input("Ingrese el porcentaje de descuento: "))

descuento = (descuento_porcentaje / 100) * precio_producto
precio_final = precio_producto - descuento


print(f"Producto: {nombre_producto}")
print(f"Precio final despues del descuento: {precio_final:.2f}")
