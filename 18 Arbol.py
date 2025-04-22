# Definimos la clase Nodo para representar cada elemento del árbol
class Nodo:
    # Corregido: __init__ en lugar de _init_
    def __init__(self, valor):
        # Cada nodo tendrá un valor
        self.valor = valor
        # Referencia al hijo izquierdo
        self.izquierda = None
        # Referencia al hijo derecho
        self.derecha = None

# Función para recorrido inorden (izquierda-raíz-derecha)
def recorrido_inorden(nodo):
    if nodo is not None:
        # Recorremos el subárbol izquierdo
        recorrido_inorden(nodo.izquierda)
        # Visitamos el nodo actual
        print(nodo.valor, end=' ')
        # Recorremos el subárbol derecho
        recorrido_inorden(nodo.derecha)

# Función para insertar un nodo en el árbol
def insertar_nodo(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    elif valor > raiz.valor:
        raiz.derecha = insertar_nodo(raiz.derecha, valor)
    return raiz

# Función para llenar el árbol con valores ingresados por el usuario
def llenado_de_arbol():
    raiz = None
    nodos_ingresados = 0
    print("El primer valor será la raíz.")
    
    while nodos_ingresados < 7:
        entrada = input("Por favor ingrese un valor: ")
        try:
            valor = int(entrada)
            if raiz is None:
                raiz = Nodo(valor)  # Creamos la raíz con el primer valor
            else:
                insertar_nodo(raiz, valor)  # Insertamos en el árbol existente
            nodos_ingresados += 1
        except ValueError:
            print("Entrada incorrecta, por favor ingrese un valor entero.")
    
    print("\nEl recorrido inorden del árbol es: ")
    recorrido_inorden(raiz)
    print()  # Salto de línea al final

# Ejemplo de creación manual de un árbol (opcional)
def ejemplo_arbol_manual():
    # Creamos nodo raíz
    raiz = Nodo(10)
    # Creamos los hijos izquierdo y derecho
    raiz.izquierda = Nodo(5)
    raiz.derecha = Nodo(20)
    # Agregamos más niveles
    raiz.izquierda.izquierda = Nodo(3)
    raiz.izquierda.derecha = Nodo(7)
    raiz.derecha.derecha = Nodo(25)
    raiz.derecha.izquierda = Nodo(15)
    
    print("Recorrido inorden del árbol manual:")
    recorrido_inorden(raiz)
    print()  # Salto de línea al final

# Ejecutamos las funciones
if __name__ == "__main__":
    ejemplo_arbol_manual()  # Opcional: muestra el árbol creado manualmente
    llenado_de_arbol()     # Solicita valores al usuario y muestra el árbol