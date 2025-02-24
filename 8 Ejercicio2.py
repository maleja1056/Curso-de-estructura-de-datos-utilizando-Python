"""
Escribe un programa en python que solicite al usuario los siguientes datos su nombre tipo  str su edad tipo int 
el total de la cuenta en un restaurante tipo float % de propina tipo int el programa debe asegurarse que el valores 
sea valido debe calcular la cantidad de propina el total a pagar cuenta mas propina  y un mensaje personalisado segun la edad del usuario
brindele al usuario la posibllidad de eleguir los productos de un menu antes de calcular  la propina

"""

# ingreso de datos 

nombre= str(input("digite su nombre "))# tipo str 
while not nombre.isalpha():
    nombre= str(input("digite su nombre "))
edad=int(input("digite su edad "))#tipo int
totalcuenta = float()



# Menu del restaurante

menu=[
    ("Bandeja ejecutiva",8000),
    ("Bandeja especial", 10000),
    ("sopa",3000),
    ("fruta",3000),
    ("Doble proteina",3000)
]
#mostar productos  y permiir la compra usando lista y diccionarios.
#pedido 
print("MENÚ")
for i,(producto,precio) in enumerate(menu, 1):
    print(f"{i}. {producto}-$ {precio}")

    cuenta=[] #La lista donde va almacenar el pedido

    tomandopedido = True #variable para controlar la compra 

while tomandopedido:
    opcion = int(input("\ndigite la opcion que desee(0 para salir: )"))

    if opcion==0:
        tomandopedido= False
    elif 1<=opcion<= len(menu):
        producto,precio=menu[opcion-1]
        cuenta.append((producto,precio))
        print(f"{producto} su pedido fue tomado")
    else:
        print("valor no valido")

#calcular el total del pedido sin propina
totalcuenta=sum(precio for _, precio in cuenta)
print(f"\nEl total a pagar es: {totalcuenta}")

#calcular el total del pedido con la propina
Ppropina =int(input("cuanto porcentaje deseas dar de propina: "))
propina =(totalcuenta/100)*Ppropina

totalcuentap =int()

totalcuentap= propina +totalcuenta

# muestra el mensaje personalizado
print(f"La cuenta total de su pedido es: {totalcuentap}")

if edad<=15:
    print("Buena eleccion para tu almuerzo")
elif 15<=25:
    print("Come mas verduras")
elif 25<=50:
    print("Bajale a lo carboidratos")
elif 50<90:
    print("come comida casera no fritos")
else:
    print("que haces aca")
    

