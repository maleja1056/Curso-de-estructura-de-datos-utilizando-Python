# Datos de personas.

personasD = [
    {"nombre": "Maria", "edad": 5},
    {"nombre": "Alejandra", "edad": 20},
    {"nombre": "Jose", "edad": 60}
]

# Imprimir los datos de las personas
print("Los datos de las personas son:")

for persona in personasD:
    for clave, valor in persona.items():
        print(clave, ":", valor)
    print()  # Salto de línea para separar cada persona