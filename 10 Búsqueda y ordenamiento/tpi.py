import random
import timeit
from datetime import datetime

# 1. Generación de datos: Lista de calificaciones aleatorias
calificaciones = [random.randint(1, 100) for _ in range(1000)]  # Lista grande para mejor análisis
print("Calificaciones originales:", calificaciones[:10], "...")  # Solo mostramos las primeras 10

# 2. Ordenamiento con Bubble Sort
def bubble_sort(lista):   n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

# 3. Ordenamiento con Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivote]
        medio = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x > pivote]
        return quick_sort(izquierda) + medio + quick_sort(derecha)

# 4. Ordenamiento con Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# 5. Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return f"Calificación encontrada en la posición {medio}"
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return "Calificación no encontrada"

# Medir tiempos con datetime
inicio_bubble = datetime.now()
bubble_sort(calificaciones.copy())
fin_bubble = datetime.now()

inicio_quick = datetime.now()
quick_sort(calificaciones.copy())
fin_quick = datetime.now()

inicio_merge = datetime.now()
merge_sort(calificaciones.copy())
fin_merge = datetime.now()

# Medir tiempos con timeit
tiempo_bubble_sort = timeit.timeit(lambda: bubble_sort(calificaciones.copy()), number=10)
tiempo_quick_sort = timeit.timeit(lambda: quick_sort(calificaciones.copy()), number=10)
tiempo_merge_sort = timeit.timeit(lambda: merge_sort(calificaciones.copy()), number=10)

# Ordenar la lista con Quick Sort para la búsqueda binaria
calificaciones_ordenadas = quick_sort(calificaciones.copy())

# Seleccionar un valor aleatorio para buscar
objetivo = random.choice(calificaciones_ordenadas)

# Medir tiempo de ejecución de Búsqueda Binaria con datetime
inicio_busqueda = datetime.now()
busqueda_binaria(calificaciones_ordenadas, objetivo)
fin_busqueda = datetime.now()

# Medir tiempo de ejecución de Búsqueda Binaria con timeit
tiempo_busqueda_binaria = timeit.timeit(lambda: busqueda_binaria(calificaciones_ordenadas, objetivo), number=10)

# Mostrar resultados comparativos
print(f"Tiempo Bubble Sort con datetime: {fin_bubble - inicio_bubble} segundos")
print(f"Tiempo Bubble Sort con timeit: {tiempo_bubble_sort:.6f} segundos")

print(f"Tiempo Quick Sort con datetime: {fin_quick - inicio_quick} segundos")
print(f"Tiempo Quick Sort con timeit: {tiempo_quick_sort:.6f} segundos")

print(f"Tiempo Merge Sort con datetime: {fin_merge - inicio_merge} segundos")
print(f"Tiempo Merge Sort con timeit: {tiempo_merge_sort:.6f} segundos")

print(f"Tiempo Búsqueda Binaria con datetime: {fin_busqueda - inicio_busqueda} segundos")
print(f"Tiempo Búsqueda Binaria con timeit: {tiempo_busqueda_binaria:.6f} segundos")

print(busqueda_binaria(calificaciones_ordenadas, objetivo))