#Analisamos la complejidad 
#comparando la busqueda ineal con la busqueda binaria 

import time #Permite hacer calculo de tiempo
import random #genera aleatoridad

def busqueda_lineal(arr,objetivo):
    for i, num in enumerate(arr):
        if num == objetivo:
            return i

    return -1    #el valor no fue encontrado 


#Busqueda binaria 

def busqueda_binaria(arr,objetivo):
    inicio, final = 0, len(arr)-1

    while inicio<= final:
        medio= int((inicio + final )/2)
        if arr[medio]== objetivo:
            return medio
        elif arr[medio]<objetivo:
            inicio = medio +1 
        else :
            final = medio-1

        return -1 # no se encontro el elemento    

#Generar datos para la prueba 😢 

n = 10**6 #  Generar la lista de 1 millon de elementos 

Datos = sorted(random.sample(range(n*10),n)) #Lista para la busqueda ordenar 
objetivo = random.choice(Datos)#elegimos un valor al azar 

# Medicion de tiempo lineal 

inicio = time.time() # inicia cuenta 

busqueda_lineal(Datos,objetivo)# ejecutamos algoritmo de busqueda lineal 

fin = time.time() # finalizacion de cuenta 


tiempo_lineal= fin - inicio # Calcular del tiempo en lineal 

# Medicion de tiempo lineal 

inicio= time.time()

busqueda_binaria(Datos,objetivo)

fin=  time.time()

tiempo_binario = fin - inicio

#imprimir los resultados 

print(f"Busqueda lineal (O(n)): {tiempo_lineal:.6f} segundos")
print(f"Busqueda binaria (O(n)): {tiempo_binario:.6f} segundos ")




