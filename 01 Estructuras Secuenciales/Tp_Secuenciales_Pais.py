#Ejercicio 1 : Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola mundo!")

#Ejercicio 2 : Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
Nombre = input ("Por favor ingresa tu nombre: ")
print (f"¡Hola {Nombre}!")

#Ejercicio 3 :  Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
Nombre = input ("Por favor, ingresa tu nombre: ")
Apellido = input ("Por favor, ingresa tu apellido: ")
Edad = input ("Por favor ingresa tu edad: ")
LugarResidencia= input ("Por favor, ingresa tu lugar de residencia: ")
print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {LugarResidencia}")

#Ejercicio 4 : Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
Radio = input ("Ingresa el radio de un círculo: ")
Radio = float (Radio)
AreaCirculo = float(3.14*Radio*Radio)
PerimetroCirculo = float(2*3.14*Radio)
print(f"El area del círculo es de {AreaCirculo} y su perímetro es de {PerimetroCirculo}") 

#Ejercicio 5 :  Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
CantSegundos= input ("Ingrese la cantidad de segundos: ")
CantSegundos = float(CantSegundos)
Horas = float(CantSegundos/3600)
print ("La cantidad de segundos equivale a: ", Horas)

#Ejercicio 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
N= int(input ("Ingrese un número, por favor: "))
print ()
for i in range (1,11):
    print(f"{N}*{i} = {i*N}")

    #Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
Num1 = int(input("Ingrese el primer número: "))
Num2= int(input("Ingrese el segundo número: "))
Suma= Num1+Num2
División= Num1/Num2
Multiplicación= Num1*Num2
Resta= Num1-Num2
print ("La suma es", Suma)
print ("La división es", División)
print ("La multiplicación es", Multiplicación)
print ("La resta es", Resta)

#Ejercicio 8 :  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal
Altura= float(input("Ingrese su altura en metros: "))
Peso= float(input("Ingrese su peso en kg: "))
IMC= Peso/Altura
print ("El indice de masa corporal es de", IMC)

#Ejercicio 9 : Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
Temperatura= float(input("Ingrese la temperatura en °C:"))
TemperaturaF= float(9/5 * Temperatura + 32)
print ("La temperatura en °C equivale a", TemperaturaF, "°F")

#Ejercicio 10:  Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números
Num1= float(input("Ingrese el primer número: "))
Num2= float(input("Ingrese el segundo número: "))
Num3= float(input ("Ingrese el último número: "))
Promedio = float(Num1+Num2+Num3/3)
print ("El promedio de los tres números es", Promedio)

