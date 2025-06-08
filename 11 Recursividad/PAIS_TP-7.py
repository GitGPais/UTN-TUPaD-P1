#TP N° 7: Recursividad
#Ejercicio 1
def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#Ejercicio 2
def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)

#Ejercicio 3:
def potencia(base, exponente):
    if exponente == 0:  # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Paso recursivo

#Ejercicio 4:
def decimal_a_binario(n):
    """Función recursiva para convertir un número decimal a binario"""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  # Divide y concatena el resto
    
    #Ejercicio 5:
def es_palindromo(palabra):
    # """Función recursiva que verifica si una palabra es un palíndromo."""
    if len(palabra) <= 1:  # Caso base: una cadena vacía o de un solo carácter es palíndroma
        return True
    elif palabra[0] != palabra[-1]:  # Si el primer y último carácter son distintos, no es palíndromo
        return False
    else:
        return es_palindromo(palabra[1:-1])  # Llamada recursiva con la palabra sin sus extremos
    
# Ejercicio 6:
def suma_digitos(n):
    """Función recursiva para calcular la suma de los dígitos de un número entero positivo."""
    if n == 0:  # Caso base: cuando n es 0, la suma es 0
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)  # Suma el último dígito y llama a la función con el return

#Ejercicio 7:
def contar_bloques(n):
    """Función recursiva para calcular la cantidad total de bloques en la pirámide."""
    if n == 1:  # Caso base: si solo hay un bloque, el total es 1
        return 1
    else:
        return n + contar_bloques(n - 1)  # Suma el nivel actual y llama a la función con el siguiente nivel

#Ejercicio 8:
def contar_digito(numero, digito):
    """Función recursiva para contar cuántas veces aparece un dígito en un número."""
    if numero == 0:  # Caso base: cuando el número es 0, no hay más dígitos que contar
        return 0
    else:
        # Comparamos el último dígito con el dígito buscado
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Programa principal
#Ejercicio 1
n = int(input("Ingrese un numero entero positivo: "))
print("El factorial de", n, "es:", factorial(n))
for i in range(1, n + 1):
    print(f"Factorial de {i} es: {factorial(i)}")

#Ejercicio 2
n = int(input("Ingrese un numero entero positivo para la serie de Fibonacci: "))
print("La serie de Fibonacci en la posición indicada", n, "es:", fabonacci(n))
for i in range(n + 1):
    print(fabonacci(i), end=' ')

#Ejercicio 3:
base = int(input("Introduce el número base: "))
exponente = int(input("Introduce el exponente: "))

resultado = (base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")

#Ejercicio 4:
# Solicitar un número al usuario
num = int(input("Introduce un número entero positivo: "))

# Obtener la representación en binario
resultado = decimal_a_binario(num)

print(f"El número {num} en binario es: {resultado}")

#Ejercicio 5:
entrada = input("Introduce una palabra sin espacios ni tildes: ").lower()

if es_palindromo(entrada):
    print(f"La palabra '{entrada}' es un palíndromo.")
else:
    print(f"La palabra '{entrada}' no es un palíndromo.")

#Ejercicio 6:
num = int(input("Introduce un número entero positivo: "))

resultado = suma_digitos(num)

print(f"La suma de los dígitos de {num} es: {resultado}")

#Ejercicio 7:

num = int(input("Introduce la cantidad de bloques en el nivel más bajo: "))

resultado = contar_bloques(num)

print(f"Para construir la pirámide con {num} bloques en la base, necesitas un total de {resultado} bloques.")

#Ejercicio 8:
num = int(input("Introduce un número entero positivo: "))
d = int(input("Introduce el dígito a contar (0-9): "))

resultado = contar_digito(num, d)

print(f"El dígito {d} aparece {resultado} veces en el número {num}.")