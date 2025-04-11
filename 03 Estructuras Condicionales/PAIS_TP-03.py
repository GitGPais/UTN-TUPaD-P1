#TRABAJO_PRÁCTICO_3
## Ejercicio 1: 
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Solicitando la edad del usuario
Edad= int(input("Ingrese su edad, por favor: "))
#Colocando el condicional
if Edad > 18:
#Imprimiendo el resultado
    print("Es mayor de edad")

##Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
#en caso contrario deberá mostrar el mensaje “Desaprobado”.

#Solicitando la nota al usuario
NotaUsuario= int(input("Ingrese la nota: "))
#Condicionales
if (NotaUsuario>=6):
#Imprimiendo el resultado correspondiente
    print ("Aprobado")
else:
    print ("Desaprobado")

##Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en casocontrario, imprimir por pantalla 
# "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) 
# en Python para evaluar si un número es par o impar.

#Solicitando al usuario el número para comprobar si es par o impar
print("Ingrese el número a comprobar: ")
num = int(input())
#Si el numero ingresado tiene resto cero significa que es par 
if (num % 2 == 0):
    #Si es par, se imprimirá un mensaje que así lo indique y sino se volverá a soliciar un número
    print ("Ha ingresado un número par")
else: print("Por favor, ingrese un número par")

##Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#Solicitando la edad del usuario
edad= int(input("Ingrese su edad: "))
#Si es menor de doce es niño/a
if edad < 12:
    print("Niño/a")
 #Si es mayor de doce y menor de dieciocho es adolescente
elif 12 <= edad < 18:
    print("Adolescente")
#Si es mayor de 18 y menor de 30 es un adulto joven
elif 18 <= edad < 30:
    print("Adulto/a jóven")
#Si no es ninguna de las anteriores,  es un adulto
else:
    print("Adulto/a")

##Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña 
# de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el usode la función len() en Python para evaluar la cantidad 
# de elementos que tiene un iterable tal como una lista o un string.

#Solicitando al usuario una contraseña
contraseña = input("Por favor, ingrese una contraseña: ")
#Si tiene los caracteres correctos se imprimirá un mensaje que lo contemple
if 8 <= len (contraseña) <= 14:
    print ("Ha ingresado una contraseña correcta")
#De lo contrario, se imprimirá un mensaje solicitando una nueva
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

##Ejercicio 6
# Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mean, median, mode

# Crear lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Determinar el sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# Mostrar valores calculados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

##Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
# e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase_o_palabra= input ("Ingrese una frase o palabra: ")

#Verificando si termina en vocal con el comando lower
if frase_o_palabra [-1].lower() in 'aeiou':
    frase_o_palabra += '!'

#Imprimiendo el resultado
print("Resultado:", frase_o_palabra)

##Ejercicio 8 
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(),lower() y title() de Python para convertir entre mayúsculas y minúsculas.

#Solicitando nombre y opción al usuario
nombre = input("Ingrese su nombre: ")
print("Seleccione una opción: ")
print("1- Nombre en MAYUSCULAS")
print ("2- Nombre en minusculas")
print("3- Primera letra con mayuscula")
opcion = input ("Ingrese la opción que desee (1, 2 o 3)")

#Segun la opción deseada:
if opcion == '1':
    nombre = nombre.upper()
elif opcion == '2':
    nombre = nombre.lower()
elif opcion == '3':
    nombre = nombre.title()
else:
    print("Opción no valida")

#Imprimiendo el resultado
print ("Resultado", nombre)

##Ejercicio 9
#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías 
# según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#Solicitar la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

#Clasificar según la magnitud
if magnitud > 3:
    clasificación = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    clasificación= "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    clasificación= "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    clasificación= "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    clasificación = "Muy fuerte (puede causar daños significativos)"
else:
    clasificación = "Extremo (puede causar graves daños a gran escala)"

#Imprimiendo resultado
print ("Clasificación:", clasificación)

##Ejercicio10
#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

#Solicitando datos al usuario
Hemisferio= input("¿En qué hemisferio te escuentras? (norte/sur):").strip().lower()
mes = int(input("¿En qué mes te encuentras?(1-12): "))
día= int(input("¿Qué día es? (1-31):"))

#Determinando la estación
estación = ""

if Hemisferio == "sur":
    if (mes == 3 and día >= 21) or (mes in [4, 5]) or (mes == 6 and día < 21):
        estacion = "Otoño"
    elif (mes == 6 and día >= 21) or (mes in [7, 8]) or (mes == 9 and día < 21):
        estacion = "Invierno"
    elif (mes == 9 and día >= 21) or (mes in [10, 11]) or (mes == 12 and día < 21):
        estacion = "Primavera"
    else:
        estacion = "Verano"
elif Hemisferio == "norte":
    if (mes == 3 and día >= 21) or (mes in [4, 5]) or (mes == 6 and día < 21):
        estacion = "Primavera"
    elif (mes == 6 and día >= 21) or (mes in [7, 8]) or (mes == 9 and día < 21):
        estacion = "Verano"
    elif (mes == 9 and día >= 21) or (mes in [10, 11]) or (mes == 12 and día < 21):
        estacion = "Otoño"
    else:
        estacion = "Invierno"
else:
    estacion = "Hemisferio no válido."

# Mostrar el resultado
print("Estación actual:", estacion)
    