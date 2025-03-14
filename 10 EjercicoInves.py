#Dicccionarios

Persona={
    "Nombre":"Maria Alejandra",
    "Edad": 18,
    "Estatura":1.59,
    "CC":1234567910,
    "Carrera":"ing.sistemas"
}
print("El diccionario tiene",len(Persona),"elementos")
print("los datos del estudiantes son: ")
for x,j in Persona.items():
    print(x,j)



#Tuplas

colores=("amarillo","azul","rojo")
print("La tupla tiene",len(colores),"elementos")
print("los colores de la bandera de colombia son : ")
for y in colores:
    print(y)

# Cojuntos 

menu={"arroz","trucha","tajadas","ensalada"}
print("Los cojuntos tiene",len(menu),"elementos")
print("el almuerzo de hoy es: ") 
for z in menu:
    print(z)
menu.add(input("Desea agrgar algo mas a su almuerzo "))
for z in menu:
    print(z)







