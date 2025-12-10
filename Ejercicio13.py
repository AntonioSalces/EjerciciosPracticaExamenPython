'''
Ejercicio 13: Operaciones encadenadas
Escribe una función “encadenar_operaciones” que tome dos listas de números como argumentos y:

Cree una nueva lista que contenga los elementos únicos presentes en ambas listas.
Ordene la lista resultante de forma descendente.
Devuelva la suma de los tres primeros elementos.
Ejemplo de uso:

print(encadenar_operaciones([1, 2, 3, 4], [3, 4, 5, 6]))

Salida esperada: 15 (ya que la lista combinada sería [6, 5, 4, 3, 2, 1])
'''
list1 = [1,2,3,4]
list2 = [3,4,5,6]

def encadenar_operaciones(list1, list2):
    newList= []
    for i in list1:
        if (i not in newList):
            newList.append(i)
    for i in list2:
        if (i not in newList):
            newList.append(i)
    newList.sort(reverse=True)

    suma = 0
    for i in newList[:3]:
        suma += i
    return suma, newList

suma, lista = encadenar_operaciones(list1, list2)
print("Suma:", suma, "Lista:", lista)