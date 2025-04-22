def verifica_simbolos(expr):
    #Se crea la  pila 
    pila = []  

    for sim in expr:
        if sim == '(' or sim == '[' or sim == '{':  # simbolos de apertura
            pila.append(sim)
        elif sim == ')':  # simbolo de cierre para )
            if len(pila) > 0 and pila[-1] == '(':
                pila.pop()
            else:
                return False
        elif sim == ']':  # simbolo de cierre para ]
            if len(pila) > 0 and pila[-1] == '[':
                pila.pop()
            else:
                return False
        elif sim == '}':  # simbolo de cierre para }
            if len(pila) > 0 and pila[-1] == '{':
                pila.pop()
            else:
                return False

   
    return len(pila) == 0

operacion = input("Digite la operación matemática: ")
if verifica_simbolos(operacion):
    print("La operación esta balanceada .")
else:
    print("La operación no esta balanceada ")