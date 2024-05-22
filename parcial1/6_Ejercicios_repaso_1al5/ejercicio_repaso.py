#crear un programa que calcule y obtenga el total a pagar por un producto determinado. se debera de solicitar el nombre o descripcion del producto, codigo, cantidad del producto, precio unitario del producto.
#El total a pagar incluye el iva y el descuento.
#Si se compran de 1 a 5 productos se otorga el 10% de descuento, si se compran de 6 a 10 el 15% de descuento, y si se compran mas de 10 el 20%

nombre_producto = input("Ingrese el nombre o descripcion del producto: ")
codigo_producto = input("Ingrese el codigo del producto: ")
cantidad_producto = int(input("Ingrese la cantidad del producto: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

subtotal = cantidad_producto * precio_unitario

if 1 <= cantidad_producto <= 5:
    descuento = subtotal * 0.10
elif 6 <= cantidad_producto <= 10:
    descuento = subtotal * 0.15
else:
    descuento = subtotal * 0.20

iva = subtotal * 0.16

total = subtotal - descuento + iva

print(f"Producto: {nombre_producto}")
print(f"Codigo: {codigo_producto}")
print(f"Cantidad: {cantidad_producto}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"IVA: ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")