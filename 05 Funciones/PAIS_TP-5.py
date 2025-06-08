#Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
numeros_multiplos_4= list(range(4,101,4)) #Creamos una lista que va del 4 al 100 inclusive con los múltiplos de dicho número
print (numeros_multiplos_4) #La imprimimos

#Ejercicio 2: Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# #¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
mi_lista= [10, 20, 30, 40, 50] #Hacemos una lista con numeros cualquiera
print (mi_lista[-2]) #Utilizamos index para imprimir el penúltimo

#Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
mi_lista_vacia= [] #Hacemos una lista vacía
mi_lista_vacia.append("Hola") #Agregamos
mi_lista_vacia.append("Mundo") #Tres 
mi_lista_vacia.append("Programación") #Palabras
print (mi_lista_vacia) #Imprimimos lista resultante

#Ejercicio 4 : Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"]
animales =["perro", "gato", "conejo", "pez"]
animales [1] = "loro" #Cambia gato por loro
animales [3] = "oso" #Cambia pez por oso
print (animales) #Imprime lista resultante

#Ejercicio 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza:
# numeros = [8, 15, 3, 22, 7]
#numeros.remove (max(numeros))
#print numeros 
numeros= [8, 15, 3, 22, 7]
numeros.remove (max(numeros)) #Lo que hace esta función es remover o eliminar el número máximo o mayor de la lista.
print (numeros) #Imprime la lista resultante

#Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros
lista_numeros = list(range (10, 31, 5)) #Numeros desde el 10 hasta el 30 inclusive de 5 en 5
print (lista_numeros[0]) #Imprime el primero
print (lista_numeros [1]) #Imprime el segundo

#Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]
autos = ["sedan", "polo", "suran", "gol"]
autos [1] = "Voyage" #Cambia polo por voyage
autos [2] = "Vento" #Cambia suran por vento
print (autos) #Imprimimos lista actualizada

#Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
dobles = []
dobles.append (5*2) #Doble de 5
dobles.append (10*2) #Doble de 10
dobles.append (15*2) #Doble de 15
# Imprimir la lista resultante por pantalla.
print (dobles) 

#Ejercicio 9: 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras= [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append ("jugo")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras [1][1]= "tallarines"
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove ("pan")
#d) Imprimir la lista resultante por pantalla
print (compras)

#Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False] #Agregamos a la lista los elementos en el orden establecido
print (lista_anidada) #Imprimimos la lista resultante