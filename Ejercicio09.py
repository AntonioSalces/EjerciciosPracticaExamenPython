'''
Ejercicio 9: bucle While
Escribe un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario tiene que adivinarlo). 
El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y después el 
usuario va probando valores y el programa va diciendo si son demasiado grandes o pequeños.

Nota: Para generar el número a adivinar utiliza la función randrange(mínimo, máximo, paso) del módulo random. Para poder 
utilizar la función randrange tendrás que incluir en el programa la instrucción siguiente:

from random import randrange

Valor mínimo: 0

Valor máximo: 100

A ver si adivinas un número entero entre 0 y 100.

Escribe un número: 20

¡Demasiado pequeño! Inténtalo de nuevo: 30

¡Demasiado grande! Inténtalo de nuevo: 27

¡Acertaste! Te ha costado 3 intentos
'''

from random import randrange

print("Primer valor: ")
first = int(input())
print("Segundo valor: ")
last = int(input())

rango = randrange(first, last, 1)

number = int(input("Elige tu primer número: "))

while(number != rango):
    if(number < rango):
        number = int(input("Es más grande. Indica otro: "))
    else:
        number = int(input("Es más pequeño. Indica otro: "))

print("Enhorabuena, el número es", rango)