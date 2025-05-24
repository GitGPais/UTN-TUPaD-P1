# TP FUNCIONES

# ACTIVIDAD 1: Crear una función que imprima "Hola Mundo!"
def imprimir_hola_mundo():
    # Devuelve el mensaje "Hola Mundo!"
    return "Hola Mundo!"

# ACTIVIDAD 2: Crear una función que devuelva un saludo personalizado
def saludar_usuario(nombre):
    # Devuelve un saludo usando el nombre recibido como parámetro
    return f"Hola {nombre}!"

# ACTIVIDAD 3: Crear una función que devuelva información personal dada por el usuario
def informacion_personal(nombre, apellido, edad, residencia):
    # Devuelve una cadena con los datos personales recibidos
    return f"Soy {nombre}, {apellido}, tengo {edad} años y vivo en {residencia}"

# ACTIVIDAD 4: Calcular área y perímetro de un círculo
def calcular_area_circulo(radio):
    # Calcula el área de un círculo usando la fórmula π*r^2
    return 3.14 * radio ** 2

def calcular_perimetro_circulo(radio):
    # Calcula el perímetro de un círculo usando la fórmula 2*π*r
    return 2 * 3.14 * radio

# ACTIVIDAD 5: Convertir segundos a horas
def segundos_a_horas(segundos):
    # Convierte los segundos recibidos a horas
    horas = segundos / 3600
    return f"{horas} horas"

# ACTIVIDAD 6: Imprimir la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    # Imprime la tabla de multiplicar del número recibido del 1 al 10
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")

# ACTIVIDAD 7: Operaciones básicas entre dos números
def operaciones_basicas(a, b):
    # Devuelve una tupla con suma, resta, multiplicación y división de a y b
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

# ACTIVIDAD 8: Calcular el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    # Calcula el IMC usando la fórmula peso / altura^2 y redondea a 2 decimales
    return round(peso / altura ** 2, 2)

# ACTIVIDAD 9: Convertir Celsius a Fahrenheit
def celsius_a_farenheit(celsius):
    # Convierte la temperatura de Celsius a Fahrenheit
    return celsius * 9 / 5 + 32

# ACTIVIDAD 10: Calcular el promedio de tres números
def calcular_promedio(a, b, c):
    # Calcula el promedio de tres números recibidos como parámetros
    return (a + b + c) / 3

# ------------------- PROGRAMA PRINCIPAL -------------------

# Act 1: Imprime "Hola Mundo!"
mensaje = imprimir_hola_mundo()  # Llama a la función que devuelve "Hola Mundo!"
print(mensaje)  # Muestra el mensaje por pantalla

# Act 2: Saludo personalizado
Nombre_usuario = input("Ingresar nombre de usuario: ")
print(saludar_usuario(Nombre_usuario))  # Llama a la función de saludo y muestra el resultado

# Act 3: Información personal
Nombre_usuario = input("Ingresa tu nombre: ")
Apellido_usuario = input("Ingresa tu apellido: ")
Edad_usuario = input("Ingresa tu edad: ")
Residencia_usuario = input("Ingresa tu lugar de residencia: ")
# Muestra la información personal usando los datos ingresados llamando a la función
print(informacion_personal(Nombre_usuario, Apellido_usuario, Edad_usuario, Residencia_usuario)) 

# Act 4: Área y perímetro de un círculo
Radio_Usuario = float(input("Ingrese el radio del circulo: "))
Area = calcular_area_circulo(Radio_Usuario)  # Calcula el área llamando a la función
Perímetro = calcular_perimetro_circulo(Radio_Usuario)  # Calcula el perímetro llamando a la función
print(f"El area del circulo es: ", Area)
print(f"El perímetro del círculo es: ", Perímetro)

# Act 5: Conversión de segundos a horas
Segundos_Usuario = float(input("Ingresa la cantidad de segundos: "))
Resultado = segundos_a_horas(Segundos_Usuario)  # Convierte segundos a horas llamando a la función
print(Resultado)

# Act 6: Tabla de multiplicar
Numero_Usuario = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(Numero_Usuario)  # Imprime la tabla de multiplicar llamando a la función

# Act 7: Operaciones básicas
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
Resultados = operaciones_basicas(a, b)  # Realiza operaciones básicas llamando a la función
print(f"suma: {Resultados[0]}, resta: {Resultados[1]}, multiplicación {Resultados[2]}, división {Resultados[3]}")  # Imprime los resultados en forma de tupla

# Act 8: Cálculo de IMC
Peso_Usuario = float(input("Ingrese su peso en kilogramos: "))
Altura_Usuario = float(input("Ingrese su altura en metros: "))
IMC = calcular_imc(Peso_Usuario, Altura_Usuario)  # Calcula el IMC llamando a la función
print(f"Tu IMC es: {IMC}")

# Act 9: Conversión de Celsius a Fahrenheit
Celsius_Usuario = float(input("Ingrese la temperatura en grados °C: "))
Temperatura_Farenheit = celsius_a_farenheit(Celsius_Usuario)  # Convierte a Fahrenheit llamando a la función
print(f"{Celsius_Usuario} °C equivalen a {Temperatura_Farenheit}°F")

# Act 10: Promedio de tres números ingresados por el usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)  # Calcula el promedio llamando a la función
print(f"El promedio de {a}, {b} y {c} es: {promedio}")