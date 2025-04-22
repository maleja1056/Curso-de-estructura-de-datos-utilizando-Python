import random

print ("Busqueda secuencial")

def busqueda_secuencial(arr,objetivo):
    for i, num in enumerate(arr):
        print (i)
        if num == objetivo:
            print(objetivo,i)
            return i
    return -1

n = 10*6
datos = sorted(random.sample(range(n*10),n))
objetivo = random.choice(datos)
print(datos)

print(f"[{objetivo}]")

busqueda_secuencial(datos,objetivo)

print("\nGeneracion de combinaciones: ")

a = input("Por favor digite un numero 1: ")
b = input("Por favor digite un numero 2: ")
c = input("Por favor digite un numero 3: ")
numeros = [a, b, c]
print(f"Las combinaciones de {a}, {b} y {c} son: ")

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and i != k and j != k:
                print (f"{numeros[i]}, {numeros[j]}, {numeros[k]}")
                
print("\nResolucion de sudoku por prueba y error.")

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else "." for num in fila))

def es_valido(tablero, fila, columna, num):
    for i in range(9):
        if tablero[fila][i] == num or tablero[i][columna] == num:
            return False
        if tablero[fila//3*3 + i//3][columna//3*3 + i%3] == num:
            return False
    return True

def jugar_sudoku(tablero, fijos, solucion):
    while True:
        imprimir_tablero(tablero)
        fila = int(input("Ingrese la fila (0-8): "))
        columna = int(input("Ingrese la columna (0-8): "))
        
        if (fila, columna) in fijos:
            print("No puedes cambiar un número fijo.")
            continue
        
        num = int(input("Ingrese el número (1-9): "))
        
        if es_valido(tablero, fila, columna, num):
            tablero[fila][columna] = num
            print("¡Número válido colocado!")
        else:
            print("Número no válido. Intenta de nuevo.")
        
        # Verificar si el tablero coincide con la solución
        if tablero == solucion:
            print("\n¡Sudoku completado correctamente!")
            imprimir_tablero(tablero)
            break
        elif all(tablero[fila][columna] != 0 for fila in range(9) for columna in range(9)):
            print("\nSudoku completo, pero con errores. Intenta nuevamente.")
            imprimir_tablero(tablero)

# Tablero inicial
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solución esperada
solucion = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Identificar posiciones fijas
fijos = {(fila, columna) for fila in range(9) for columna in range(9) if sudoku[fila][columna] != 0}

jugar_sudoku(sudoku, fijos, solucion)















































  

