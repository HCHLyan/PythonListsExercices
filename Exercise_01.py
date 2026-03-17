# Crear una lista de 10 números enteros e imprimir el número mayor.
# Dada una lista de números, contar cuántos son pares y cuántos impares.
# Invertir el orden de una lista sin usar funciones propias del lenguaje.
# Eliminar los elementos duplicados de una lista y mostrar la nueva lista.
# Dada una lista de notas, calcular el promedio y mostrar si el estudiante aprueba (>= 3.0).

#Ejercicio 1

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mayor = numeros[0]

for i in numeros:
    if i > mayor:
        mayor = i

print(f"El número mayor es: {mayor}")

#Ejercicio 2

pares = 0
impares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}. Impares: {impares}")

#Ejercicio 3

alreves = numeros[::-1]
print(alreves)

#Ejercicio 4

lista = [0,0,0,1,1,2,2,4,5,5,5,4,5,87,4,7]

no_duplicados = []

for i in lista:
    if elemento not in no_duplicados:
        
