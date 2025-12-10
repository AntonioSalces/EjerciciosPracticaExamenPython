'''
Escribe el código necesario para que, dada una lista de enteros:

Reordene la lista colocando los números pares al inicio y los impares al final.
Ejemplo:

[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

Salida esperada: [4, 2, 6, 3, 1, 1, 5, 9, 5, 3, 5]
'''

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

pares = [n for n in lista if (n % 2 == 0)]
impares = [n for n in lista if (n % 2 != 0)]
print(pares + impares)