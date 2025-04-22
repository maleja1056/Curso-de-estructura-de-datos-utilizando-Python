class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.comienzo = None
        self.final = None

    def esta_vacia(self):
        return self.comienzo is None    

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.comienzo = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            return "La cola esta vacia. No hay elementos para desencolar."
        dato = self.comienzo.dato
        self.comienzo = self.comienzo.siguiente

        if self.comienzo is None:
            self.final = None
        return dato
    
    def mirar(self):
        if self.esta_vacia():
            return "La cola está vacía."
        return self.comienzo.dato

    def mostrar(self):
        actual = self.comienzo
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
print("\n Elementos con colas enlazadas :")
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Elementos en la cola:", cola.mostrar())
print("Desencolando:", cola.desencolar())
print("Nuevo frente:", cola.mirar())
print("Elementos después de desencolar:", cola.mostrar())

#cola con vectores
class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, dato):
        self.cola.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            return "La cola está vacía. No se puede desencolar."
        return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0

    def mirar(self):
        if self.esta_vacia():
            return "La cola está vacía."
        return self.cola[0]

    def mostrar(self):
        return self.cola

# Ejemplo de uso
print("\n Elementos con colaa con vectores :")
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Elementos en la cola:", cola.mostrar())
print("Desencolando:", cola.desencolar())
print("Elemento al frente:", cola.mirar())
print("Elementos después de desencolar:", cola.mostrar())