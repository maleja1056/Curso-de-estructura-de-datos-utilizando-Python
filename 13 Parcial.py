import time

inicio = time.time()
Tienda = []
elementos = int(input("Digite la cantidad de productos que desea ingresar: "))
for i in range(elementos):
    nombre_del_producto = input("Digite el nombre del producto: ")
    precio_unitario = float(input("Digite el precio del producto: "))
    Tienda.append((nombre_del_producto, precio_unitario))
    print("Se guardó el producto")

print(Tienda)

print("Los productos de la lista son:")

for i, (nombre_del_producto, precio_unitario) in enumerate(Tienda, 1):
    print(f"{i}. {nombre_del_producto} - {precio_unitario}")

# Filtrar y mostrar productos que superan el valor de 100000
productos_caros = [producto for producto in Tienda if producto[1] > 100000]

if productos_caros:
    print("Los productos que superan el valor de 100000 son:")
    for nombre_del_producto, precio_unitario in productos_caros:
        print(f"{nombre_del_producto} - {precio_unitario}")
else:
    print("Todos sus productos fueron económicos")

fin = time.time()
duracion = fin - inicio
print(f"El tiempo de duración del código es: {duracion:.2f} segundos")


