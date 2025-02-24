""""
el ususario debe registar su informacion personal(nombre,edad, saldo en cuenta), se alamacenara una lista de productos disponibles
en la tienda cada uno con su precio, se permitira que el ususario agregue productos a su carrito de compras se calculara el total de la compra y se verificara
si el saldo del usuario es suficiente se mostrara un resumen con los productos comprados y el saldo restante.


"""

# Ingreso de datos 

nombre = input("digite su nombre: ") #tipo str
edad = int(input("digite su edad: ")) # tipo int 
saldo = float(input("digite su saldo: "))# tipo float


# Lista de productos de la tienda 

productos=[
    ("portatil",1200000),
    ("mouse",45000),
    ("lapiz",150000),
    ("celular",2000000),
    ("forro celular",30000)
    ]

# parte 3, mostar productos  y permiir la compra usando lista y diccionarios.
#Carrito de compras 

print("\nLista de productos disponibles: ")
for i,(producto, precio) in enumerate(productos,1):
    # f-string o cadena formateada 
    print(f"{i}. {producto} - $ {precio}")

    carrito = [] #La lista donde va almacenar los productos

    comprando = True  #variable para controlar la compra 

while comprando:
        opcion =int(input("\n Seleccione el numero de producto que desea comprar ( 0 para salir): "))
        if opcion==0:
            comprando= False 

        elif 1<=opcion <= len(productos):
            producto,precio = productos[opcion - 1]
            carrito.append((producto, precio))#guardar en el carrito de compras
            print(f"¡{producto} agregado al carrito!")
        else:
            print("valor no valido")

#calcular el total de la compra
totalc= sum(precio for _,precio in carrito)
print(f"\n el total de la compra es: {totalc}")

#verificar el presupuesto
    
if saldo>=totalc:
        saldo-=totalc
        print("\n compra realizada")
else:
        print ("Saldo insuficiente")

print(f"su saldo actual es{saldo}")      
